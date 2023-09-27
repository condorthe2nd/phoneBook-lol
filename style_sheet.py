from tkinter import ttk

# Colors
BG_COLOR = "thistle"
BUTTON_COLOR = "#2196F3"
BUTTON_TEXT_COLOR = "White"

# Fonts
FONT = "Helvetica 16"

# Icons
ADD_ICON = "\u2795"
SEARCH_ICON = "\U0001F50D"
EXIT_ICON = "\U0001F6AA"

# Themes
THEME = 'clam'


def configure_button_style():
    style = ttk.Style()
    style.theme_use(THEME)


def configure_label_style():
    style = ttk.Style()
    style.theme_use(THEME)


def get_styles():
    return {
        'BG_COLOR': BG_COLOR,
        'FONT': FONT,
        'BUTTON_COLOR': BUTTON_COLOR,
        'BUTTON_TEXT_COLOR': BUTTON_TEXT_COLOR,
        'configure_button_style': configure_button_style  # Adding the function to the dictionary
    }
