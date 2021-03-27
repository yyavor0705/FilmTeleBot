import json


class Film:
    def __init__(self):
        self.__title = ""
        self.__category = ""
        self.__img = None

    def parse(self, dict_obj):
        self.__title = dict_obj.get("title", "")
        self.__category = dict_obj.get("category", "")
        file_name = dict_obj.get("picture_file")
        self.__load_img(file_name)

    def __load_img(self, file_name):
        with open("film_img/{}".format(file_name), 'rb') as fp:
            self.__img = fp.read()

    @property
    def title(self):
        return self.__title

    @property
    def category(self):
        return self.__category

    @property
    def img(self):
        return self.__img


class Films:
    def __init__(self):
        self.__categories_map = {}

    def load_all_films(self):
        with open("films.json", "r", encoding="utf-8") as fp:
            films_dict_obj = json.load(fp)
            films = films_dict_obj.get("films")
            for film in films:
                new_film = Film()
                new_film.parse(film)
                if new_film.category not in self.__categories_map:
                    self.__categories_map[new_film.category] = []
                self.__categories_map[new_film.category].append(new_film)

    def get_films_by_category(self, category):
        return self.__categories_map.get(category)

    @property
    def categories(self):
        return self.__categories_map.keys()