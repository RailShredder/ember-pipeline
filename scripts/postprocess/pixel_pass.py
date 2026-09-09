"""
pixel_pass.py — AI 原图 → 像素风成品
用法: python pixel_pass.py in.png out.png --size 48 --colors 16 --palette ../style/palette.json
"""
import argparse
import json

from PIL import Image
from rembg import remove


def load_palette(path: str) -> list[tuple[int, int, int]]:
    with open(path, encoding="utf-8") as f:
        hexes = json.load(f)["colors"]
    return [tuple(int(h.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4)) for h in hexes]


def pixel_pass(
    src: Image.Image,
    out_size: int = 48,
    palette: list[tuple[int, int, int]] | None = None,
) -> Image.Image:
    img = remove(src)                                  # 1. 去背景 → RGBA
    bbox = img.getbbox()                               # 2. 裁到内容
    img = img.crop(bbox)
    # 3. 等比缩放进目标框（内边距 8%）
    w, h = img.size
    scale = min(out_size * 0.84 / w, out_size * 0.84 / h)
    img = img.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", (out_size, out_size), (0, 0, 0, 0))
    canvas.paste(img, ((out_size - img.width) // 2, (out_size - img.height) // 2))
    # 4. 量化到固定调色板（一致性关键：全局共用 style/palette.json）
    if palette is not None:
        pal_img = Image.new("P", (1, 1))
        pal_img.putpalette([c for rgb in palette for c in rgb] + [0] * (256 * 3 - len(palette) * 3))
        quant = canvas.convert("RGB").quantize(palette=pal_img, dither=Image.Dither.NONE)
    else:
        quant = canvas.convert("RGB").quantize(colors=16, dither=Image.Dither.NONE)
    canvas = Image.merge("RGBA", (*quant.convert("RGB").split(), canvas.split()[3]))
    return canvas.resize((out_size * 8, out_size * 8), Image.NEAREST)  # 5. 整数倍放大


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--size", type=int, default=48)
    p.add_argument("--palette", default=None, help="style/palette.json 路径，强烈建议使用")
    a = p.parse_args()
    pal = load_palette(a.palette) if a.palette else None
    pixel_pass(Image.open(a.input), a.size, pal).save(a.output)
