"""Compose the nine unchanged paper figures into a README preview."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent
ITEMS = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
OUTPUT = ROOT / "figure-gallery.png"

WIDTH = 1840
MARGIN = 24
GAP = 18
HERO_HEIGHT = 620
ROW_HEIGHT = 360
HEIGHT = MARGIN * 2 + HERO_HEIGHT + ROW_HEIGHT * 2 + GAP * 2


def card(canvas: Image.Image, filename: str, box: tuple[int, int, int, int]) -> None:
    x, y, width, height = box
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(
        (x + 3, y + 5, x + width + 3, y + height + 5),
        radius=16,
        fill="#dce3ea",
    )
    draw.rounded_rectangle(
        (x, y, x + width, y + height),
        radius=16,
        fill="#ffffff",
        outline="#d5dde6",
        width=2,
    )
    source = ROOT / filename
    with Image.open(source) as original:
        image = original.convert("RGB")
    image.thumbnail((width - 28, height - 28), Image.Resampling.LANCZOS)
    canvas.paste(
        image,
        (x + (width - image.width) // 2, y + (height - image.height) // 2),
    )


def main() -> None:
    if len(ITEMS) != 9:
        raise ValueError("The gallery requires exactly nine figures")
    for item in ITEMS:
        path = ROOT / item["file"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            raise ValueError(f"Source figure changed: {path}")

    canvas = Image.new("RGB", (WIDTH, HEIGHT), "#f1f4f8")
    left_width = 720
    right_x = MARGIN + left_width + GAP
    right_width = WIDTH - MARGIN - right_x
    right_top_height = (HERO_HEIGHT - GAP) // 2
    positions = [
        (MARGIN, MARGIN, left_width, HERO_HEIGHT),
        (right_x, MARGIN, right_width, right_top_height),
        (right_x, MARGIN + right_top_height + GAP, right_width, HERO_HEIGHT - right_top_height - GAP),
    ]
    y = MARGIN + HERO_HEIGHT + GAP
    tile_width = (WIDTH - MARGIN * 2 - GAP * 2) // 3
    for row in range(2):
        for col in range(3):
            x = MARGIN + col * (tile_width + GAP)
            width = tile_width if col < 2 else WIDTH - MARGIN - x
            positions.append((x, y + row * (ROW_HEIGHT + GAP), width, ROW_HEIGHT))

    for item, box in zip(ITEMS, positions, strict=True):
        card(canvas, item["file"], box)
    canvas.save(OUTPUT, optimize=True)
    print(f"Wrote {OUTPUT}: {canvas.width}×{canvas.height}")


if __name__ == "__main__":
    main()
