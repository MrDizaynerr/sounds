from data.atomic import key as k


class Chord:
    """
    Хранит аккорды. В частности, ноты, которые в него входят и его название
    """
    _keys: list[k.Key]
    _name: str

    def __init__(self, keys: list[k.Key]) -> None:
        key_len: int = len(keys)
        if key_len < 2:
            raise ValueError(f"Аккорд не может состоять менее, чем из двух нот ({key_len})!")
        self._keys = keys
        self._name = keys[0].name
        if key_len > 2:
            first_second_difference: int = keys[1] - keys[0]
            if first_second_difference == 3:
                self._name += "m"
            if key_len == 4:
                third_four_difference: int = keys[3] - keys[2]
                if third_four_difference == 3:
                    self._name += "7"

    def get_keys(self):
        return self._keys

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name
