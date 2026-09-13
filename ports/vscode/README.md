# Puget Sound for VS Code

`puget-sound-settings.jsonc` is a ready-to-merge VS Code user-settings customization for the built-in **Light 2026** and **Dark 2026** themes (with compatibility for **Default Light Modern** and **Default Dark Modern**). It is not an extension.

The `.jsonc` file is a template to copy from; it is not a separate extension to install. Open your VS Code settings as JSON by pressing `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) and choosing **Preferences: Open User Settings (JSON)**. Then copy the file’s three top-level settings (`workbench.colorCustomizations`, `editor.tokenColorCustomizations`, and `editor.semanticTokenColorCustomizations`) into that settings file. If you already have settings there, add these sections alongside them rather than deleting anything; make sure the setting immediately above the new sections ends with a comma. VS Code accepts the comments and the `.jsonc` format used here. Save the settings, then select the corresponding built-in theme in **Preferences: Color Theme**: 

- **Light 2026**, **Light Modern**, or **Default Light Modern** provides the Puget Sound Morning customization.
- **Dark 2026**, **Dark Modern**, or **Default Dark Modern** provides the Puget Sound Evening customization.

The customization covers workbench surfaces, editor states, diagnostics, source control, terminal ANSI colors, TextMate grammar scopes (`editor.tokenColorCustomizations`), and language-server semantic tokens (`editor.semanticTokenColorCustomizations`). The combined theme selectors support the current 2026 themes and the older Light/Dark Modern names. If the overrides do not apply, replace the theme names with the exact names shown by the Color Theme picker.

The file intentionally leaves font, layout, and icon choices unchanged. The palette values follow `palette/morning.json` and `palette/evening.json`, including the application-specific terminal colors.
