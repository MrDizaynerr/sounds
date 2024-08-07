from data.gamma import Gamma
from data.atomic import keysenum as ke


def main0():
    g: Gamma = Gamma(ke.KeyEnum.G, True)
    print("Соль мажор: ", end="")
    print(str(g))
    print("Натуральный аккорд: " + str([str(c) for c in g.get_natural_chord()]))
    print("Септаккорд" + str([str(c) for c in g.get_cept_chord()]))
    print("Квинта: " + str([str(c) for c in g.get_quint()]))

    g = Gamma(ke.KeyEnum.G, major=False)
    print("Соль минор: ", end="")
    print(str(g))
    print("Натуральный аккорд: " + str([str(c) for c in g.get_natural_chord()]))
    print("Септаккорд: " + str([str(c) for c in g.get_cept_chord()]))
    print("Квинта: " + str([str(c) for c in g.get_quint()]))

main: list = [main0]

if __name__ == "__main__":
    selected_main: int = 0
    main[selected_main]()
