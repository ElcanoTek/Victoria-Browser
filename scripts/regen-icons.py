#!/usr/bin/env python3
"""Regenerate the Victoria icon pyramid from the master SVG.

Reads the canonical Victoria ship SVG and writes a deep-purple branded
logo + every PNG size Chromium expects. Silhouette path data is embedded
so the script is self-contained and stays runnable even if the flag
design-system repo is not checked out alongside.

Requires: CairoSVG, Pillow.
"""

from __future__ import annotations

import io
import os
from pathlib import Path

import cairosvg
from PIL import Image

REPO = Path(__file__).resolve().parent.parent
AGENT_ASSETS = REPO / "packages/browseros-agent/apps/agent/assets"
AGENT_PUBLIC_ICON = REPO / "packages/browseros-agent/apps/agent/public/icon"
BROWSEROS_ICONS = REPO / "packages/browseros/resources/icons"

SHIP_PATH = (
    "M264.7 36v21.76c5.9-1.27 11.9-2.91 18-4.99V36zm26.7 32.79C257.1 81.22 226 80.48 195 79.88c28.7 15.85 61.1 23.32 92.2 16.58 2.6-9.36 6-18.4 4.2-27.67zm-164.1 10.8C140.5 136.8 152.2 197.3 137.9 285c12.8 17.6 24 35.7 34 53.7l5.1 9.3c73.7-19.3 135.4-22.7 186.9-12.3 2.4-6.5 4.7-13.3 6.7-20.1-53.5-91.8-136.8-169.4-243.3-236.01zm155.4 36.01c-6 .9-12 1.4-18 1.4v42.6c6.1 5.5 12.1 11.1 18 16.8zM56.73 192v10.3c6.24 4.6 12.24 9.3 18 14.2V192zm351.97 4v17.9c6.2 2.5 12.2 5.5 18 8.9V196zm-386.01 5.1c5.77 19.7 10.88 39.8 12.08 60.4 1.21 20.6-1.8 41.8-11.79 62.8 41.42-12.1 84.42-6.5 121.82 3.7-28.5-46.9-66.02-92.4-122.11-126.9zm216.81 1c1.7 9.5 2.1 21.4 1.3 33.8 1.2 0 2.4-.1 3.6-.1 10.8-.2 20.9.4 29.2 2l-3.4 17.6c-7.7-1.4-18.9-1.8-31.3-1.1-2.1 14.1-5.7 27.6-10.6 38.2l-16.4-7.6c3.3-6.9 5.9-17.4 7.8-28.7-9.3 1.3-18.6 3.1-27.1 5.5l-4.8-17.4c11-3.1 22.7-5.3 34.2-6.8 1.1-12.6 1.1-24.6-.3-32.2zm155.3 26c4.8 20.2 3.7 43.2-.6 66-4.1 21.8-11.1 43.6-19.3 62.5 17.1-4.2 37.7-8.3 58.1-10.7 20.4-2.3 40.1-3.4 56.3.3-18.3-68.6-53.7-105.2-94.5-118.1zM81.64 254.5c1.3 7.3 1.7 15.1 1.52 22.9 5.62.7 11.51 1.9 18.04 3.5l-4.32 17.4c-5.68-1.4-10.54-2.4-15.06-3.1-.78 6.5-1.8 12.5-2.85 17.7l-17.64-3.6c.89-4.4 1.72-9.5 2.39-15-4.54.3-9.38.8-15 1.6l-2.59-17.8c6.81-1 12.95-1.6 18.92-1.7.15-6.7-.15-13.2-1.13-18.7zm341.46 23.6 18 1.2c-.4 5.9-.9 12.1-1.5 18.4 6.7.3 13.5 1.1 20.5 2.9l-4.2 17.4c-6.3-1.5-12.4-2.2-18.6-2.4-1.2 7.2-2.7 14.3-4.7 21l-17.2-5.2c1.4-4.5 2.5-9.4 3.4-14.6-5.4.7-10.9 1.7-16.5 2.9l-3.6-17.6c7.4-1.5 14.9-2.9 22.7-3.7.7-6.8 1.2-13.7 1.7-20.3zM56.73 336.2v13.7c6.04.6 12.04 1.3 18 2v-16.5c-6.3.1-12.76.3-18 .8zm69.07 5.5c-1.4 5.5-2.9 11-4.5 16.6 4.5.7 8.9 1.4 13.2 2.1 9.5-3 18.7-5.9 27.8-8.4-12.6-4.1-25.5-7.8-36.5-10.3zm156.9 6.7c-5.9.4-11.9.9-18 1.5v76.7c6.1-.2 12.1-.6 18-1zm144 16.5s-18.3 3.6-18 3.5v29c6.1-2.2 12.1-4.5 18-6.8zm-392.5 1.4c24.11 40.8 50.62 82.6 55.75 124.7H414.3c2.8-2.5 10.3-9.2 20.5-19.4 12.4-12.4 26.6-28.3 33-40 4.9-8.7 9.3-20.3 11.8-31.1 1.2-5.2 1.8-10.2 2.1-14.7C419 416.1 340.9 445 248.8 445h-5.7l-23.6-49.2c-10.3-2.5-97.1-23-185.3-29.5zm16.85 66.9-7.36 9.7 16 51.9 12.32-2.2c-2.51-18.7-10.49-38.7-20.96-59.4z"
)


