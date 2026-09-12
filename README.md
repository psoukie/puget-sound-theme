<div align="center">

# Puget Sound

**A coastal palette for the tools you live in.**

Cool water, weathered wood, and a little shoreline warmth.<br>
Two expressions of the same colors: **Morning** and **Evening**.

[The palette](#the-palette) · [Applications](#applications) · [Design](#design)

</div>

<br>

![Puget Sound Morning: cool daylight surfaces with seven muted coastal accents](assets/morning-palette.svg)

![Puget Sound Evening: deep blue-gray surfaces with seven softened coastal accents](assets/evening-palette.svg)

## A familiar place, in different light

Puget Sound is a personal theme collection for **Helix, Pi, and WezTerm**. It brings a consistent visual language to an editor, a coding assistant, and a terminal—without requiring each application to use color in exactly the same way.

**Morning** pairs cool, near-white surfaces with grounded accents. **Evening** settles into blue-gray backgrounds, lighter foregrounds, and an atmospheric blue scale with a hint of indigo.

Neither is a mechanical inversion of the other. They are companion palettes, tuned to feel related in different light.

## The palette

Seven named accents form the shared vocabulary. Each name belongs to both its Morning and Evening expression.

| Color | Morning | Evening |
| :--- | :--- | :--- |
| **Madrona** · red | `#AA534E` | `#E98C84` |
| **Copper** · orange | `#AA7223` | `#D79C52` |
| **Sand** · yellow | `#B7A36F` | `#D1BD88` |
| **Fern** · green | `#708F6D` | `#90B18E` |
| **Sound** · blue | `#5278A7` | `#8BB2E4` |
| **Tidepool** · teal | `#5592A1` | `#72B1BF` |
| **Lavender** · purple | `#7E76A6` | `#AAA3D6` |

Three supporting families give the accents somewhere to belong:

- **Shore** — three levels of neutral background surfaces.
- **Driftwood** — primary, secondary, and tertiary foregrounds.
- **Horizon** — four atmospheric blues for interface layers, selections, and markup.

Sound is the semantic blue; Horizon is a separate interface scale. Terminal ANSI colors include application-specific adjustments and derived bright variants rather than simply duplicating every core swatch.

<details>
<summary><strong>Supporting palette · all values</strong></summary>

<br>

| Color | Implementation token | Morning | Evening |
| :--- | :--- | :--- | :--- |
| Shore 0 | `bg-0` | `#F9FCFF` | `#18242F` |
| Shore 1 | `bg-1` | `#E0EAEF` | `#2A3A46` |
| Shore 2 | `bg-2` | `#B9C9D0` | `#4E5C68` |
| Driftwood Primary | `fg-primary` | `#3E515E` | `#C1CCD3` |
| Driftwood Secondary | `fg-secondary` | `#5A6C74` | `#9FADB3` |
| Driftwood Tertiary | `fg-tertiary` | `#6A7B84` | `#87959C` |
| Horizon 0 | `blue-0` | `#375378` | `#B2BFDB` |
| Horizon 1 | `blue-1` | `#7298CA` | `#8194BA` |
| Horizon 2 | `blue-2` | `#C8DDFC` | `#496594` |
| Horizon 3 | `blue-3` | `#E4EFFF` | `#31466C` |

Token spelling varies by application; the names above describe the shared palette. Numbered steps describe interface roles, not a universal light-to-dark ordering.

</details>

## Applications

Both variants are included for each application. The theme files are plain configuration files; no build step is required to use them.

| Application | Theme files |
| :--- | :--- |
| **Helix** | [Port guide](ports/helix/README.md) · [Morning](ports/helix/puget_sound_morning.toml) · [Evening](ports/helix/puget_sound_evening.toml) |
| **Pi** | [Port guide](ports/pi/README.md) · [Morning](ports/pi/puget-sound-morning.json) · [Evening](ports/pi/puget-sound-evening.json) |
| **WezTerm** | [Port guide](ports/wezterm/README.md) · [Both schemes](ports/wezterm/puget_sound_theme.lua) |

Installation and application-specific details live in each [port guide](#applications).
## Design

- **Related, not inverted.** Morning and Evening preserve the identity of the accent colors while adjusting their perceptual lightness.
- **Atmosphere belongs in the interface.** Horizon receives its own Evening treatment; syntax accents retain their semantic hues.
- **Adapt to the application.** Terminal brights and tool-specific surfaces serve their local roles while staying within the palette’s character.

The color relationships and terminal derivations are documented in [the theme principles](PRINCIPLES.md).

## Growing the collection

This is a personal collection, with the three applications I use as its starting point. Additional ports can build on the same named palette and Morning/Evening relationship.

See [the proposed repository structure](docs/repository-structure.md) for an approach to adding applications, shared palette data, previews, and validation without mixing application-specific details into the core colors.
