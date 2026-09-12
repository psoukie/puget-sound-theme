-- Puget Sound terminal color schemes
-- This file returns a table suitable for assigning to config.color_schemes.

local palettes = {
  morning = {
    ['bg-0'] = '#F9FCFF',
    ['bg-1'] = '#E0EAEF',
    ['bg-2'] = '#B9C9D0',
    ['fg-0'] = '#3E515E',
    ['fg-1'] = '#5A6C74',
    ['fg-2'] = '#6A7B84',
    ['blue-0'] = '#375378',
    ['blue-1'] = '#7298CA',
    ['blue-2'] = '#C8DDFC',
    ['blue-3'] = '#E4EFFF',
    ['red'] = '#AA534E',
    ['orange'] = '#AA7223',
    ['yellow'] = '#B7A36F',
    ['green'] = '#708F6D',
    ['blue'] = '#5278A7',
    ['teal'] = '#5592A1',
    ['purple'] = '#7E76A6',
  },
  evening = {
    ['bg-0'] = '#18242F',
    ['bg-1'] = '#2A3A46',
    ['bg-2'] = '#4E5C68',
    ['fg-0'] = '#C1CCD3',
    ['fg-1'] = '#9FADB3',
    ['fg-2'] = '#87959C',
    ['blue-0'] = '#B2BFDB',
    ['blue-1'] = '#8194BA',
    ['blue-2'] = '#496594',
    ['blue-3'] = '#31466C',
    ['red'] = '#E98C84',
    ['orange'] = '#D79C52',
    ['yellow'] = '#D1BD88',
    ['green'] = '#90B18E',
    ['blue'] = '#8BB2E4',
    ['teal'] = '#72B1BF',
    ['purple'] = '#AAA3D6',
  },
}

local terminal = {
  morning = {
    ansi = {
      black = palettes.morning['bg-0'], red = palettes.morning['red'],
      green = '#789667', yellow = palettes.morning['yellow'],
      blue = palettes.morning['blue'], magenta = palettes.morning['purple'],
      cyan = palettes.morning['teal'], white = '#ACBCC2',
    },
    brights = {
      black = palettes.morning['fg-1'], red = '#E07B6F', green = '#A7C681',
      yellow = '#D3C084', blue = '#7AA1DA', magenta = '#A89CD3',
      cyan = '#75B8CC', white = palettes.morning['bg-0'],
    },
  },
  evening = {
    ansi = {
      black = palettes.evening['bg-0'], red = palettes.evening['red'],
      green = '#88A46D', yellow = palettes.evening['yellow'],
      blue = '#94BBEE', magenta = '#ACA5D8', cyan = '#6BAAB8',
      white = palettes.evening['fg-1'],
    },
    brights = {
      black = palettes.evening['bg-1'], red = '#FFB5AD', green = '#ADC98D',
      yellow = '#FDE7B1', blue = '#CFE4FF', magenta = '#D5D0FF',
      cyan = '#93D4E1', white = palettes.evening['fg-0'],
    },
  },
}

return {
  ['Puget Sound morning'] = {
    foreground = palettes.morning['fg-0'],
    background = palettes.morning['bg-0'],
    cursor_bg = palettes.morning['fg-0'],
    cursor_fg = palettes.morning['bg-0'],
    cursor_border = palettes.morning['fg-0'],
    selection_fg = palettes.morning['fg-0'],
    selection_bg = palettes.morning['blue-2'],
    scrollbar_thumb = '#7D8E97',
    split = '#ACBCC2',
    ansi = {
      terminal.morning.ansi.black,     -- 0
      terminal.morning.ansi.red,       -- 1
      terminal.morning.ansi.green,     -- 2
      terminal.morning.ansi.yellow,    -- 3
      terminal.morning.ansi.blue,      -- 4
      terminal.morning.ansi.magenta,   -- 5
      terminal.morning.ansi.cyan,      -- 6
      terminal.morning.ansi.white,     -- 7
    },
    brights = {
      terminal.morning.brights.black,  -- 0
      terminal.morning.brights.red,    -- 1
      terminal.morning.brights.green,  -- 2
      terminal.morning.brights.yellow, -- 3
      terminal.morning.brights.blue,   -- 4
      terminal.morning.brights.magenta,-- 5
      terminal.morning.brights.cyan,   -- 6
      terminal.morning.brights.white,  -- 7
    },
  },

  ['Puget Sound evening'] = {
    foreground = palettes.evening['fg-0'],
    background = palettes.evening['bg-0'],
    cursor_bg = '#86ACDE',
    cursor_fg = palettes.evening['bg-0'],
    cursor_border = '#86ACDE',
    selection_fg = palettes.evening['fg-0'],
    selection_bg = palettes.evening['blue-2'],
    scrollbar_thumb = '#495B68',
    split = palettes.evening['blue-2'],
    ansi = {
      terminal.evening.ansi.black,     -- 0
      terminal.evening.ansi.red,       -- 1
      terminal.evening.ansi.green,     -- 2
      terminal.evening.ansi.yellow,    -- 3
      terminal.evening.ansi.blue,      -- 4
      terminal.evening.ansi.magenta,   -- 5
      terminal.evening.ansi.cyan,      -- 6
      terminal.evening.ansi.white,     -- 7
    },
    brights = {
      terminal.evening.brights.black,  -- 0
      terminal.evening.brights.red,    -- 1
      terminal.evening.brights.green,  -- 2
      terminal.evening.brights.yellow, -- 3
      terminal.evening.brights.blue,   -- 4
      terminal.evening.brights.magenta,-- 5
      terminal.evening.brights.cyan,   -- 6
      terminal.evening.brights.white,  -- 7
    },
  },
}