def product_logo_svg() -> str:
    """Deep-purple rounded-square tile with the Victoria ship in Elcano accent."""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#241b31"/>
      <stop offset="1" stop-color="#1a0b1e"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="1024" height="1024" rx="180" ry="180" fill="url(#bg)"/>
  <g transform="translate(152 152) scale(1.40625)">
    <path fill="#9da7ef" d="{SHIP_PATH}"/>
  </g>
</svg>
"""


def mono_svg(foreground: str = "#ffffff") -> str:
    """Single-color silhouette used for the macOS menubar / template icon."""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <path fill="{foreground}" d="{SHIP_PATH}"/>
</svg>
"""


def wordmark_svg(white: bool = False) -> str:
    """Compact 'Victoria' wordmark alongside the ship silhouette."""
    text_color = "#ffffff" if white else "#1a0b1e"
    ship_color = "#ffffff" if white else "#7272ab"
    return f"""<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 128" width="512" height="128">
  <g transform="translate(0 0) scale(0.25)">
    <path fill="{ship_color}" d="{SHIP_PATH}"/>
  </g>
  <text x="150" y="85" font-family="Georgia, 'Times New Roman', serif" font-size="72" font-weight="600" fill="{text_color}">Victoria</text>
</svg>
"""


def svg_to_png(svg: str, out_path: Path, size: int) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        output_width=size,
        output_height=size,
        write_to=str(out_path),
    )


def svg_to_png_wordmark(svg: str, out_path: Path, height: int) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    width = height * 4
    cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        output_width=width,
        output_height=height,
        write_to=str(out_path),
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def png_to_ico(src: Path, dst: Path, sizes: list[int]) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    img = Image.open(src).convert("RGBA")
    img.save(dst, format="ICO", sizes=[(s, s) for s in sizes])


