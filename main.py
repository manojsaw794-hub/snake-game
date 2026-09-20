from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from random import randint

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)
        self.food = (200, 200)
        Clock.schedule_interval(self.update, 0.1)

    def update(self, dt):
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake.insert(0, head)
        
        if abs(head[0] - self.food[0]) < 15 and abs(head[1] - self.food[1]) < 15:
            self.food = (randint(2, 20) * 20, randint(2, 20) * 20)
        else:
            self.snake.pop()

        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 1)
            for part in self.snake:
                Rectangle(pos=part, size=(15, 15))
            Color(1, 0, 0, 1)
            Rectangle(pos=self.food, size=(15, 15))

    def on_touch_down(self, touch):
        if touch.x > self.width / 2:
            self.direction = (0, 10) if self.direction[0] != 0 else (-10, 0)
        else:
            self.direction = (0, -10) if self.direction[0] != 0 else (10, 0)

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
