import random

from data.atomic.keysenum import KeyEnum
from gamma import Gamma
from data.atomic.key import Key


def generate_random_midi_melody_from_sequence(sequence: list[Key], minor: bool = True, max_note_shift_value: int = 10, max_notes_in_beat: int = 10) -> list[list[int]]:
    """
    генерирует простейшую мелодию в формате кодов midi из заданной последовательности аккордов
    """
    result_midi_melody: list[list[int]] = list[list[int]]()
    i: int = 0
    for key in sequence:
        notes_count: int = random.choice(range(1, max_notes_in_beat+1))
        beat: list[int] = list[int]()
        gamma_for_key: Gamma = Gamma(key.name)
        first_key_to_beat: Key = KeyEnum.by_name(
                    random.choice(
                        gamma_for_key.get_minor() if minor else gamma_for_key.get_major()
                    )
        )
        last_midi_num_from_previous_beat: int = random.choice(first_key_to_beat.midi_nums)
        if i > 0:
            min(first_key_to_beat.midi_nums, key=lambda x: abs(result_midi_melody[i - 1][len(result_midi_melody[i-1])-1] - x))
        beat.append(last_midi_num_from_previous_beat)
        for i in range(1, notes_count + 1):
            prev_midi_key: int = beat[i-1]
            prev_key: Key = KeyEnum.by_midi_num(prev_midi_key)
            next_key: Key = KeyEnum.by_name(
                gamma_for_key.get_step_from_key(
                    prev_key.name,
                    random.randint(-max_note_shift_value, max_note_shift_value)
                )
            )
            next_midi_num: int = min(next_key.midi_nums, key=lambda x: abs(x-prev_midi_key))
            beat.append(next_midi_num)
        result_midi_melody.append(beat)
        i = len(result_midi_melody)
    return result_midi_melody


class Synth:
    """
    объект, отвечающий непосредственно за генерацию мелодий
    """

    key_list: dict[str, Gamma]
    tempo: int

    def generate_random_sequence(self, key: str, minor: bool = False, tacts: int = 4, tact_size: int = 4) -> (
            list[list[str]]):
        """
        генерирует случайную последовательность аккордов в виде двумерного массива, где
        первый индекс - такт, второй - аккорд
        """
        if tacts <= 0:
            raise ValueError(f"Количество тактов ({tacts}) не может быть отрицательным!")
        if key not in self.key_list.keys():
            raise ValueError(f"Неверный номер тональности: {key}! Для данного объекта доступны: {self.key_list}")
        key: Gamma = self.key_list[key]
        key: list[str] = key.get_minor() if minor else key.get_major()
        sequence: list[list[str]] = list()
        for _ in range(tacts):
            sequence.append(
                random.choices(population=key, k=tact_size)
            )
        return sequence

    def __init__(self, keys: list[str], tempo: int = 60) -> None:
        self.key_list = {}
        self.tempo = tempo
        for key in keys:
            Gamma.check_key_valid(key)
            self.key_list[key] = Gamma(key)
