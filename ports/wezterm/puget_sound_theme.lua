-- Puget Sound terminal color schemes
-- This file returns a table suitable for assigning to config.color_schemes.

return {
  ['Puget Sound morning'] = {
    foreground = '#3E515E',
    background = '#F9FCFF',
    cursor_bg = '#3E515E',
    cursor_fg = '#F9FCFF',
    cursor_border = '#3E515E',
    selection_fg = '#3E515E',
    selection_bg = '#C8DDFC',
    scrollbar_thumb = '#7D8E97',
    split = '#ACBCC2',
    ansi = {
      '#3E515E',  -- 0
      '#AA534E',  -- 1
      '#789667',  -- 2
      '#B7A36F',  -- 3
      '#5278A7',  -- 4
      '#7E76A6',  -- 5
      '#5592A1',  -- 6
      '#ACBCC2',  -- 7
    },
    brights = {
      '#5A6C74',  -- 0
      '#E07B6F',  -- 1
      '#A7C681',  -- 2
      '#D3C084',  -- 3
      '#7AA1DA',  -- 4
      '#A89CD3',  -- 5
      '#75B8CC',  -- 6
      '#F9FCFF',  -- 7
    },
  },

  ['Puget Sound evening'] = {
    foreground = '#C1CCD3',
    background = '#18242F',
    cursor_bg = '#86ACDE',
    cursor_fg = '#18242F',
    cursor_border = '#86ACDE',
    selection_fg = '#C1CCD3',
    selection_bg = '#496594',
    scrollbar_thumb = '#495B68',
    split = '#496594',
    ansi = {
      '#18242F',  -- 0
      '#E98C84',  -- 1
      '#88A46D',  -- 2
      '#D1BD88',  -- 3
      '#94BBEE',  -- 4
      '#ACA5D8',  -- 5
      '#6BAAB8',  -- 6
      '#9FADB3',  -- 7
    },
    brights = {
      '#2A3A46',  -- 0
      '#FFB5AD',  -- 1
      '#ADC98D',  -- 2
      '#FDE7B1',  -- 3
      '#CFE4FF',  -- 4
      '#D5D0FF',  -- 5
      '#93D4E1',  -- 6
      '#C1CCD3',  -- 7
    },
  },
}
