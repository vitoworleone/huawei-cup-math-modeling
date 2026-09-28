#!/usr/bin/env python3
"""可复制的二维科学图起点；CSV 示例只演示排版，不是论文结果。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.text import Text

PAPER_FONT_PT = 5.973632
AXIS_LINE_PT = 0.754564
TICK_LINE_PT = 0.503043
BLUE = "#2056A0"
RED = "#D83A46"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def setup_fonts(cjk_font: Path, cjk_bold_font: Path) -> None:
    for path in (cjk_font, cjk_bold_font):
        if not path.is_file():
            raise FileNotFoundError(f"字体不存在：{path}；请提供合法安装的字体文件")
        font_manager.fontManager.addfont(str(path))
    for family, weight in (
        ("Microsoft YaHei", "normal"),
        ("Microsoft YaHei", "bold"),
        ("Times New Roman", "normal"),
    ):
        font_manager.findfont(
            font_manager.FontProperties(family=family, weight=weight),
            fallback_to_default=False,
        )
    plt.rcParams.update({
        "font.family": ["Times New Roman", "Microsoft YaHei"],
        "font.size": PAPER_FONT_PT,
        "font.weight": "normal",
        "axes.labelsize": PAPER_FONT_PT,
        "axes.labelweight": "normal",
        "axes.titlesize": PAPER_FONT_PT,
        "axes.titleweight": "bold",
        "legend.fontsize": PAPER_FONT_PT,
        "xtick.labelsize": PAPER_FONT_PT,
        "ytick.labelsize": PAPER_FONT_PT,
        "axes.linewidth": AXIS_LINE_PT,
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "text.color": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.width": TICK_LINE_PT,
        "ytick.major.width": TICK_LINE_PT,
        "xtick.major.size": 3.145,
        "ytick.major.size": 3.145,
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "svg.fonttype": "path",
        "pdf.fonttype": 42,
        "axes.unicode_minus": False,
        "figure.facecolor": "white",
    })


def read_csv(path: Path, x_column: str, y_columns: list[str]) -> tuple[list[float], dict[str, list[float]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = [x_column, *y_columns]
        if not reader.fieldnames or any(name not in reader.fieldnames for name in required):
            raise ValueError(f"CSV 缺少所需列：{required}")
        rows = list(reader)
    if not rows:
        raise ValueError("CSV 没有数据行")
    x = [float(row[x_column]) for row in rows]
    series = {name: [float(row[name]) for row in rows] for name in y_columns}
    if any(not math.isfinite(value) for value in x + [v for ys in series.values() for v in ys]):
        raise ValueError("绘图列包含非有限数值")
    if any(right <= left for left, right in zip(x, x[1:])):
        raise ValueError("这个曲线模板要求 X 列严格递增；类别图或重复时间点需另选图型")
    return x, series


def draw(
    x: list[float],
    series: dict[str, list[float]],
    width_mm: float,
    height_mm: float,
    x_label: str,
    y_label: str,
    title: str,
    kind: str,
):
    fig, ax = plt.subplots(figsize=(width_mm / 25.4, height_mm / 25.4), dpi=160)
    fig.subplots_adjust(left=0.18, right=0.97, bottom=0.20, top=0.91)
    for index, (name, y) in enumerate(series.items()):
        color = (BLUE, RED)[index % 2]
        style = "-" if index % 2 == 0 else "--"
        if kind == "step":
            ax.step(x, y, where="post", color=color, linestyle=style, linewidth=1.1, label=name)
        else:
            ax.plot(x, y, color=color, linestyle=style, linewidth=1.1, marker="o",
                    markersize=2.6, label=name)
    ax.set_xlabel(x_label, labelpad=5.67)
    ax.set_ylabel(y_label, labelpad=5.67)
    if title:
        ax.set_title(title, pad=7.0)
    if len(series) > 1:
        ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linewidth=0.35, color="#E3E6EA")
    return fig


def export(fig, source: Path, out: Path, width_mm: float, dpi: int) -> None:
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    clipped = []
    off_axis_ticks = set()
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            low, high = sorted(axis.get_view_interval())
            for tick in axis.get_major_ticks() + axis.get_minor_ticks():
                if not low <= tick.get_loc() <= high:
                    off_axis_ticks.update((id(tick.label1), id(tick.label2)))
    for item in fig.findobj(Text):
        if not item.get_visible() or not item.get_text() or id(item) in off_axis_ticks:
            continue
        box = item.get_window_extent(renderer)
        if box.x0 < -1 or box.y0 < -1 or box.x1 > fig.bbox.width + 1 or box.y1 > fig.bbox.height + 1:
            clipped.append(item.get_text())
    if clipped:
        raise ValueError(f"文字越过画布：{clipped}")
    out.parent.mkdir(parents=True, exist_ok=True)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        for ext in ("png", "pdf", "svg"):
            fig.savefig(out.with_suffix("." + ext), dpi=dpi)
    missing = [str(w.message) for w in caught if "Glyph" in str(w.message) or "missing from font" in str(w.message)]
    if missing:
        raise ValueError("字体缺字：" + "; ".join(missing))
    outputs = {ext: sha256(out.with_suffix("." + ext)) for ext in ("png", "pdf", "svg")}
    out.with_suffix(".json").write_text(json.dumps({
        "source_name": source.name,
        "source_sha256": sha256(source),
        "paper_width_mm": width_mm,
        "png_dpi": dpi,
        "output_sha256": outputs,
        "visual_review": "待按论文实际插入宽度审阅",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--x-column", default="x")
    parser.add_argument("--y-columns", nargs="+", required=True)
    parser.add_argument("--x-label", default="参数 / —")
    parser.add_argument("--y-label", default="指标 / —")
    parser.add_argument("--title", default="")
    parser.add_argument("--kind", choices=("line", "step"), default="line")
    parser.add_argument("--width-mm", type=float, default=120)
    parser.add_argument("--height-mm", type=float, default=78)
    parser.add_argument("--dpi", type=int, default=320)
    parser.add_argument("--out", type=Path, required=True, help="不带扩展名的输出路径")
    parser.add_argument("--cjk-font", type=Path, default=Path(os.environ.get(
        "MODEL_FIG_CJK_FONT", str(Path.home() / "Library/Fonts/MicrosoftYaHei.ttf"))))
    parser.add_argument("--cjk-bold-font", type=Path, default=Path(os.environ.get(
        "MODEL_FIG_CJK_BOLD_FONT", str(Path.home() / "Library/Fonts/MicrosoftYaHei-Bold.ttf"))))
    args = parser.parse_args()
    if args.width_mm <= 0 or args.height_mm <= 0 or args.dpi < 300:
        parser.error("宽高须为正，PNG 导出 DPI 至少为 300")
    setup_fonts(args.cjk_font, args.cjk_bold_font)
    x, series = read_csv(args.csv, args.x_column, args.y_columns)
    fig = draw(x, series, args.width_mm, args.height_mm, args.x_label, args.y_label,
               args.title, args.kind)
    export(fig, args.csv, args.out, args.width_mm, args.dpi)
    plt.close(fig)
    print(f"已输出 {args.out}.png / .pdf / .svg / .json")


if __name__ == "__main__":
    main()
