#!/usr/bin/env python3
"""Render GitHub palette previews from shared colors (standard library only)."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Display names follow interface roles, not absolute lightness. Existing JSON
# family keys are retained for compatibility; these are presentation labels.
# Names follow perceptual lightness within each variant. The implementation
# keys remain stable even though Morning and Evening reverse their scales.
NAMES = {
    'morning': {
        'core': [('3', 'Horizon'), ('2', 'Inlet'), ('1', 'Deception Pass'), ('0', 'Deep Water')],
        'foreground': [('2', 'Pebble'), ('1', 'Driftwood'), ('0', 'Slate')],
        'background': [('0', 'Shell'), ('1', 'Mist'), ('2', 'Shore')],
    },
    'evening': {
        'core': [('0', 'Horizon'), ('1', 'Inlet'), ('2', 'Deception Pass'), ('3', 'Deep Water')],
        'foreground': [('0', 'Shell'), ('1', 'Mist'), ('2', 'Pebble')],
        'background': [('2', 'Shore'), ('1', 'Driftwood'), ('0', 'Slate')],
    },
}


def render(mode):
    palette = json.loads((ROOT / f'palette/{mode}.json').read_text())
    fg = palette['foreground']['0']
    muted = palette['foreground']['1']
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1008" height="760" '
        'viewBox="0 0 1008 760" role="img" aria-labelledby="title desc">',
        f'<title id="title">Puget Sound {mode.title()} palette</title>',
        '<desc id="desc">Four prominent primary blues, followed by foreground '
        'and background neutrals, and seven smaller accent swatches. '
        'Each swatch is labeled with its name and hex value.</desc>',
        f'<rect width="1008" height="760" fill="{palette["background"]["0"]}"/>',
        f'<g font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif" fill="{fg}">',
    ]

    def text(x, y, value, size=14, color=fg, weight=400, mono=False):
        font = ' font-family="ui-monospace, monospace"' if mono else ''
        parts.append(f'<text x="{x:g}" y="{y:g}" font-size="{size}" '
                     f'font-weight="{weight}" fill="{color}"{font}>{escape(value)}</text>')

    def row(items, x, y, width, height, gap=12):
        sw = (width - gap * (len(items) - 1)) / len(items)
        for i, (name, color) in enumerate(items):
            sx = x + i * (sw + gap)
            parts.append(f'<rect x="{sx:g}" y="{y:g}" width="{sw:g}" '
                         f'height="{height}" fill="{color}"/>')
            text(sx, y + height + 24, name, 16, weight=600)
            text(sx, y + height + 46, color, 13, muted, mono=True)

    text(32, 49, mode.title(), 28, weight=600)
    names = NAMES[mode]
    text(32, 98, 'Core colors', 16, weight=600)
    row([(name, palette['core'][key]) for key, name in names['core']], 32, 118, 944, 174)
    text(32, 390, 'Foreground', 16, weight=600)
    row([(name, palette['foreground'][key]) for key, name in names['foreground']], 32, 410, 456, 72)
    text(520, 390, 'Background', 16, weight=600)
    row([(name, palette['background'][key]) for key, name in names['background']], 520, 410, 456, 72)
    text(32, 589, 'Semantic colors', 16, weight=600)
    row([(c['name'], c['hex']) for c in palette['semantic'].values()], 32, 609, 944, 60)
    parts.extend(['</g>', '</svg>'])
    (ROOT / f'assets/{mode}-palette.svg').write_text('\n'.join(parts) + '\n')


if __name__ == '__main__':
    for variant in ('morning', 'evening'):
        render(variant)
