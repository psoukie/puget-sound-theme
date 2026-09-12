# Puget Sound for WezTerm

Place `puget_sound_theme.lua` alongside your `wezterm.lua`, then load both schemes into your configuration:

```lua
local schemes = require("puget_sound_theme")
config.color_schemes = config.color_schemes or {}
for name, scheme in pairs(schemes) do
  config.color_schemes[name] = scheme
end

config.color_scheme = "Puget Sound morning"
-- or: config.color_scheme = "Puget Sound evening"
```
