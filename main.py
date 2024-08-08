from data.gamma import Gamma
from data import chord as c
from data.atomic import key as k
from data.atomic import keysenum as ke
from data import gammatypesenum as ge


# проверка гамм
def main0() -> None:
    g: Gamma = Gamma(ke.KeyEnum.C, ge.GammaTypesEnum.major_gamma)
    print("До мажор: ", end="")
    print(str(g))
    print("Натуральный аккорд: " + str([str(c) for c in g.get_natural_chord()]))
    print("Септаккорд: " + str([str(c) for c in g.get_cept_chord()]))
    print("Квинта: " + str([str(c) for c in g.get_quint()]))

    g = Gamma(ke.KeyEnum.C, major=ge.GammaTypesEnum.minor_gamma)
    print("До минор: ", end="")
    print(str(g))
    print("Натуральный аккорд: " + str([str(c) for c in g.get_natural_chord()]))
    print("Септаккорд: " + str([str(c) for c in g.get_cept_chord()]))
    print("Квинта: " + str([str(c) for c in g.get_quint()]))


# проверка аккордов
def main1() -> None:
    chord_c_keys: list[k.Key] = [
        ke.KeyEnum.C.value,
        ke.KeyEnum.Dd.value,
        ke.KeyEnum.G.value,
        ke.KeyEnum.Ad.value
    ]
    chord_c: c.Chord = c.Chord(chord_c_keys)
    print(f"Аккорд: {chord_c}")


main: list = [main0, main1]

if __name__ == "__main__":
    selected_main: int = 0
    main[selected_main]()
