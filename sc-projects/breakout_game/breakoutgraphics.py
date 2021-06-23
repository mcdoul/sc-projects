"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

File: number_of_words.py
Name: Charlotte Yang
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.bg = GRect(width=window_width, height=window_height)
        self.bg.filled = True
        self.bg.fill_color = 'whitesmoke'
        self.bg.color = 'whitesmoke'
        self.window.add(self.bg)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = '#8F8681'
        self.paddle.color = '#8F8681'
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.fill_color ='#8F8681'
        self.ball.color = '#8F8681'
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.switch = True
        onmouseclicked(self.start)
        onmousemoved(self.move_paddle)

        # check dead
        self.check_dead()

        # Draw bricks
        self.brick_cols = BRICK_COLS
        self.brick_rows = BRICK_ROWS
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                self.brick = GRect(brick_width, brick_height)
                if j <= self.brick_rows*(1/5):
                    self.brick.filled = True
                    self.brick.fill_color = '#7CACBE'
                    self.brick.color = '#7CACBE'
                if j >= self.brick_rows*(1/5):
                    self.brick.filled = True
                    self.brick.fill_color = '#BBD3D9'
                    self.brick.color = '#BBD3D9'
                if j >= self.brick_rows*(2/5):
                    self.brick.filled = True
                    self.brick.fill_color = '#A4BFB0'
                    self.brick.color = '#A4BFB0'
                if j >= self.brick_rows*(3/5):
                    self.brick.filled = True
                    self.brick.fill_color = '#74A685'
                    self.brick.color = '#74A685'
                if j >= self.brick_rows*(4/5):
                    self.brick.filled = True
                    self.brick.fill_color = '#BCBFB1'
                    self.brick.color = '#BCBFB1'
                self.brick.x = i*brick_spacing+i*self.brick.width
                self.brick.y = brick_offset + j*brick_spacing+j*self.brick.height
                self.window.add(self.brick, self.brick.x, self.brick.y)

        # count bricks
        self.count = 0
        self.check_win()

        # score board
        self.score = -1
        self.score_board = GLabel('score '+str(self.score))
        self.score_board.color = '#776c5b'
        self.score_board.font = 'SANSSERIF-12'
        self.window.add(self.score_board, 7, self.window.height - 7)
        self.line = GRect(230, 0.05)
        self.line.filled = True
        self.line.fill_color = '#d9d3ce'
        self.line.color = '#d9d3ce'
        self.window.add(self.line, 80, self.window.height - 14)

        # life
        self.lives = GLabel('Lives')
        self.lives.color = '#77665b'
        self.lives.font = 'SANSSERIF-12'
        self.window.add(self.lives, self.window.width - 125, self.window.height - 7)
        self.square1 = GRect(15, 10)
        self.square1.filled = True
        self.square1.fill_color = '#A5948A'
        self.square1.color = '#A5948A'
        self.square2 = GRect(15, 10)
        self.square2.filled = True
        self.square2.fill_color = '#A5948A'
        self.square2.color = '#A5948A'
        self.square3 = GRect(15, 10)
        self.square3.filled = True
        self.square3.fill_color = '#A5948A'
        self.square3.color = '#A5948A'
        self.window.add(self.square1, self.window.width - 75, self.window.height - 22)
        self.window.add(self.square2, self.window.width - 50, self.window.height - 22)
        self.window.add(self.square3, self.window.width - 25, self.window.height - 22)

    def move_paddle(self, e):
        if e.x <= self.paddle.width/2:
            e_x = self.paddle.width/2
        elif e.x >= self.window.width-self.paddle.width/2:
            e_x = self.window.width-self.paddle.width/2
        else:
            e_x = e.x
        paddle_x = e_x - self.paddle.width / 2
        paddle_y = self.window.height - self.paddle_offset - self.paddle.height
        self.window.add(self.paddle, paddle_x, paddle_y)

    def start(self, e_c):
        if self.switch:
            self.switch = False
            self.set_ball()

    def set_ball(self):
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() < 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def remove(self):
        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        right_up = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        right_down = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if left_up is not None and left_up is not self.paddle:
            if self.ball.y <= 0.5 * self.window.height:
                self.__dy *= -1
                self.window.remove(left_up)
                self.count += 1
                self.score += 1
        elif left_up is self.paddle:
            self.__dy = -1 * abs(self.__dy)  # make sure the ball always goes up
        elif left_down is not None and left_up is not self.paddle:  # 'elif' slows the game
            if self.ball.y <= 0.5 * self.window.height:
                self.__dy *= -1
                self.window.remove(left_down)
                self.count += 1
                self.score += 1
        elif left_down is self.paddle:
            self.__dy = -1 * abs(self.__dy)
        elif right_up is not None and left_up is not self.paddle:
            if self.ball.y <= 0.5 * self.window.height:
                self.__dy *= -1
                self.window.remove(right_up)
                self.count += 1
                self.score += 1
        elif right_up is self.paddle:
            self.__dy = -1 * abs(self.__dy)
        elif right_down is not None and left_up is not self.paddle:
            if self.ball.y <= 0.5 * self.window.height:
                self.__dy *= -1
                self.window.remove(right_down)
                self.count += 1
                self.score += 1
        elif right_down is self.paddle:
            self.__dy = -1 * abs(self.__dy)

    def check_dead(self):
        self.switch = True
        self.__dx = 0
        self.__dy = 0

    def check_edge(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1

    def check_win(self):
        if self.count == (self.brick_rows * self.brick_cols):
            return 1
        else:
            return 0

    def renew_score(self):
        self.score_board.text = 'Score: '+str(self.score)
