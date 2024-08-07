from data.atomic import key as k
from data.atomic import keysenum as ke


class Gamma:
    """
    Хранит данные о конкретной гамме
    """

    # тональность
    key: k.Key
    # мажорность. True - мажорная гамма, False - минорная гамма 
    major: bool
    
    # хранит словарь, где ключ - ступень, значение - смещение на количество тонов для мажорной гаммы
    MAJOR_STEPS: dict[int, bool] = {
        1: True,
        2: True,
        3: False,
        4: True,
        5: True,
        6: True,
        7: False
    }
    
    # хранит словарь, где ключ - ступень, значение - смещение на: True - тон, False - полтона
    MINOR_STEPS: dict[int, bool] = {
        1: True,
        2: False,
        3: True,
        4: True,
        5: False,
        6: True,
        7: True
    }
    
    def get_natural_chord(self) -> list[k.Key]:
        return [self.get_step(0), self.get_step(2), self.get_step(4)]
    
    def get_cept_chord(self) -> list[k.Key]:
        return [self.get_step(0), self.get_step(2), self.get_step(4), self.get_step(6)]
        
    
    def get_step(self, step: int) -> k.Key:
        """
        Возвращает выбранную ступень гаммы
        """
        if step in range(8):
            if not step:
                return self.key
            current_step: k.Key = self.key
            for i in range(1, step + 1):
                steps_type: list[int] = Gamma.MAJOR_STEPS if self.major else Gamma.MINOR_STEPS
                current_step = current_step.step_up_by_tone() if steps_type[i] else current_step.step_up_by_half_tone()
            return current_step
        else:
            raise ValueError(f"Ступень {step} должна быть в диапазоне от 1 до 7")
            
    def get_full_gamma(self):
        key_list: list[k.Key] = []
        for i in range(8):
            step: k.Key = self.get_step(i)
            key_list.append(step)
        return key_list
            
    def __str__(self) -> str:
        return str([str(key_item) for key_item in self.get_full_gamma()])
    
    def __init__(self, key: k.Key | ke.KeyEnum, major: bool = False) -> None:
        self.key = key if type(key) == k.Key else key.value
        self.major = major
