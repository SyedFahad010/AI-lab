# FizzBuzz

class FizzBuzz:
    def __init__(self, start=1, end=50):
        self.start = start
        self.end = end

    def play(self):
        for num in range(self.start, self.end + 1):
            text = ""
            if num % 3 == 0:
                text += "Fizz"
            if num % 5 == 0:
                text += "Buzz"
            if text == "":
                text = str(num)
            print(f"{num:>3} → {text}")

game = FizzBuzz(1, 50)
game.play()
