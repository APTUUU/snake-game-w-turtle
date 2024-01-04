from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(0, 280)
        self.color("white")
        self.high_score = 0
        self.link()
        self.score = 0
        self.show_stats()

    def show_stats(self):
        """Display the current score and high score."""
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score} ", move=False, align="center",
                   font=("verdana", 12, "normal"))

    def add(self):
        """Increase the score by 1 and update the displayed score."""
        self.score += 1
        self.clear()
        self.show_stats()

    def reset_score(self):
        """Reset the score and update the high score if necessary."""
        self.setpos(0, 280)
        if self.high_score <= self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score_file:
                high_score_file.write(str(self.high_score))
        self.clear()
        self.score = 0
        self.show_stats()

    def link(self):
        """Read the high score from a file and set it as the high score."""
        try:
            with open("data.txt", mode="r") as high_score_file:
                high_score_text = high_score_file.read()
                self.high_score = int(high_score_text)
        except FileNotFoundError:
            pass
