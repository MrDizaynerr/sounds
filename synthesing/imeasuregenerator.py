from abc import ABC, abstractmethod


class IMeasureGenerator(ABC):
    """
    Размер такта в битах
    """
    _size: int

    @abstractmethod
    def generate_tact(self):
        """
        Генерирует целый такт нужного размера
        """
        pass

    @abstractmethod
    def _generate_keys_weights(self, sub_beats_count: int) -> list[float]:
        """
        Генерирует кривую экспрессии, которая задаёт, в общем смысле,
        насколько много нот и будет в каждой доле такта.
        :sub_beats_count количество долей, для которых будет вестись расчёт
        :return последовательность чисел размером с количество долей, значения которых в пределах от 0 до 1
        """
        return [.5 for _ in range(sub_beats_count)]

    def __init__(self, size: int):
        self._size = size
