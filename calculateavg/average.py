from score import Score

class Average(Score):
    @staticmethod
    def average_decorator(func):
        def wrapper():
            with open(r"C:\Users\User\Desktop\scores.txt", "r") as scores:
                for score in scores:
                    data = score.split()
                    print(data)  
                    name = data[0]
                    surname = data[1]                 
                    score1 = int(data[2])
                    score2 = int(data[3])
                    score3 = int(data[4])
                    avg = (score1*20/100)+(score2*30/100)+(score3*50/100)
                    print(f'{name} {surname} your average is: {avg}')
                    with open(r"C:\Users\User\Desktop\avg.txt", "a") as avg_file:
                        if avg == 0 or avg < 25:
                            avg_file.write(f'{name} {surname} : {avg} // GRADE: F\n')
                        elif 25 <= avg < 45:
                            avg_file.write(f'{name} {surname} : {avg} // GRADE: D\n') 
                        elif 45 <= avg < 65:
                            avg_file.write(f'{name} {surname} : {avg} // GRADE: C\n') 
                        elif 65 <= avg < 80:
                            avg_file.write(f'{name} {surname} : {avg} // GRADE: B\n') 
                        elif avg >= 85:
                            avg_file.write(f'{name} {surname} : {avg} // GRADE: A\n') 
            return func()  
        return wrapper

@Average.average_decorator
def record_avg():
    pass

record_avg()
