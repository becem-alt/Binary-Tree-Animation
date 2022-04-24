from manim import *


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))
        self.play(circle.animate.set_fill(WHITE,opacity=1))
        text = Text("Hello world", font_size=16,color=BLACK)
        self.play(Write(text))
        self.play(circle.animate.shift(2 * RIGHT),
                  text.animate.shift(2 * RIGHT))

        self.wait()

