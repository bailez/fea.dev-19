from gerenciador import Gerenciador,Pessoa,Ativo

ntnb =  Ativo('ntnb',100,5,120)
petro = Ativo('petro',50,40,100)
apple = Ativo('apple', 80,30,140)
debtr = Ativo('debtr',20,10,30)
bitcoin = Ativo('btc',40,80,4000)
ativos = [ntnb,petro,apple,debtr,bitcoin]

manzi = Pessoa('Manzi','m',1000)
bailao = Pessoa('Bailão','r',680)
tiagod = Pessoa('Tiagod','a',640)
lott = Pessoa('Lott','m', 850)
nich = Pessoa('Nicholson','r',740)
pessoas = [manzi,bailao,tiagod,lott,nich]

bailao.verificar_saldo()

"""
for i in pessoas:
    for j in ativos:
        recomenda = Gerenciador().indica_ativo(i,j)
        if recomenda:
            i.comprar(j)
"""

bailao.comprar(bitcoin)
bailao.verificar_saldo()
bailao.verifica_saldo_final()

