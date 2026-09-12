#!/usr/bin/env python3
"""Render GitHub palette previews from shared colors (standard library only)."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEFT_MARGIN = 32
SWATCH_GAP = 8
CORE_WIDTH = 629.333
CORE_SWATCH_WIDTH = (CORE_WIDTH - SWATCH_GAP * 3) / 4
CANVAS_WIDTH = LEFT_MARGIN * 2 + CORE_WIDTH
NEUTRAL_WIDTH = CORE_SWATCH_WIDTH * 2 + SWATCH_GAP
NEUTRAL_SECOND_X = LEFT_MARGIN + NEUTRAL_WIDTH + SWATCH_GAP

def render(mode):
    palette = json.loads((ROOT / f'palette/{mode}.json').read_text())
    fg = palette['foreground']['fg-0']['hex']
    muted = palette['foreground']['fg-1']['hex']
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_WIDTH:g}" height="704" '
        f'viewBox="0 0 {CANVAS_WIDTH:g} 704" role="img" aria-labelledby="title desc">',
        f'<title id="title">Puget Sound {mode.title()} palette</title>',
        '<desc id="desc">Four prominent primary blues, followed by foreground '
        'and background neutrals, and seven smaller accent swatches. '
        'Each swatch is labeled with its technical token, evocative name, and hex value.</desc>',
        f'<rect width="{CANVAS_WIDTH:g}" height="704" fill="{palette["background"]["bg-0"]["hex"]}"/>',
        f'<g font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif" fill="{fg}">',
    ]

    def text(x, y, value, size=14, color=fg, weight=400, mono=False, italic=False):
        font = ' font-family="Cascadia Code, Cascadia Mono, SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"' if mono else ''
        style = ' font-style="italic"' if italic else ''
        parts.append(f'<text x="{x:g}" y="{y:g}" font-size="{size}" '
                     f'font-weight="{weight}" fill="{color}"{font}{style}>{escape(value)}</text>')

    def row(items, x, y, width, height, gap=8):
        # Keep the typography unchanged while reducing each swatch's area.
        sw = (width - gap * (len(items) - 1)) / len(items)
        sh = height * (2 / 3)
        for i, (token, name, color) in enumerate(items):
            sx = x + i * (sw + gap)
            parts.append(f'<rect x="{sx:g}" y="{y:g}" width="{sw:g}" '
                         f'height="{sh:g}" fill="{color}"/>')
            text(sx, y + sh + 24, token, 16, weight=600)
            text(sx, y + sh + 44, name, 13, muted, italic=True)
            text(sx, y + sh + 64, color, 13, muted, mono=True)

    text(32, 49, mode.title(), 28, weight=600)
    text(32, 98, 'Core colors', 16, weight=600)
    row([(token, color['name'], color['hex']) for token, color in palette['core'].items()], LEFT_MARGIN, 118, CORE_WIDTH, 174)
    text(LEFT_MARGIN, 362, 'Background', 16, weight=600)
    row([(token, color['name'], color['hex']) for token, color in palette['background'].items()], LEFT_MARGIN, 382, NEUTRAL_WIDTH, 72)
    text(NEUTRAL_SECOND_X, 362, 'Foreground', 16, weight=600)
    row([(token, color['name'], color['hex']) for token, color in reversed(list(palette['foreground'].items()))], NEUTRAL_SECOND_X, 382, NEUTRAL_WIDTH, 72)
    text(LEFT_MARGIN, 559, 'Semantic colors', 16, weight=600)
    row([(token, color['name'], color['hex']) for token, color in palette['semantic'].items()], LEFT_MARGIN, 579, CORE_WIDTH, 60)
    parts.extend(['</g>', '</svg>'])
    (ROOT / f'assets/{mode}-palette.svg').write_text('\n'.join(parts) + '\n')


if __name__ == '__main__':
    for variant in ('morning', 'evening'):
        render(variant)
