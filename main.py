NB_JEU = 2


class Carte:
    def __init__(self, carte, valeur):
        self.carte = carte
        self.valeur = valeur
        self.reset_counter()

    def __str__(self):
        return "(" + self.carte + " | " + str(self.counter) + ") -> " + str(self.proba()) + "%"

    def reset_counter(self):
        self.counter = 4 * NB_JEU

    def decremente(self):
        if self.counter == 0:
            print("il n'y a plus de carte BG")
            return
        self.counter -= 1
        BJ.TOTAL -= 1

    def proba(self):
        return truncate(self.counter * 100 / BJ.TOTAL, 2)

    @staticmethod
    def probabilite(cartes):
        res = 0

        for x in cartes:
            res += x.counter

        return truncate(res * 100 / BJ.TOTAL, 2)


class BJ:
    TOTAL = 52 * NB_JEU

    cor = {
        "As": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "10": 9,
        "J": 10,
        "Q": 11,
        "K": 12
    }

    def __init__(self):
        self.cartes = []
        self.cartes.append(Carte("As", 1))
        self.cartes.append(Carte("2", 2))
        self.cartes.append(Carte("3", 3))
        self.cartes.append(Carte("4", 4))
        self.cartes.append(Carte("5", 5))
        self.cartes.append(Carte("6", 6))
        self.cartes.append(Carte("7", 7))
        self.cartes.append(Carte("8", 8))
        self.cartes.append(Carte("9", 9))
        self.cartes.append(Carte("10", 10))
        self.cartes.append(Carte("J", 10))
        self.cartes.append(Carte("Q", 10))
        self.cartes.append(Carte("K", 10))

    def __str__(self):
        res = ""
        for x in range(0, 9):
            res += self.cartes[x].__str__() + "\n"
        pb_10 = Carte.probabilite([x for x in self.cartes if x.valeur == 10])
        res += "(10 | " + str(self.nb_carte(10)) + ") -> " + str(pb_10) + "%\n"
        pb_10 /= 100
        pb_10 *= self.cartes[0].proba()

        res += "(BJ | XX) -> " + str(truncate(pb_10, 2)) + "%"
        return res

    def decremente(self, carte):
        if carte not in self.cor.keys():
            return
        self.cartes[self.cor[carte]].decremente()

    def nb_carte(self, p):
        res = 0
        for x in self.cartes:
            if x.valeur == p:
                res += x.counter
        return res


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return float('.'.join([i, (d + '0' * n)[:n]]))


if __name__ == "__main__":
    board = BJ()

    while True:
        print(board)
        print("quelle carte veux tu enlever ?\nAs\n1\n...\nK")
        c = input("Carte : ")
        if c == 'r':
            for x in board.cartes:
                x.reset_counter()
        board.decremente(c)
