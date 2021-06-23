"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: number_of_words.py
Name: Charlotte Yang
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 60  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        # updates
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.remove()
        graphics.check_edge()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            if lives == 2:
                graphics.window.remove(graphics.square1)
            elif lives == 1:
                graphics.window.remove(graphics.square2)
            elif lives == 0:
                graphics.window.remove(graphics.square3)
                break
            graphics.set_ball()
            graphics.check_dead()  # switch=True
        # up date score
        graphics.renew_score()
        if graphics.check_win() == 1:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
