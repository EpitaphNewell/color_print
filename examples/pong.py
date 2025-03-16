import os
import time
import random
from color_print import printc

def clear_screen():
    print("\033[2J\033[H", end="")

def draw_frame(ball_x, ball_y, left_paddle_y, right_paddle_y, width, height, paddle_size=4):
    frame = []
    frame.append("─" * width)
    for y in range(1, height - 1):
        line = ""
        for x in range(width):
            if x == 2 and left_paddle_y <= y < left_paddle_y + paddle_size:
                line += "{re}■"
            elif x == width - 3 and right_paddle_y <= y < right_paddle_y + paddle_size:
                line += "{bl}■"
            elif x == ball_x and y == ball_y:
                line += "{gr}■"
            else:
                line += " "
        frame.append(line)
    frame.append("─" * width)
    frame_str = "\n".join(frame) + "{rs}"
    printc(frame_str)

def pong_animation():
    width = 80
    height = 24
    paddle_size = 4
    ball_x = width // 2
    ball_y = height // 2
    ball_vel_x = random.choice([-1, 1])
    ball_vel_y = random.choice([-1, 1])
    left_paddle_y = (height - paddle_size) // 2
    right_paddle_y = (height - paddle_size) // 2
    try:
        while True:
            clear_screen()
            draw_frame(ball_x, ball_y, left_paddle_y, right_paddle_y, width, height, paddle_size)
            time.sleep(0.05)
            ball_x += ball_vel_x
            ball_y += ball_vel_y
            if ball_y <= 1 or ball_y >= height - 2:
                ball_vel_y *= -1
                ball_y += ball_vel_y
            if ball_x == 3 and left_paddle_y <= ball_y < left_paddle_y + paddle_size:
                ball_vel_x *= -1
                ball_x += ball_vel_x
            if ball_x == width - 4 and right_paddle_y <= ball_y < right_paddle_y + paddle_size:
                ball_vel_x *= -1
                ball_x += ball_vel_x
            if ball_x < 0 or ball_x >= width:
                ball_x = width // 2
                ball_y = height // 2
                ball_vel_x = random.choice([-1, 1])
                ball_vel_y = random.choice([-1, 1])
            left_center = left_paddle_y + paddle_size / 2
            if ball_y < left_center:
                left_paddle_y -= 1
            elif ball_y > left_center:
                left_paddle_y += 1
            right_center = right_paddle_y + paddle_size / 2
            if ball_y < right_center:
                right_paddle_y -= 1
            elif ball_y > right_center:
                right_paddle_y += 1
            if left_paddle_y < 1:
                left_paddle_y = 1
            if left_paddle_y + paddle_size > height - 1:
                left_paddle_y = height - 1 - paddle_size
            if right_paddle_y < 1:
                right_paddle_y = 1
            if right_paddle_y + paddle_size > height - 1:
                right_paddle_y = height - 1 - paddle_size
    except KeyboardInterrupt:
        clear_screen()
        printc("{yl}Animation Stopped{rs}")

if __name__ == "__main__":
    pong_animation()
