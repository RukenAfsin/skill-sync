import json
import os
from user import User

class UserRepository():
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.loadUser()

    def loadUser(self):
        if os.path.exists('movie-demo/musers.json'):
            with open("movie-demo/musers.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'], password=user['password'], mail=user['mail'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı oluşturuldu')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                print("Successfully login")
                break
        else:
            print("username or password wrong")

    def logout(self):
        self.isLoggedIn = False
        print("Logout successful")

    def savetoFile(self):
        user_list = [user.__dict__ for user in self.users]
        with open("movie-demo/musers.json", "w") as file:
            json.dump(user_list, file)

repository = UserRepository()




class Movie:
    def __init__(self, movie_name, director, type, date, user_repository):
        self.movie_name = movie_name
        self.director = director
        self.type = type
        self.date = date
        self.user_repository = user_repository  

    def movie_add(self):
        if self.user_repository.isLoggedIn:
            self.save_to_file()
        else:
            print("You should login first")

    def save_to_file(self):
        movie_data = {
            "movie_name": self.movie_name,
            "director": self.director,
            "type": self.type,
            "date": self.date
        }
        with open("movie-demo/movies.json", "a") as file:
            json.dump(movie_data, file)
            file.write('\n')  

    def search(self, movie_name, director):
      with open("movie-demo/movies.json", "r") as file:
        movies = json.load(file)
        for movie in movies:
            if movie_name == self.movie_name or director == self.director:
              print(f'Movie Found: {self.movie_name}, Director: {self.director}, Type: {self.type}, Date: {self.date}')
            else:
              print("Movie not found")




      

while True:
    print("Ana Menü".center(50, '*'))
    secim = input('1-Register\n2- Login\n3 - Logout\n4 - Movies\n5- Exit\nSeçiminiz:')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input("Username: ")
            password = input("Password: ")
            mail = input("Mail: ")
            user = User(username=username, password=password, mail=mail)
            repository.register(user)

        elif secim == '2':
            if repository.isLoggedIn:
                print("You are already logged in.")
            else:
                username = input('Username: ')
                password = input('Password: ')
                repository.login(username, password)

        elif secim == '3':
            repository.logout()

        elif secim == '4':
            while True:
                print("Movie Menüsü".center(50, '*'))
                secim = input('1-Add Movie\n2- Movies List\n3- Search Movie\n4- Back to Main Menu\nSeçiminiz:')
                if secim == '1':
                    if repository.isLoggedIn:
                        movie_name = input("Please input the movie's name: ")
                        director = input("Who is the director: ")
                        type = input("What is the movie's type: ")
                        date = int(input("What is the vision date: "))
                        movie = Movie(movie_name, director, type, date, repository)
                        movie.movie_add()
                        print("Movie successfully saved!!")
                    else:
                        print("You should login first")
                elif secim == '3':
                  movie_name = input("Enter the movie name: ")
                  director = input("Enter the director name: ")
                  movie = Movie("", "", "", "", repository)  
                  movie.search(movie_name, director)
                elif secim == '2':
                    pass
                elif secim == '4':
                    break
                else:
                    print('Yanlış seçim. Lütfen tekrar deneyin.')
