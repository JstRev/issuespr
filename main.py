from calcolatrice import Calcolatrice


def main():
    calc = Calcolatrice()

    print("Sottrazione:", calc.sottrai(10, 3))
    print("Moltiplicazione:", calc.moltiplica(10, 3))
    print("Divisione:", calc.dividi(10, 2))


if __name__ == "__main__":
    main()