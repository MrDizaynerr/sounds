class Gamma:
    default_key: str

    _total_notes: list[str] = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B"
    ]

    @staticmethod
    def _throw_invalid_key_exception(key: str) -> None:
        raise ValueError(f"Ноты {key} не существует!")

    @staticmethod
    def _normalize_key(key: str) -> str:
        key = key.upper().replace("H", "B")
        return key

    @staticmethod
    def check_octave_valid(octave_number: int) -> None:
        if octave_number not in range(11):
            raise ValueError(f"Неверная октава: {octave_number}. Должна быть в диапазоне [0..10]")

    @staticmethod
    def check_key_valid(key: str) -> None:
        key = Gamma._normalize_key(key)
        if key not in Gamma._total_notes:
            Gamma._throw_invalid_key_exception(key)

    @staticmethod
    def get_step_from_key(key: str, step_num: int) -> str:
        key = Gamma._normalize_key(key)
        Gamma.check_key_valid(key)
        key_num: int = Gamma._total_notes.index(key)
        return Gamma._total_notes[(key_num + step_num) % len(Gamma._total_notes)]

    @staticmethod
    def generate_major_gamma(key: str) -> list[str]:
        key: str = key.upper().replace("H", "B")
        Gamma.check_key_valid(key)
        return [
            key,
            Gamma.get_step_from_key(key, 2),
            Gamma.get_step_from_key(key, 2 + 2),
            Gamma.get_step_from_key(key, 2 + 2 + 1),
            Gamma.get_step_from_key(key, 2 + 2 + 1 + 2),
            Gamma.get_step_from_key(key, 2 + 2 + 1 + 2 + 2),
            Gamma.get_step_from_key(key, 2 + 2 + 1 + 2 + 2 + 2),
            Gamma.get_step_from_key(key, 2 + 2 + 1 + 2 + 2 + 2 + 1)
        ]

    @staticmethod
    def generate_minor_gamma(key: str) -> list[str]:
        key: str = key.upper().replace("H", "B")
        Gamma.check_key_valid(key)
        return [
            key,
            Gamma.get_step_from_key(key, 2),
            Gamma.get_step_from_key(key, 2 + 1),
            Gamma.get_step_from_key(key, 2 + 1 + 2),
            Gamma.get_step_from_key(key, 2 + 1 + 2 + 2),
            Gamma.get_step_from_key(key, 2 + 1 + 2 + 2 + 1),
            Gamma.get_step_from_key(key, 2 + 1 + 2 + 2 + 2 + 2),
            Gamma.get_step_from_key(key, 2 + 1 + 2 + 2 + 2 + 2 + 2)
        ]

    def get_minor(self) -> list[str]:
        return Gamma.generate_minor_gamma(self.default_key)

    def get_major(self) -> list[str]:
        return Gamma.generate_major_gamma(self.default_key)

    def __init__(self, key: str) -> None:
        Gamma.check_key_valid(key)
        self.default_key = key

    def __str__(self) -> str:
        return f"key: {self.default_key}"
