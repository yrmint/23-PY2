class Painting:
    """ Базовый класс картины """

    def __init__(self, name: str, author: str, price: float) -> None:
        """
            Инициализация экземпляра класса
            :param name: название картины
            :param author: имя или псевдоним автора
            :param price: цена картины
        """

        self.name = name
        self.author = author
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Название картины должно быть типа str")
        if not new_name:
            raise ValueError("Название картины не может быть пустой строкой")
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("Имя или псевдоним автора должен быть типа str")
        if not new_author:
            raise ValueError("Имя или псевдоним автора не может быть пустой строкой")
        self._author = new_author

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if not isinstance(new_price, float):
            raise TypeError("Цена картины должна быть типа float")
        if new_price <= 0:
            raise ValueError("Цена картины должна быть положительным числом")
        self._price = new_price

    def __str__(self) -> str:
        return f"Картина {self._name}. Автор {self._author}. Цена {self._price}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r})"

    def get_final_price(self) -> float:
        """
            Возвращает окончательную цену картины с учётом налога
        """
        return round(self._price * 1.1, 2)


class TraditionalPainting(Painting):
    """
        Дочерний класс - традиционная (физическая) картина
    """

    def __init__(self, name: str, author: str, price: float, material: str) -> None:
        """
            Инициализация экземпляра класса
            :param name: название картины
            :param author: имя или псевдоним автора
            :param price: цена картины
            :param material: материал
        """
        super().__init__(name, author, price)
        self.material = material

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, new_material: str) -> None:
        if not isinstance(new_material, str):
            raise TypeError("Материал должен быть типа str")
        self._material = new_material

    def __str__(self) -> str:
        return f"Картина {self._name}. Автор {self._author}. Цена {self._price}. Материал {self._material}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r}, " \
               f"material={self._material!r})"

    def get_final_price(self, shipping_cost: float) -> float:
        """
            В окончательную цену традиционной картины входит стоимость доставки
            :param shipping_cost: стоимость доставки
        """
        if not isinstance(shipping_cost, float):
            raise TypeError("Стоимость доставки должна быть типа float")
        if shipping_cost < 0:
            raise ValueError("Стоимость доставки должна быть неотрицательным числом")
        return super().get_final_price() + shipping_cost


class DigitalPainting(Painting):
    """
        Дочерний класс - цифровая картина
    """
    def __init__(self, name: str, author: str, price: float, file_format: str) -> None:
        """
            Инициализация экземпляра класса
            :param name: название картины
            :param author: имя или псевдоним автора
            :param price: цена картины
            :param file_format: формат файла
        """
        super().__init__(name, author, price)
        self.file_format = file_format

    @property
    def file_format(self) -> str:
        return self._file_format

    @file_format.setter
    def file_format(self, new_file_format: str) -> None:
        if not isinstance(new_file_format, str):
            raise TypeError("Формат файла должен быть типа str")
        if not new_file_format:
            raise ValueError("Формат файла не может быть пустой строкой")
        self._file_format = new_file_format

    def __str__(self) -> str:
        return f"Картина {self._name}. Автор {self._author}. Цена {self._price}. Формат файла {self._file_format}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r}, " \
               f"file_format={self._file_format!r})"

    def is_valid_format(self, file_formats: list[str]) -> bool:
        """
            Проверяет, валиден ли формат файла, т. е. входит ли он в список заданных форматов
        """
        return self._file_format in file_formats


if __name__ == "__main__":
    p1 = Painting("test name", "test author", 300.0)
    p2 = TraditionalPainting("name2", "author2", 300.0, "watercolor")
    p3 = DigitalPainting("name3", "author3", 100.0, "pdf")
    list_p = [p1, p2, p3]
    for p in list_p:
        print(p)
    print(list_p)
    print(p2.get_final_price(10.0))
    print(p3.get_final_price())

    formats = ["png", "jpg", "pdf", "psd"]
    print(p3.is_valid_format(formats))
    pass
