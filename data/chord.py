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
        if key_len > 2:
            first_second_difference: int = keys[1] - keys[0]
            if first_second_difference == 3:
                self.name += "m"
            if key_len == 4:
                third_four_difference: int = keys[3] - keys[2]
                if third_four_difference == 3:
                    self.name += "7"

    def __str__(self):
        return self.name
