# OLD VERSION 
import traceback

def format_text(text, error=None):
    codes = {
        "{re}": "\033[91m",
        "{yl}": "\033[93m",
        "{gr}": "\033[92m",
        "{bl}": "\033[94m",
        "{rs}": "\033[0m"
    }

    if "{er}" in text:
        err_text = "[ERROR]"
        if error:
            err_text += f" {error}"
        text = text.replace("{er}", f"\033[91m{err_text}\033[0m")

    for key, value in codes.items():
        text = text.replace(key, value)

    if not text.endswith("\033[0m"):
        text += "\033[0m"

    return text

def printc(text, error=None):
    print(format_text(text, error))

def print_error(e):
    error_msg = traceback.format_exc().strip().split("\n")[-1]
    printc("{er}", error_msg)
