import random
import sys
from pyfiglet import Figlet

def check_argv(fonts: list):
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        return sys.argv[2] in fonts
    return False

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        if len(sys.argv) == 3 and check_argv(fonts):
            choice = sys.argv[2]
        else:
            choice = random.choice(fonts)
        if len(sys.argv) == 1:
            text = input("Input: ")
        else:
            text = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        rendered_text = figlet.renderText(text)
        print(rendered_text)
    else:
        #print("Usage: python script.py [-f <font>] <text>")
        sys.exit(1)  # Exit with non-zero exit code for invalid arguments

if __name__ == "__main__":
    main()
