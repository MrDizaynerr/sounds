class Key:
    """
    name - наименование ноты
    midi_nums - список, хранящий коды ноты для разных октав, где индекс - это номер октавы, значение - номер midi
    """

    # человеческая запись ноты
    name: str
    # список с кодами для разных октав данной ноты
    midi_nums: list[int]

    def step_up_by_sub_tones_count(self, sub_tones_count: int) -> "Key":
        """
        Получить ноту на заданное количество полутонов выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] + sub_tones_count) % 12 + 12)

    def step_down_by_sub_tones_count(self, sub_tones_count: int) -> "Key":
        """
        Получить ноту на заданное количество полутонов выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] - sub_tones_count) % 12 + 12)

    def step_up_by_tone(self) -> "Key":
        """
        Получить ноту на тон выше
        """
        return self.step_up_by_sub_tones_count(2)

    def step_up_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона выше
        """
        return self.step_up_by_sub_tones_count(1)

    def step_down_by_tone(self) -> "Key":
        """
        Получить ноту на тон ниже
        """
        return self.step_down_by_sub_tones_count(2)

    def step_down_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона ниже
        """
        return self.step_up_by_sub_tones_count(1)

    def __sub__(self, other: "Key") -> int:
        """
        Получить разницу в полутонах
        """
        return self.midi_nums[0] - other.midi_nums[0]

    def __str__(self) -> str:
        return self.name

    def __init__(self, name, midi_nums: list) -> None:
        self.name = name
        self.midi_nums = midi_nums
