from data.gamma import Gamma
from data.atomic import keysenum as ke


def main0():
    g: Gamma = Gamma(ke.KeyEnum.C, True)
    print(str(g))
    print(g.get_step(0))
    print([str(c) for c in g.get_natural_chord()])
    print([str(c) for c in g.get_cept_chord()])

main: list = [main0]

if __name__ == "__main__":
    selected_main: int = 0
    main[selected_main]()
