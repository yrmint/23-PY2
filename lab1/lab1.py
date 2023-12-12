# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Song:
    def __init__(self, name: str, author: str, genre: str, duration: float):
        """
                Создание и подготовка к работе объекта "Песня"

               :param name: Название песни
               :param author: Автор песни
               :param genre: Жанр песни
               :param duration: Длинельность песни (в минутах)

               Пример:
               >>> song = Song("Lovesong", "The Cure", "rock", 3.55)  # инициализация экземпляра класса
               """
        if not isinstance(name, str):
            raise TypeError("Название песни должно быть типа str")
        self.name = name
        if not isinstance(author, str):
            raise TypeError("Автор песни должен быть типа str")
        self.author = author
        if not isinstance(genre, str):
            raise TypeError("Жанр песни должен быть типа str")
        self.genre = genre
        if not isinstance(duration, float):
            raise TypeError("Длительность песни должна быть типа float")
        if duration < 0:
            raise ValueError("Длительность песни должна быть положительным числом")
        self.duration = duration

    def is_jazz_song(self) -> bool:
        """
                Проверяет, принадлежит ли песня к жанру джаз
                :return: Принадлежит ли песня к жанру джаз

                Пример:
                >>> song = Song("Hello, Dolly", "Louie Armstrong", "jazz", 5.1)
                >>> song.is_jazz_song()
        """
        ...

    @staticmethod
    def remix(new_genre: str) -> None:
        """
                Меняет жанр песни

                :param new_genre: новый жанр песни

                Пример:
                >>> song = Song("Lovesong", "The Cure", "rock", 3.55)
                >>> song.remix("pop")
        """
        if not isinstance(new_genre, str):
            raise TypeError("Жанр песни должен быть типа str")
        ...


class Playlist:
    def __init__(self, songs: list[str]):
        """
              Создание и подготовка к работе объекта "Плэйлист"

               :param songs: Список песен, входящих в плэйлист

               >>> playlist = Playlist(["Forever", "Please", "Vanity", "Risk"])
        """
        if not isinstance(songs, list):
            raise TypeError("Плейлист должен быть списком")
        for song in songs:
            if not isinstance(song, str):
                raise TypeError("Песни должны быть типа str")
        self.songs = songs

    @staticmethod
    def add_song(song: str) -> None:
        """
                Добавляет песню в плейлист

                :param song: песня, добавляемая в альбом

                Пример:
                >>> playlist = Playlist(["Cake"])
                >>> playlist.add_song("Due")
        """
        if not isinstance(song, str):
            raise TypeError("Песня должна быть типа str")
        ...

    def sort_songs(self) -> list[str]:
        """
                Возвращает список песен, отсортированных в алфавитном порядке

                :return: Список с объектами типа str, отсортированных в алфавитном порядке

                Пример:
                >>> playlist = Playlist(["Forever", "Please", "Vanity", "Risk"])
                >>> playlist.sort_songs()
        """
        ...


class Musician:
    def __init__(self, name: str, pseudonym: str):
        """
                Создание и подготовка к работе объекта "Музыкант"

                :param name: Имя музыканта
                :param pseudonym: Псевдоним музыканта

                Пример:
                       >>> musician = Musician("David Bowie", "Ziggy Stardust")
        """
        if not isinstance(name, str):
            raise TypeError("Имя музыканта должно быть типа str")
        self.name = name
        if not isinstance(pseudonym, str):
            raise TypeError("Псевдоним музыканта должен быть типа str")
        if pseudonym == name:
            raise ValueError("Псевдоним музыканта не должен совпадать с его именем")
        self.pseudonym = pseudonym

    def write_song(self, name: str, genre: str, duration: float) -> Song:
        """
                Пишет песню

                :param name: название песни
                :param genre: жанр песни
                :param duration: длительность песни
                :return: Объект класса Song

                Пример:
                >>> musician = Musician("David Bowie", "Ziggy Stardust")
                >>> musician.write_song("Starman", "glam-rock", 5.12)
        """
        ...

    def change_pseudonym(self, new_pseudonym: str) -> None:
        """
                Меняет псевдоним

                :param new_pseudonym: новый псевдоним музыканта

                Пример:
                >>> musician = Musician("David Bowie", "")
                >>> musician.change_pseudonym("Ziggy Stardust")
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
