import doctest


class SocialNetwork:
    """
    Базовый класс, описывающий социальную сеть
    """

    def __init__(self, name: str, founded_year: int, country: str) -> None:
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param founded_year: Год основания
        :param country: Страна-владелец

        Атрибуты _name, _founded_year, _country непубличны, так как их изменение
        пользователем не подразумевается

        Примеры:
        >>> social_network = SocialNetwork("MAX", 2025, "Russia")
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        self._name = name

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть типа int")
        if founded_year < 1900 or founded_year > 2026:
            raise ValueError("Год основания должен быть между 1900 и 2026")
        self._founded_year = founded_year

        if not isinstance(country, str):
            raise TypeError("Страна должна быть типа str")
        if not country or not country.strip():
            raise ValueError("Страна не может быть пустой")
        self._country = country

    @property
    def name(self) -> str:
        return self._name

    @property
    def founded_year(self) -> int:
        return self._founded_year

    @property
    def country(self) -> str:
        return self._country

    def register_user(self, username: str) -> str:
        """
        Регистрация нового пользователя

        :param username: Имя пользователя
        :return: Сообщение о регистрации

        Примеры:
        >>> social_network = SocialNetwork("MAX", 2025, "Russia")
        >>> social_network.register_user("Evgeny")
        'Пользователь Evgeny зарегистрирован'
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username or not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        ...

    def get_info(self) -> str:
        """
        Получение информации о социальной сети

        :return: Строка с информацией

        Примеры:
        >>> social_network = SocialNetwork("MAX", 2025, "Russia")
        >>> social_network.get_info()
        'MAX основана в 2025 году в Russia'
        """
        ...

    def __str__(self) -> str:
        return f"Социальная сеть {self._name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, founded_year={self._founded_year!r}, country={self._country!r})"


class Twitter(SocialNetwork):
    """
    Дочерний класс, описывающий социальную сеть Twitter (X)

    :param name: Название социальной сети
    :param founded_year: Год основания
    :param country: Страна-владелец
    :param character_limit: Ограничение на количество символов в твите

    Атрибут _character_limit непубличен, так как его изменение пользователем
    не подразумевается

    Примеры:
    >>> twitter = Twitter("Twitter", 2006, "USA", 280)
    """

    def __init__(self, name: str, founded_year: int, country: str, character_limit: int) -> None:
        """
        Конструктор расширяет базовый, добавляя ограничение на символы
        """
        super().__init__(name, founded_year, country)

        if not isinstance(character_limit, int):
            raise TypeError("Лимит символов должен быть типа int")
        if character_limit <= 0:
            raise ValueError("Лимит символов должен быть положительным числом")
        self._character_limit = character_limit

    @property
    def character_limit(self) -> int:
        return self._character_limit

    def register_user(self, username: str) -> str:
        """
        Регистрация нового пользователя в Twitter

        Метод ПЕРЕГРУЖЕН, так как в Twitter имя пользователя должно начинаться с @

        :param username: Имя пользователя
        :return: Сообщение о регистрации

        Примеры:
        >>> twitter = Twitter("Twitter", 2006, "USA", 280)
        >>> twitter.register_user("@Evgeny")
        'Пользователь @Evgeny зарегистрирован в Twitter'
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username or not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if not username.startswith('@'):
            raise ValueError("Имя пользователя в Twitter должно начинаться с @")
        ...

    # Метод get_info наследуется от базового класса (не перегружен)

    def __str__(self) -> str:
        """
        Метод ПЕРЕГРУЖЕН, так как нужно отобразить лимит символов
        """
        return f"Twitter - {self._character_limit} символов в твите"

    def __repr__(self) -> str:
        """
        Метод ПЕРЕГРУЖЕН, так как нужно включить специфический атрибут
        """
        return f"{self.__class__.__name__}(name={self._name!r}, founded_year={self._founded_year!r}, country={self._country!r}, character_limit={self._character_limit!r})"


class VK(SocialNetwork):
    """
    Дочерний класс, описывающий социальную сеть ВКонтакте

    :param name: Название социальной сети
    :param founded_year: Год основания
    :param country: Страна-владелец
    :param users_count: Количество пользователей

    Атрибут _users_count непубличен, так как его изменение пользователем
    не подразумевается

    Примеры:
    >>> vk = VK("VK", 2006, "Russia", 100)
    """

    def __init__(self, name: str, founded_year: int, country: str, users_count: int) -> None:
        """
        Конструктор расширяет базовый, добавляя количество пользователей
        """
        super().__init__(name, founded_year, country)

        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self._users_count = users_count

    @property
    def users_count(self) -> int:
        return self._users_count

    def register_user(self, username: str) -> str:
        """
        Регистрация нового пользователя в ВКонтакте

        Метод ПЕРЕГРУЖЕН, так как в VK требуется проверка на допустимые символы
        (только буквы, цифры и знак подчеркивания)

        :param username: Имя пользователя
        :return: Сообщение о регистрации

        Примеры:
        >>> vk = VK("VK", 2006, "Russia", 100)
        >>> vk.register_user("Evgeny_Borodulin")
        'Пользователь Evgeny_Borodulin зарегистрирован в VK'
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username or not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        # Проверка на допустимые символы
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("Имя может содержать только буквы, цифры, _ и -")
        ...

    # Метод get_info наследуется от базового класса (не перегружен)

    def __str__(self) -> str:
        """
        Метод ПЕРЕГРУЖЕН, так как нужно отобразить количество пользователей
        """
        return f"ВКонтакте - {self._users_count} млн пользователей"

    def __repr__(self) -> str:
        """
        Метод ПЕРЕГРУЖЕН, так как нужно включить специфический атрибут
        """
        return f"{self.__class__.__name__}(name={self._name!r}, founded_year={self._founded_year!r}, country={self._country!r}, users_count={self._users_count!r})"


if __name__ == "__main__":
    doctest.testmod()