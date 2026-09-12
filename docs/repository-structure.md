# Repository structure

Keep one repository with a shared palette and self-contained application ports. Use GitHub Markdown plus local SVG assets for the landing page: it renders directly on GitHub without relying on custom CSS or a separate website.

## Target layout

```text
puget-sound/
├── README.md
├── LICENSE
├── PRINCIPLES.md
├── CONTRIBUTING.md
├── palette/
│   ├── morning.json
│   └── evening.json
├── ports/
│   ├── helix/
│   │   ├── README.md
│   │   ├── puget_sound_morning.toml
│   │   └── puget_sound_evening.toml
│   ├── pi/
│   │   ├── README.md
│   │   ├── puget-sound-morning.json
│   │   └── puget-sound-evening.json
│   └── wezterm/
│       ├── README.md
│       └── puget_sound_theme.lua
├── assets/
│   ├── morning-palette.svg
│   ├── evening-palette.svg
│   └── screenshots/
│       ├── helix-morning.png
│       └── helix-evening.png
├── docs/
│   └── repository-structure.md
├── scripts/
│   ├── render-palettes.py
│   └── check-palettes.py
└── .github/
    └── workflows/
        └── validate.yml
```

This structure is now in place locally. The installable theme files live under `ports/`, while `palette/` contains the shared named colors and supporting scales.

## Responsibilities

### Shared palette

`palette/` should become the authoritative source of the seven accents and three supporting scales. Store display names alongside stable semantic keys: for example, `red` has the display name `Madrona`. Keep roles independent of naming so a documentation change does not require rewriting every port.

Use the same schema in both variants. Record application-specific colors separately in their ports, including Pi message backgrounds and WezTerm ANSI adjustments. Do not force those colors to equal core swatches.

### Application ports

Each `ports/<application>/` directory owns:

- Installable files for Morning and Evening.
- A short README with installation, activation, supported versions, and any caveats.
- Application-specific mappings and deliberate deviations from the core palette.

Commit ready-to-use theme files. Consumers should not need a generator or package manager just to install a theme. A new application should usually require one new directory and one entry in the root README.

### Presentation

Keep the root README focused on identity, previews, colors, and links to installation instructions. Move detailed installation instructions into the port READMEs as the collection grows.

Use flat SVG swatches without borders or shadows, matching the existing design principles. Supplement them with real application screenshots using the same sample content in both variants. Label palette previews as palettes, not application screenshots.

A separate HTML site can be added later if an interactive preview becomes useful; it is not necessary for a polished GitHub landing page.

### Validation and maintenance

Add lightweight scripts to:

- Validate shared palette structure and hexadecimal values.
- Check shared colors in each port while explicitly allowing documented overrides.
- Parse theme files with the appropriate JSON, TOML, and Lua tooling.
- Regenerate SVG previews from the shared palette.
- Detect outdated generated assets in CI.

Start with validation rather than a universal theme generator. Generate ports only if maintaining duplicate values becomes a practical burden.

## Suggested migration order

1. Choose a license before publishing; no license is assumed yet.
2. Add paired application screenshots and, when useful, an additional port.
3. Add reproducible preview generation and synchronization checks.
4. Add CI and a contribution guide if the project begins accepting outside contributions.

The naming vocabulary is **Madrona, Copper, Sand, Fern, Sound, Tidepool, Lavender**, supported by **Shore, Driftwood, and Horizon**.
