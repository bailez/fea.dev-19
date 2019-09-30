import random
class Ativo:
    def __init__(self, nome, preco, risco, retorno):
        self.nome = nome
        self.preco = preco
        self.risco = risco
        self.retorno = retorno
        if (risco > 100) or (risco < 0):
            raise ValueError('Risco deve ser um valor entre 0 e 1')

    def excecuta(self):
        sorteio = random.randint(0,100)
        if sorteio <= self.risco:
            print(f'Investimento em {self.nome} foi perdido')
            self.retorno = 0
        else:
            print(f'Investimento em {self.nome} funcionou!')