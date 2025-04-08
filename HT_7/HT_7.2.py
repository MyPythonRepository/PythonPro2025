import sys
from colorama import Fore, Style, init


class TextColorizer:
    def __init__(self, text_color):
        init(autoreset=True)
        self.color_code = getattr(Fore, text_color.upper(), Fore.RESET)
        self.default_write = sys.stdout.write

    def __enter__(self):
        sys.stdout.write = self.colored_output

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.default_write

    def colored_output(self, text):
        self.default_write(self.color_code + text + Style.RESET_ALL)


with TextColorizer("green"):
    print("Text is green")
print("Default text color")
