from synthesing import beat as b
from data import gamma as g
from data.atomic import key as k


class Measure:
    """
    Класс хранит данные о такте - их количество, bpm, биты, тональность
    """
    # список битов, составляющих такт
    _beats: list[b.Beat]
    # удары в минуту для данного такта
    _bpm: int
    # размер такта
    _size: int
    # тональность
    _gamma: g.Gamma

    def _validate_beats(self, beats: list[b.Beat], size: int) -> None:
        """
        Проверяет, что все переданные биты не выходят за рамки такта, а ноты не выходят за пределы тональности
        """
        for beat in beats:
            beat_position: float = beat.get_position()
            if beat_position < 0 or beat_position >= size:
                raise ValueError(
                    f"Положение бита (бит {beats.index(beat)}: {beat}) должно быть в пределах размера такта: [0 {size})"
                )
            beat_is_in_gamma: tuple[bool, k.Key | None] = beat.in_gamma(self._gamma)
            if not beat_is_in_gamma[0]:
                raise ValueError(f"Нота {beat} не принадлежит тональности {self._gamma.get_key()}")

    def __init__(self, beats: list[b.Beat], bpm: int, size: int, gamma: g.Gamma) -> None:
        self._gamma = gamma
        self._validate_beats(beats, size)

        self._beats = beats
        self._bpm = bpm
        self._size = size
