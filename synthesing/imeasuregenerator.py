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

    def __init__(self, size: int):
        self._size = size
