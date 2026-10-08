class Calcolatrice:

    def sottrai(self, a, b):
        return a - b

    def moltiplica(self, a, b):
        return a * b

    def dividi(self, a, b):
        if b == 0:
            raise ValueError("Non puoi dividere per zero")
        return a / b
    
    def somma(self, a, b):
        return a + b