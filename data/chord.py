from data.atomic import key as k


class Chord:
    """
    Хранит аккорды. В частности, ноты, которые в него входят и его название
    """
    keys: list[k.Key]
    name: str

    def __init__(self, keys: list[k.Key]) -> None:
        key_len: int = len(keys)
        if key_len < 2:
            raise ValueError(f"Аккорд не может состоять менее, чем из двух нот ({key_len})!")
        self.keys = keys
        self.name = keys[0].name
        if key_len == 3:
            if keys[1] - keys[0] == 3:
                self.name += "m"

    def __str__(self):
        return self.name
