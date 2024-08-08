from data.atomic import key as k
from data.atomic import keysenum as ke
from data import gammatypesenum as ge


class Gamma:
    """
    Хранит данные о конкретной гамме
    """

    # тональность
    _key: k.Key
    # мажорность. True - мажорная гамма, False - минорная гамма 
    _gamma_type: ge.GammaTypesEnum
    # все ноты тональности
    _key_list: list[k.Key]

    def get_natural_chord(self) -> list[k.Key]:
        """
        Получает натуральный аккорд
        """
        return [self.get_step(0), self.get_step(2), self.get_step(4)]

    def get_cept_chord(self) -> list[k.Key]:
        """
        Получает септаккорд
        """
        return [self.get_step(0), self.get_step(2), self.get_step(4), self.get_step(6)]

    def get_quint(self) -> list[k.Key]:
        """
        Получает квинту
        """
        return [self.get_step(0), self.get_step(4)]

    def get_step(self, step: int) -> k.Key:
        """
        Возвращает выбранную ступень гаммы
        TODO: надо бы сделать его рекурсивным, но мне пока лень
        """
        if step in range(8):
            if not step:
                return self._key
            current_step: k.Key = self._key
            steps_type: dict[int, int] = self._gamma_type.value
            for i in range(1, step + 1):
                current_step = current_step.step_up_by_sub_tones_count(steps_type[i])
            return current_step
        else:
            raise ValueError(f"Ступень {step} должна быть в диапазоне от 1 до 7")

    def get_key_list(self) -> list[k.Key]:
        """
        Получает всю гамму
        """
        return self._key_list

    def get_key(self) -> k.Key:
        """
        Получает тональность гаммы
        """
        return self._key

    def is_major(self) -> bool:
        """
        Является ли гамма мажорной или минорной
        TODO: заменить на перечисление для разного рода ладов, а пока обходимся натурой
        """
        return self.is_major()

    def _generate_full_gamma(self) -> None:
        """
        Генерирует и сохраняет все ноты для данной гаммы
        """
        key_list: list[k.Key] = []
        for i in range(8):
            step: k.Key = self.get_step(i)
            key_list.append(step)
        self._key_list = key_list

    def __str__(self) -> str:
        return str([str(key_item) for key_item in self.get_key_list()])

    def __init__(self, key: k.Key | ke.KeyEnum, major: ge.GammaTypesEnum = ge.GammaTypesEnum.major_gamma) -> None:
        self._key = key if type(key) is k.Key else key.value
        self._gamma_type = major
        self._generate_full_gamma()
