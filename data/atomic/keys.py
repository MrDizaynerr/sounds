from data.atomic.keys_enum import KeyEnum


class Key:
    """
    name - наименование ноты
    midi_nums - список, хранящий коды ноты для разных октав, где индекс - это номер октавы, значение - номер midi
    """

    name: str
    midi_nums: list[int]

    def step_up_by_tone(self) -> "Key":
        """
        Получить ноту на тон выше
        """
        return KeyEnum.by_midi_num((self.midi_nums[0] + 2) % 7)

    def step_up_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона выше
        """
        return KeyEnum.by_midi_num((self.midi_nums[0] + 1) % 7)

    def step_down_by_tone(self) -> "Key":
        """
        Получить ноту на тон выше
        """
        return KeyEnum.by_midi_num((self.midi_nums[0] - 2) % 7)

    def step_down_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона выше
        """
        return KeyEnum.by_midi_num((self.midi_nums[0] - 1) % 7)

    def __sub__(self, other: "Key") -> int:
        """
        Получить разницу в полутонах
        """
        return self.midi_nums[0] - other.midi_nums[0]

    def __init__(self, name, midi_nums: list) -> None:
        self.name = name
        self.midi_nums = midi_nums
