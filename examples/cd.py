from color_print import printc

import os
import random

def random_folder_path(start=None):
    if start is None:
        start = os.path.expanduser('~')
    path = start
    while True:
        try:
            subdirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            if not subdirs:
                break
            chosen = random.choice(subdirs)
            new_path = os.path.join(path, chosen)
            if random.choice([True, False]):
                path = new_path
            else:
                path = new_path
                break
        except PermissionError:
            break
    return path

def print_colored_path(path):
    parts = [p for p in path.split(os.sep) if p]
    available_colors = ["{re}", "{yl}", "{gr}", "{bl}"]
    colored_parts = []
    for part in parts:
        if available_colors:
            color = random.choice(available_colors)
            available_colors.remove(color)
        else:
            color = random.choice(["{re}", "{yl}", "{gr}", "{bl}"])
        colored_parts.append(f"{color}{part}")
    colored_path = os.sep.join(colored_parts)
    printc(colored_path)

if __name__ == "__main__":
    folder = random_folder_path()
    print_colored_path(folder)

