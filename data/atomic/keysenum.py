import enum
from data.atomic import key


class KeyEnum(enum.Enum):
    """
    Перечисление, хранящее все ноты
    """

    C = key.Key(
        "C",
        [
            12,
            24,
            36,
            48,
            60,
            72,
            84
        ]
    )
    Cd = key.Key(
        "C#",
        [
            13,
            25,
            37,
            49,
            61,
            73,
            85
        ]
    )
    D = key.Key(
        "D",
        [
            14,
            26,
            38,
            50,
            62,
            74,
            86
        ]
    )
    Dd = key.Key(
        "D#",
        [
            15,
            27,
            39,
            51,
            63,
            75,
            87
        ]
    )
    E = key.Key(
        "E",
        [
            16,
            28,
            40,
            52,
            64,
            76,
            88
        ]
    )
    F = key.Key(
        "F",
        [
            17,
            29,
            41,
            53,
            65,
            77,
            89
        ]
    )
    Fd = key.Key(
        "F#",
        [
            18,
            30,
            42,
            54,
            66,
            78,
            90
        ]
    )
    G = key.Key(
        "G",
        [
            19,
            31,
            43,
            55,
            67,
            79,
            91
        ]
    )
    Gd = key.Key(
        "G#",
        [
            20,
            32,
            44,
            56,
            68,
            80,
            92
        ]
    )
    A = key.Key(
        "A",
        [
            21,
            33,
            45,
            57,
            69,
            81,
            93
        ]
    )
    Ad = key.Key(
        "A#",
        [
            22,
            34,
            46,
            58,
            70,
            82,
            94
        ]
    )
    B = key.Key(
        "B",
        [
            23,
            35,
            47,
            59,
            71,
            83,
            95
        ]
    )

    @staticmethod
    def by_midi_num(midi_num: int) -> key.Key | None:
        """
        Получение экземпляра ноты по её midi номеру
        """
        for key_item in KeyEnum:
            if midi_num in key_item.value.midi_nums:
                return key_item.value
        return None

    @staticmethod
    def by_name(key_name: str) -> key.Key | None:
        """
        Получение экземпляра ноты по её названию
        """
        for key_item in KeyEnum:
            if key_item.value.name == key_name:
                return key_item.value
        return None
