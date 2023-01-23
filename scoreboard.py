from turtle import Turtle


FONT = ("Arial", 15, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = -1
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def game_ended(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
        self.high_score()

    def high_score(self):
        # open and read existing high score file (if exists)
        # if this games score is higher, save high score
        try:
            fd = None
            # use append "plus" mode for read/write, and creation if file doesn't exist
            with open("./high_score.txt", "a+t") as fd:
                fd.seek(0)
                contents = fd.read()
                print(type(contents))
                if len(contents) > 0:
                    print(f"Previous high score is {contents}")
                    if self.score > int(contents):
                        print(f"Well done, with {self.score} you are new high scorer!")
                        fd.seek(0)
                        fd.truncate()
                        fd.write(f"{self.score}")
                else:
                    print(f"No previous high score, you are new high scorer!")
                    fd.write(f"{self.score}")
        except IOError:
            print("IOError")
        except ValueError:
            print("ValueError")
        except Exception as e:
            print(f"some other error: {e}")
        finally:
            if fd:
                fd.close()




