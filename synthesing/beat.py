from data.atomic import key as k
from data import gamma as g


class Beat:
    """
    Тип, представляющий собой долю в такте.
    Хранит ноты, которые должны во время доли быть сыграны и информацию о положении в такте.
    """
    # ноты
    _keys: list[k.Key]
    # положение доли в такте
    _position: float

    def in_gamma(self, gamma: g.Gamma) -> tuple[bool, k.Key | None]:
        """
        Проверяет, все ли ноты такта принадлежат заданной гамме
        TODO: надо бы переработать это. Потому что сейчас оно точно не покрывает все случаи. Те же септы тут упадут в False. Или я просто чего то не понимаю
        """
        for key in self._keys:
            if key not in gamma.get_key_list():
                return False, key
        return True, None

    def get_position(self) -> float:
        """
        # получает положение доли в такте
        """
        return self._position

    def __init__(self, keys: list[k.Key], position: float) -> None:
        """
        :keys - может быть как одиночной нотой, так и аккордом
        """
        self._keys = keys
        self._position = position
