import json
import os
from userRepo import UserRepository

class Movie:
    def __init__(self, movie_name, director, type, date):
        self.movie_name = movie_name
        self.director = director
        self.type = type
        self.date = date
        self.user = UserRepository()  

    def movie_add(self, movie: "Movie"):
        if self.user.isLoggedIn:
            self.movies.append(movie)
            self.save_to_file()
        else:
            print("You should login first")

    def save_to_file(self):
        list=[]
        for movie in self.movies:
            list.append(json.dumps(movie.__dict__))

        with open("movie-demo/movies.json", "w") as file:
            json.dump(movie_list, file)
