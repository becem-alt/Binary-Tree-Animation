from manim import *


class CircleToTop(Scene):
    def construct(self):
        circle = Circle(radius=1)  # create a circle
        circle.set_fill(WHITE, opacity=0.9)  # set the color and transparency
        self.play(GrowFromCenter(circle))
        # self.play(circle.animate.set_fill(WHITE,opacity=0.8))
        text = Text("165", font_size=22, color=BLACK)
        self.play(Write(text, color=BLACK))
        self.play(circle.animate.shift(2 * UP).scale(0.7),
                  text.animate.shift(2 * UP).scale(0.7))
        toRight = Line([0, 1.3, 0], [1, 0, 0])
        toLeft = Line([0, 1.3, 0], [-1, 0, 0])
        leftNode = Circle(radius=0.5).shift(1*RIGHT + 0.5*DOWN).set_fill(color=WHITE,opacity=0.9)
        rightNode = Circle(radius=0.5).shift(0.5*DOWN + 1*LEFT).set_fill(color=WHITE,opacity=0.9)
        text = Text("170", font_size=22, color=BLACK).shift(1*RIGHT + 0.5*DOWN)
        text1 = Text("150", font_size=22, color=BLACK).shift(0.5*DOWN + 1*LEFT)
        self.play(Create(toRight), Create(toLeft))
        self.play(GrowFromCenter(leftNode), GrowFromCenter(rightNode))
        self.play(Write(text),Write(text1))
        self.wait(3)
