import doctest


class Table:
    def __init__(self, material: str, height: float, color: str) -> None:
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param height: Высота стола в сантиметрах
        :param color: Цвет стола

        Примеры:
        >>> table = Table("Дуб", 75.0, "Коричневый")  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        if not material or not material.strip():
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if not color or not color.strip():
            raise ValueError("Цвет не может быть пустым")
        self.color = color

    def fold(self) -> str:
        """
        Функция которая складывает стол

        :return: Сообщение о результате складывания

        Примеры:
        >>> table = Table("Пластик", 60.0, "Белый")
        >>> table.fold()
        'Стол сложен'
        """
        return "Стол сложен"

    def change_color(self, new_color: str) -> str:
        """
        Изменение цвета стола

        :param new_color: Новый цвет стола
        :return: Сообщение о смене цвета
        :raise ValueError: Если новый цвет пустой

        Примеры:
        >>> table = Table("Металл", 72.0, "Черный")
        >>> table.change_color("Серый")
        'Цвет стола изменён на Серый'
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")
        if not new_color or not new_color.strip():
            raise ValueError("Цвет не может быть пустым")
        self.color = new_color
        return f"Цвет стола изменён на {new_color}"

    def adjust_height(self, new_height: float) -> str:
        """
        Регулировка высоты стола

        :param new_height: Новая высота стола в сантиметрах
        :return: Сообщение о регулировке высоты
        :raise ValueError: Если новая высота не положительная

        Примеры:
        >>> table = Table("Дуб", 70.0, "Коричневый")
        >>> table.adjust_height(75.0)
        'Высота стола изменена на 75.0 см'
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Новая высота должна быть типа int или float")
        if new_height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = new_height
        return f"Высота стола изменена на {new_height} см"


class Tree:
    def __init__(self, species: str, age: int, height: float) -> None:
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param age: Возраст дерева в годах
        :param height: Высота дерева в метрах

        Примеры:
        >>> tree = Tree("Дуб", 50, 15.5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not species or not species.strip():
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def grow(self, years: int) -> str:
        """
        Процесс роста дерева

        :param years: Количество лет роста
        :return: Сообщение о результате роста
        :raise ValueError: Если количество лет отрицательное

        Примеры:
        >>> tree = Tree("Сосна", 10, 5.0)
        >>> tree.grow(5)
        'Дерево выросло на 5 лет, текущий возраст: 15 лет'
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным")
        self.age += years
        return f"Дерево выросло на {years} лет, текущий возраст: {self.age} лет"

    def shed_leaves(self) -> str:
        """
        Функция которая имитирует сбрасывание листвы деревом

        :return: Сообщение о сбрасывании листьев

        Примеры:
        >>> tree = Tree("Береза", 20, 12.0)
        >>> tree.shed_leaves()
        'Дерево сбросило листву'
        """
        return "Дерево сбросило листву"

    def get_info(self) -> str:
        """
        Получение информации о дереве

        :return: Строка с информацией о дереве

        Примеры:
        >>> tree = Tree("Клен", 15, 8.5)
        >>> tree.get_info()
        'Вид: Клен, Возраст: 15 лет, Высота: 8.5 м'
        """
        return f"Вид: {self.species}, Возраст: {self.age} лет, Высота: {self.height} м"


class SocialNetwork:
    def __init__(self, name: str, users_count: int, founded_year: int) -> None:
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param users_count: Количество пользователей
        :param founded_year: Год основания

        Примеры:
        >>> network = SocialNetwork("MAX", 1000, 2025)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not name or not name.strip():
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.users_count = users_count

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть типа int")
        if founded_year < 1900 or founded_year > 2026:
            raise ValueError("Год основания должен быть между 1900 и 2026")
        self.founded_year = founded_year

    def register_user(self, username: str) -> str:
        """
        Регистрация нового пользователя

        :param username: Имя пользователя
        :return: Сообщение о регистрации
        :raise ValueError: Если имя пользователя пустое

        Примеры:
        >>> network = SocialNetwork("Twitter", 500000000, 2006)
        >>> network.register_user("Evgeny")
        'Пользователь Evgeny успешно зарегистрирован'
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username or not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        self.users_count += 1
        return f"Пользователь {username} успешно зарегистрирован"

    def post_message(self, user: str, message: str) -> str:
        """
        Публикация сообщения в социальной сети

        :param user: Имя пользователя
        :param message: Текст сообщения
        :return: Сообщение о публикации
        :raise ValueError: Если имя пользователя или сообщение пустые

        Примеры:
        >>> network = SocialNetwork("Instagram", 2000000000, 2010)
        >>> network.post_message("Evgeny", "Hello world!")
        'Пользователь Evgeny опубликовал сообщение'
        """
        if not isinstance(user, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not user or not user.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть типа str")
        if not message or not message.strip():
            raise ValueError("Сообщение не может быть пустым")
        return f"Пользователь {user} опубликовал сообщение"

    def get_statistics(self) -> dict:
        """
        Получение статистики социальной сети

        :return: Словарь со статистикой

        Примеры:
        >>> network = SocialNetwork("VK", 100000000, 2006)
        >>> stats = network.get_statistics()
        >>> stats['name']
        'VK'
        >>> stats['users_count'] > 0
        True
        """
        return {
            "name": self.name,
            "users_count": self.users_count,
            "founded_year": self.founded_year,
        }


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации