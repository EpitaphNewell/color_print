def format_text(text, error=None):
    codes = {
        "{re}": "\033[91m",
        "{yl}": "\033[93m",
        "{gr}": "\033[92m",
        "{bl}": "\033[94m",
        "{pu}": "\033[95m",
        "{rs}": "\033[0m"
    }

    if "{er}" in text:
        err_text = "[ОШИБКА]"
        if error:
            err_text += f" {error}"
        text = text.replace("{er}", f"{codes.get("{re}")}{err_text}{codes.get("{rs}")}")

    if "{wr}" in text:
        err_text = "[ПРЕДУПРЕЖДЕНИЕ]"
        if error:
            err_text += f" {error}"
        text = text.replace("{wr}", f"{codes.get("{yl}")}{err_text}{codes.get("{rs}")}")

    if "{if}" in text:
        err_text = "[ИНФО]"
        if error:
            err_text += f" {error}"
        text = text.replace("{if}", f"{codes.get("{bl}")}{err_text}{codes.get("{rs}")}")

    for key, value in codes.items():
        text = text.replace(key, value)

    if not text.endswith("\033[0m"):
        text += "\033[0m"

    return text
