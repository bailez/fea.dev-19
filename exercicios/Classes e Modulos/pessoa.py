class Pessoa:

    def __init__(self, nome, perfil, saldo = 0, ativos = []):
        self.nome = nome
        self.perfil = perfil
        self.saldo = saldo
        self.ativos = ativos
        
    def comprar(self, item, quantidade = 1):
        preco = item.preco
        if self.saldo >= preco*quantidade:
            print(f'{self.nome} comprou {quantidade} {item.nome} e gastou um totl de $',preco*quantidade)
            self.saldo = self.saldo - preco*quantidade
            for i in range(quantidade):
                print(str(i+1), f'{item.nome} comprado com sucesso')
                self.ativos.append(item)
        else:
            print(f'{self.nome} não tem saldo suficiente para comprar {quantidade} {item.nome}')        
        
    def vender(self, item,quantidade=1):
        total_de_ativos = len(self.ativos)
        if item in self.ativos:
            for i in range(quantidade):
                for j,k in zip(self.ativos,range(total_de_ativos)):
                    if item == j:
                        self.ativos.pop(k)
                        self.saldo = self.saldo + j.retorno
                print(str(i + 1), f'{item.nome} vendido com sucesso')
        else:
            print(f'{self.nome} não possui nenhum {item.nome}')

    def verificar_saldo(self):
        print(f'{self.nome} possui ${self.saldo} em conta.')
        return self.saldo

    def verifica_saldo_final(self):
        for ativo in self.ativos:
            ativo.excecuta()
            self.vender(ativo)
        
        print(f'Saldo final de {self.nome} é de {self.saldo}')
        return self.saldo        
