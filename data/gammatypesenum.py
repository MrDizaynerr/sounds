import enum


class GammaTypesEnum(enum.Enum):
    """
    Перечисление, которое хранит в себе типы гамм и информацию о смещениях тонов для каждой их ступени
    """
    # мажорная гамма
    major_gamma: dict[int, int] = {
        1: 2,
        2: 2,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 1
    }
    # минорная гамма
    minor_gamma: dict[int, int] = {
        1: 2,
        2: 1,
        3: 2,
        4: 2,
        5: 1,
        6: 2,
        7: 2
    }
