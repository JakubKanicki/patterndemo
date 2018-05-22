from core import Core
from engine import Engine


def main():
    core = Core()
    engine = Engine(core)
    engine.run()


if __name__ == '__main__':
    main()