def xpm_from_png(src: Path, dst: Path) -> None:
    """Write an X Pixmap from a PNG. Pillow lacks a writer, so we emit it by hand.

    XPM is a C-source image format. We produce a 2-color palette (on/off)
    based on alpha: this keeps the window icon legible at ~22-32px on Linux
    WMs that read the XPM.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    pixels = img.load()
    on, off = "# ", "  "
    lines = [
        "/* XPM */",
        f'static char *product_logo_32[] = {{',
        f'"{w} {h} 2 1",',
        f'"{on[0]}\tc #7272AB",',
        f'"{off[0]}\tc None",',
    ]
    for y in range(h):
        row = "".join(on[0] if pixels[x, y][3] > 128 else off[0] for x in range(w))
        comma = "," if y < h - 1 else ""
        lines.append(f'"{row}"{comma}')
    lines.append("};")
    dst.write_text("\n".join(lines))


def regen() -> None:
    product = product_logo_svg()
    mono_white = mono_svg("#ffffff")

    write_text(AGENT_ASSETS / "product_logo.svg", product)
    write_text(BROWSEROS_ICONS / "product_logo.svg", product)

    # Main pyramid
    main_sizes = [16, 22, 24, 32, 48, 64, 128, 192, 256, 1024]
    for s in main_sizes:
        svg_to_png(product, BROWSEROS_ICONS / f"product_logo_{s}.png", s)
    svg_to_png(product, BROWSEROS_ICONS / "product_logo.png", 128)

    # 22 mono (macOS template menu bar icon)
    svg_to_png(mono_white, BROWSEROS_ICONS / "product_logo_22_mono.png", 22)

    # 1x / 2x resource variants
    for base, size in [("default_100_percent", 16), ("default_100_percent", 32),
                       ("default_200_percent", 16), ("default_200_percent", 32)]:
        scale = 2 if "200" in base else 1
        svg_to_png(product, BROWSEROS_ICONS / base / f"product_logo_{size}.png", size * scale)

    # Wordmark variants (logo + "Victoria" text)
    wm = wordmark_svg(white=False)
    wm_white = wordmark_svg(white=True)
    svg_to_png_wordmark(wm, BROWSEROS_ICONS / "product_logo_name_22.png", 22)
    svg_to_png_wordmark(wm, BROWSEROS_ICONS / "product_logo_name_22_2x.png", 44)
    svg_to_png_wordmark(wm_white, BROWSEROS_ICONS / "product_logo_name_22_white.png", 22)
    svg_to_png_wordmark(wm_white, BROWSEROS_ICONS / "product_logo_name_22_white_2x.png", 44)
    svg_to_png_wordmark(wm, BROWSEROS_ICONS / "default_100_percent/product_logo_name_22.png", 22)
    svg_to_png_wordmark(wm_white, BROWSEROS_ICONS / "default_100_percent/product_logo_name_22_white.png", 22)
    svg_to_png_wordmark(wm, BROWSEROS_ICONS / "default_200_percent/product_logo_name_22.png", 44)
    svg_to_png_wordmark(wm_white, BROWSEROS_ICONS / "default_200_percent/product_logo_name_22_white.png", 44)

    # Linux
    linux_sizes = [24, 48, 64, 128, 256]
    for s in linux_sizes:
        svg_to_png(product, BROWSEROS_ICONS / f"linux/product_logo_{s}.png", s)
    svg_to_png(product, BROWSEROS_ICONS / "linux/product_logo_32.png", 32)
    xpm_from_png(BROWSEROS_ICONS / "linux/product_logo_32.png", BROWSEROS_ICONS / "linux/product_logo_32.xpm")

    # ChromeOS
    svg_to_png(product, BROWSEROS_ICONS / "chromeos/chrome_app_icon_192.png", 192)
    svg_to_png(product, BROWSEROS_ICONS / "chromeos/chrome_app_icon_32.png", 32)
    svg_to_png(product, BROWSEROS_ICONS / "chromeos/webstore_app_icon_128.png", 128)
    svg_to_png(product, BROWSEROS_ICONS / "chromeos/webstore_app_icon_16.png", 16)

    # Windows .ico (multi-resolution)
    tmp_dir = BROWSEROS_ICONS / "_tmp"
    tmp_dir.mkdir(exist_ok=True)
    for s in [16, 24, 32, 48, 64, 128, 256]:
        svg_to_png(product, tmp_dir / f"{s}.png", s)
    png_to_ico(tmp_dir / "256.png", BROWSEROS_ICONS / "win/chromium.ico",
               [16, 24, 32, 48, 64, 128, 256])
    png_to_ico(tmp_dir / "256.png", BROWSEROS_ICONS / "win/chromium_doc.ico",
               [16, 24, 32, 48, 64, 128, 256])
    png_to_ico(tmp_dir / "256.png", BROWSEROS_ICONS / "win/chromium_pdf.ico",
               [16, 24, 32, 48, 64, 128, 256])
    png_to_ico(tmp_dir / "256.png", BROWSEROS_ICONS / "win/app_list.ico",
               [16, 24, 32, 48, 64, 128, 256])
    for f in tmp_dir.iterdir():
        f.unlink()
    tmp_dir.rmdir()

    # Root logo.png in resources
    svg_to_png(product, REPO / "packages/browseros/resources/logo.png", 512)

    # Agent extension public icons (shown in the Chrome toolbar)
    for s in [16, 32, 48, 96, 128]:
        svg_to_png(product, AGENT_PUBLIC_ICON / f"{s}.png", s)

    # macOS Assets.xcassets — regenerate the PNG members; .icns and Assets.car
    # are built from these at packaging time via `iconutil` / `actool` on macOS.
    mac_xc = BROWSEROS_ICONS / "mac/Assets.xcassets"
    for s in [16, 32, 64, 128, 256, 512, 1024]:
        svg_to_png(product, mac_xc / f"AppIcon.appiconset/appicon_{s}.png", s)
    svg_to_png(product, mac_xc / "Icon.iconset/icon_256x256.png", 256)
    svg_to_png(product, mac_xc / "Icon.iconset/icon_256x256@2x.png", 512)

    print("Icon pyramid regenerated.")


if __name__ == "__main__":
    regen()
