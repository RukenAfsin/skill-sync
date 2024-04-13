class Score:
    def __init__(self, name, surname, score1, score2, score3):
        self.name = name
        self.surname = surname
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def record_scores(self):
        with open(r"C:\Users\User\Desktop\scores.txt", "a") as scores:
            scores.write(f"{self.name} {self.surname} {self.score1} {self.score2} {self.score3}\n")

    @staticmethod
    def decorator(func):
        def wrapper():
            while True:
                name = input("Enter your name: ")
                surname = input("Enter your surname: ")
                if not name and not surname:  
                    break
                try:
                    score1 = int(input("Score 1: "))
                    score2 = int(input("Score 2: "))
                    score3 = int(input("Score 3: "))
                except ValueError as e:
                    print("You can not input out of number")
                    continue
                score_recorder = Score(name, surname, score1, score2, score3)
                score_recorder.record_scores()
                func()  
        return wrapper


# @Score.decorator
# def function():
#     pass

# function()
