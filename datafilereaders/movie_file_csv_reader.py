import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                self.__dataset_of_movies.append(movie)
                actors = row["Actors"]
                actors = actors.split(",")
                for actor in actors:
                    actor = Actor(actor)
                    movie.add_actor(actor)

                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)

                director = Director(row["Director"])
                movie.director = director

                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)

                genres = row["Genre"]
                genres = genres.split(",")
                for genre in genres:
                    genre = Genre(genre)
                    movie.add_genre(genre)

                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre)

                movie.description = row["Description"]
                movie.runtime_minutes = row["Runtime (Minutes)"]

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> list:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> list:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> list:
        return self.__dataset_of_genres


reader = MovieFileCSVReader("C:\\Users\\aidan\\OneDrive\\Desktop\\Year "
                            "2\\COMPSCI235\\A1\\CS235Flix\\datafiles\\Data1000Movies.csv")
reader.read_csv_file()
print(len(reader.dataset_of_movies))
print(len(reader.dataset_of_actors))
print(len(reader.dataset_of_directors))
print(len(reader.dataset_of_genres))
print(reader.dataset_of_genres)