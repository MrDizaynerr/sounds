class Key:
    """
    name - наименование ноты
    midi_nums - список, хранящий коды ноты для разных октав, где индекс - это номер октавы, значение - номер midi
    """

    # человеческая запись ноты
    name: str
    # список с кодами для разных октав данной ноты
    midi_nums: list[int]

    def step_up_by_tone(self) -> "Key":
        """
        Получить ноту на тон выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] + 2) % 12 + 12)

    def step_up_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] + 1) % 12 + 12)

    def step_down_by_tone(self) -> "Key":
        """
        Получить ноту на тон выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] - 2) % 12 + 12)

    def step_down_by_half_tone(self) -> "Key":
        """
        Получить ноту на полтона выше
        """
        from data.atomic import keysenum as ke
        return ke.KeyEnum.by_midi_num((self.midi_nums[0] - 1) % 12 + 12)

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
