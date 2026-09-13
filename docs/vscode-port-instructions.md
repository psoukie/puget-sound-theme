# Puget Sound for VS Code: design instructions for an AI

## Assignment and scope

Create **Morning and Evening customizations of VS Code’s built-in color themes**, not an extension. Use the customization approach described in [Customize a color theme](https://code.visualstudio.com/docs/configure/themes#_customize-a-color-theme). Start with **Default Light Modern** for Morning and **Default Dark Modern** for Evening (verify the names in the target installation). Treat these as coverage fallbacks, not as the desired color identity.

The eventual deliverable should be two clearly separated, theme-scoped sets of settings overrides, with a short explanation of any deliberate palette departures. Do not create extension packaging, change fonts or layout, or require an icon theme. Research configuration keys and token scopes as needed; this document specifies the visual result rather than implementation mechanics.

## Read these sources first

Paths below are relative to the repository root:

- `README.md`: the theme’s identity and named colors.
- `PRINCIPLES.md`: the relationship between Morning and Evening.
- `palette/morning.json` and `palette/evening.json`: authoritative color values, including terminal-specific colors.
- `ports/helix/puget_sound_morning.toml` and `ports/helix/puget_sound_evening.toml`: the closest existing reference for syntax and editor roles.
- `assets/morning-palette.svg` and `assets/evening-palette.svg`: palette previews.

Preserve the existing palette. The recommendations below for VS Code-specific surfaces are design proposals, not claims that a VS Code port already exists. Translate roles rather than copying every Helix decision literally.

## Visual intent

**Cool water, weathered wood, and a little shoreline warmth.** Blues establish the atmosphere; cool neutrals support reading; semantic accents clarify structure without turning code into a rainbow.

- **Morning:** airy, near-white blue-tinted paper, slate text, pale blue interaction surfaces. Avoid warm cream backgrounds, pure black text, and electric blue accents.
- **Evening:** deep blue-gray surroundings, soft shell-colored text, and subdued indigo-blue layers. Avoid neutral charcoal, pure white text, neon accents, and large saturated blue panels.
- These are companion palettes, **not inversions**. Use the supplied values independently. Do not derive Evening by darkening Morning or applying a uniform hue shift.
- The editor should remain the visual center. Sidebars and controls should feel related, not compete with the code.
- Prefer flat surfaces, quiet separators, and restrained emphasis over heavy outlines or conspicuous shadows.

## Palette reference

Use these exact base colors. If this table becomes stale, prefer the shared palette JSON files.

| Role | Morning | Evening |
|---|---|---|
| `bg-0` — main surface | `#F9FCFF` | `#18242F` |
| `bg-1` — secondary surface | `#E0EAEF` | `#2A3A46` |
| `bg-2` — strongest neutral layer/stroke | `#B9C9D0` | `#4E5C68` |
| `fg-0` — primary text | `#3E515E` | `#C1CCD3` |
| `fg-1` — secondary text | `#5A6C74` | `#9FADB3` |
| `fg-2` — tertiary text | `#6A7B84` | `#87959C` |
| `blue-0` — strong blue foreground/heading | `#375378` | `#B2BFDB` |
| `blue-1` — interface accent | `#7298CA` | `#8194BA` |
| `blue-2` — stronger blue highlight | `#C8DDFC` | `#496594` |
| `blue-3` — quieter blue layer | `#E4EFFF` | `#31466C` |
| red — Madrona | `#AA534E` | `#E98C84` |
| orange — Copper | `#AA7223` | `#D79C52` |
| yellow — Sand | `#B7A36F` | `#D1BD88` |
| green — Hemlock | `#708F6D` | `#90B18E` |
| blue — Sound | `#5278A7` | `#8BB2E4` |
| teal — Tidepool | `#5592A1` | `#72B1BF` |
| purple — Lavender | `#7E76A6` | `#AAA3D6` |

**Keep the two blue families distinct.** `blue-0` through `blue-3` are atmospheric interface and markup colors. Semantic `blue` is for functions, links, and information. Do not use the layered blues as code-syntax foregrounds. Their numbering reverses physical lightness between variants but preserves their intended roles.

## Workbench and editor hierarchy

Start with this allocation, then refine by inspecting a real workspace:

| Area | Intended treatment |
|---|---|
| Editor, gutter, terminal | `bg-0`, with `fg-0` text; keep the gutter visually attached to the editor |
| Sidebar and panel chrome | `blue-3`, with secondary labels in `fg-1`; use the atmospheric blue family to separate these areas from the editor |
| Activity bar and section headers | `blue-2` for a more definite toolbar/navigation layer; use `blue-0`/`blue-3` for contrasting labels as appropriate |
| Active tab | `bg-0`, `fg-0` label, a restrained blue indicator |
| Inactive tab strip | `blue-3`, keeping tabs related to the sidebar/panel without merging everything into `bg-1` |
| Title/status bars | `blue-3` or a quiet neutral according to density; use blue active indicators rather than large default saturated bars |
| Inputs | `bg-0` or `bg-1` relative to their container; `fg-0` text and quiet neutral boundaries |
| Hover, completion, quick picker | Try `blue-3` with `fg-0`; use `bg-1` if a large overlay feels excessively blue |
| Separators, guides, scrollbars | `bg-2`, subdued where necessary; these should not resemble focus indicators |
| Focus rings, active controls | `blue-1` as a starting accent, or semantic `blue` where stronger definition is needed |

Do not use `bg-2` as a broad default panel background: it is the strongest neutral step, not a fourth major workspace area. The core blue layers are intentionally available for major chrome surfaces; use them selectively and avoid making every control blue. Avoid inventing extra opaque surface colors unless a demonstrated readability problem requires one.

Helix has a colored, mode-aware status line. VS Code does not need a literal copy: a large colored status bar can dominate its denser workbench. Prefer a quiet bar with localized state accents. Keep debugging, remote, and workspace state recognizable without reverting to unrelated bright orange or purple strips.

Use `fg-0` for actionable labels and `fg-1` for supporting information. Reserve `fg-2` for tertiary content, not every inactive control. Disabled items may be quieter, but ordinary secondary text must remain readable.

For primary buttons, test a blue treatment with an explicitly chosen contrasting label. Do not assume white text works on Morning `blue-1`, or that the same foreground/background pairing works in both variants. A `blue-2` fill with `blue-0` text is another starting point, subject to contrast checks.

## Selection, focus, and navigation

- Primary editor selection: start with `blue-2`; secondary or inactive selection: `blue-3` or a quieter blend of the primary selection.
- Current line: a restrained `bg-1` treatment. It should be less prominent than selected text; reduce its strength if the full-width band is distracting.
- Cursor: `blue-0` for a clear focal point. Do not emulate Helix’s mode colors unless a separate modal-editing customization is requested.
- Selected list rows: `blue-2`, with `blue-0` or `fg-0` text after checking contrast. Hover should be weaker than selection; keyboard focus should remain independently visible.
- Matching brackets and occurrences: quiet blue highlighting or a fine outline. Avoid default rainbow bracket colors; use a restrained palette if distinct nesting colors are retained.
- Search matches: use blue-family highlights for ordinary matches. Distinguish the current match with a stronger outline or a restrained orange/yellow tint, not an opaque amber block.
- Line numbers and indent guides: low-emphasis neutrals; active line number in semantic `blue`. Prefer `fg-2` for readable line numbers if Helix’s `bg-2` treatment is too faint in VS Code.
- Inlay hints: `fg-1` on a quiet neutral surface. Ghost text should be visibly secondary but not illegible.

A selection overlay must not destroy syntax readability. Where transparency is required or useful, derive it from an existing palette color and inspect the **composited result** on both editor and current-line backgrounds. Do not assume identical alpha values create equivalent visual weight in Morning and Evening.

## Syntax: preserve the Helix language

Keep identifiers mostly neutral. Let color identify meaningful classes rather than assigning every token a distinct accent.

| Syntax role | Treatment |
|---|---|
| Ordinary variables, parameters, properties/members | `fg-0` |
| Operators | `fg-0` |
| Punctuation, delimiters, brackets | `fg-1` |
| Comments | `fg-2`, optionally italic; do not add further dimming by default |
| Keywords, control flow, storage modifiers | purple |
| Functions and methods, including built-ins | semantic blue |
| Types, classes, interfaces, namespaces, constructors | teal |
| Constants, booleans, enum members | teal |
| Numbers | green |
| Strings | green |
| Character literals and escape sequences | teal |
| Regular expressions | yellow, subject to readability adjustment |
| Special strings and macros | orange |
| Tags | purple |
| Attributes, annotations, labels, directives | purple, with sparse optional italics |
| URLs | semantic blue, optionally underlined |

Do not let semantic highlighting reintroduce the base theme’s unrelated colors. A symbol should retain the same conceptual role whether colored by a grammar or a language server. Avoid extra colors for declaration versus reference, static members, or readonly variables unless the distinction genuinely helps; readonly alone should not turn all properties teal.

Use italics sparingly, chiefly for comments and annotations. Do not make all keywords italic or functions bold. Documentation prose should remain comfortably readable.

### Markup

Use `blue-0` for the strongest headings. Descend through primary and secondary foregrounds rather than introducing a rainbow of heading colors. Preserve bold, italic, and strikethrough as meaningful formatting. Links use semantic blue, quotes use `fg-1`, and inline/fenced code may use a quiet `bg-1` surface where supported. Keep code content’s language syntax consistent with the editor.

## Diagnostics, source control, and terminal

- **Errors/deletions:** red.
- **Warnings:** orange for readable labels and icons; yellow may serve as a softer underline or background tint.
- **Information:** semantic blue.
- **Hints/additions:** green.
- **Modified lines:** yellow, following Helix; use orange for small indicators if yellow is too weak.
- **Moved content:** semantic blue where the UI distinguishes it.

Favor colored glyphs, underlines, and low-opacity diff fills over large opaque semantic surfaces. Preserve legible code inside added/deleted regions, including inline changes and selections. Do not rely on hue alone: retain icons, squiggles, borders, and textual state cues.

For the integrated terminal, copy each variant’s `terminal.ansi` and `terminal.brights` groups from the palette JSON. Those colors include intentional terminal-specific adjustments; do not substitute the syntax palette or generate new brights. Start with `bg-0` and `fg-0` for the terminal surface and text. Terminal brights are not extra workbench or syntax accents.

## Contrast and permissible adaptations

Palette fidelity is the starting point, not proof of accessibility. In particular, Morning’s green, teal, and yellow can be too soft for small text, and foregrounds may lose contrast over blue selections.

Check actual pairs, aiming for at least 4.5:1 for ordinary text and 3:1 for essential non-text indicators where applicable. Do not describe the finished customization as accessible without validating it.

If a role fails:

1. Try a more suitable existing foreground or a quieter background/overlay.
2. For secondary prose, promote to `fg-1` or `fg-0` rather than adding saturation.
3. If a syntax hue must remain identifiable, derive a local text-grade variant by adjusting perceptual lightness, preserving hue and approximately preserving chroma. Use OKLCH rather than arbitrary RGB darkening/lightening.
4. Record the exact derived value, its role, and why it was necessary. Keep the shared palette unchanged.

Do not globally brighten Evening or darken Morning to solve an isolated problem. Never apply Evening’s atmospheric indigo treatment to the warm semantic colors.

## Suggested design pass and acceptance criteria

1. Establish the main surfaces and neutral text first. Inspect the workspace with plain text before adding syntax accents.
2. Add blue interaction states and navigation. Check active/inactive tabs, focused/unfocused selections, picker rows, and inputs.
3. Apply the syntax role map, then inspect representative TypeScript/JavaScript, Python, Rust or another typed language, JSON, HTML/CSS, and Markdown. Check semantic highlighting as well as grammar-only coloring.
4. Add diagnostics, source-control states, diff views, and terminal colors.
5. Audit inherited defaults on welcome/settings screens, notifications, badges, links, buttons, breadcrumbs, minimap, and overview ruler. Override visible off-palette colors where they undermine the design; do not enumerate obscure keys merely for completeness.
6. Compare Morning and Evening in the same workspace, including comments, long strings, nested code, diagnostics, selected code, hover cards, and terminal ANSI samples.

The result is successful when:

- Both variants are unmistakably Puget Sound, not stock VS Code with a changed editor background.
- Blue carries the atmosphere; warm accents remain occasional and meaningful.
- Code remains the focus, and unselected identifiers remain mostly neutral.
- Hover, selection, focus, search, diagnostics, and diff states remain distinguishable without obscuring content.
- Morning feels airy and Evening feels sheltered; neither feels washed out or harsh.
- Any departures from the supplied palette are small, role-specific, and documented.

Deliver the customizations and a short design note. State what was actually inspected or contrast-tested, and identify remaining uncertainties rather than claiming unperformed validation.
