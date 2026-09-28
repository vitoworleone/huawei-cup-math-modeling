# 数学建模论文绘图模板与 Codex 技能

这套文件从本次 D 题已确认的绘图规范、四题定稿图集与成品 LaTeX 中提取可复用部分：先确定图的论证作用与数据来源，再选择图型，按论文最终插入宽度设置字体和间距，导出后分别检查数据、PDF/SVG、视觉效果。`examples/` 收录七张成品论文实际引用的图，作为排版与选图实例；模板数据仍为虚构数值。没有收录完整论文图集或商业参考资料。

| 文件 | 用途 |
|---|---|
| `SKILL.md` | Codex 使用的绘图工作方式与边界 |
| `references/figure-style-guide.md` | 这次确认的二维 v1.5、三维 v1.6 规则及适用边界 |
| `references/source-priority.md` | 全工作区相关规范的盘点、现行顺序和章节例外 |
| `references/ai-audit-and-iteration.md` | 根据实际绘图 trace 提炼的逐图审计、局部修改与闭环流程 |
| `examples/README.md` | 七张成品论文实图、纸面宽度、图型分析及来源 |
| `examples/*.pdf`、`examples/*.png` | 成品正文实际引用的 PDF 与便于在 GitHub 浏览的预览 |
| `assets/figure-plan-template.md` | 选图、图号、数据源、论文位置和核验记录 |
| `assets/audit-trace-template.md` | 可复制的问题清单与逐轮 trace |
| `assets/caption-template.md` | 图内、图注和结果表的信息分工 |
| `assets/plot_template.py` | CSV 驱动的二维 Matplotlib 起点，输出 PNG/PDF/SVG/记录 JSON |
| `assets/demo.csv`、`assets/demo-preview.png` | 无论文结果的演示数据及预览 |

## 运行绘图模板

安装 Matplotlib，并在系统中合法安装 Microsoft YaHei 常规及粗体、Times New Roman。模板不打包字体。当前电脑可用以下命令生成示例：

```sh
python assets/plot_template.py assets/demo.csv \
  --y-columns 基准方案 比较方案 \
  --x-label '参数 / —' --y-label '指标 / —' \
  --out example/figure
```

默认成稿宽度为 120 mm、PNG 为 320 dpi。若字体文件不在默认的 macOS 路径，传入 `--cjk-font` 和 `--cjk-bold-font`。`plot_template.py` 的 `draw()` 演示连续曲线；遇到热图、地图、甘特图或三维图，应保留数据溯源、字体和导出方式，按实际证据重新设计主体图形。示例 CSV 是虚构数值；`examples/` 则是本次 D 题真实成品图，不能当作别的论文的数据。

## 使用技能

本目录同时是一个 Codex skill，`SKILL.md` 可作为入口。当前工作区可通过 Codex skills 目录中的链接调用；复制到其他环境时，将整个目录放进该环境的 Codex skills 目录即可。技能会按需读取 `references/` 和 `assets/`。

## 来源与发布状态

规则来源于本工作区的三份主规范、章节专项修订，以及问题一至四 `定稿图集` 的计划、图注、代码、核验和交接记录，详见[盘点](references/source-priority.md)。AI 审计流程另从实际绘图过程的 `PLAN`、`REVIEW`、`HANDOFF`、逐图问题和三格式核验 trace 提炼。七张实图来自 `draft/D题/figures`，按该工程最终 LaTeX 正文引用核对，哈希记录在 `examples/manifest.json`。其余本题特定的图和计算数据仍在原工程。这个目录目前只在本地 `GitHub` 文件夹中，尚未上传远端。
