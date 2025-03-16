import random
from color_print import printc

def draw_square(size=10, symbol="█"):
    colors = ["{re}", "{yl}", "{gr}", "{bl}"]
    for _ in range(size):
        line = ""
        for _ in range(size):
            color = random.choice(colors)
            line += f"{color}{symbol}"
        printc(line)

if __name__ == "__main__":
    draw_square()
    printc("=={re}C{rs}{yl}U{rs}{gr}B{rs}{bl}E{rs}!==")
