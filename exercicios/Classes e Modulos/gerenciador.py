from pessoa import Pessoa
from ativo import Ativo

class Gerenciador:

    
    
    def indica_ativo(self, pessoa, ativo):
        perfil = pessoa.perfil
        risco = ativo.risco
        # m para moderado
        if perfil == 'm':
            if risco > 25 and risco <75:
                print(f'O ativo {ativo.nome} é recomendado para {pessoa.nome}')
                pessoa.comprar(ativo,1)
            else:
                print(f'O ativo {ativo.nome} não é recomendado para {pessoa.nome}')
        # r para arriscador
        elif perfil == 'r':
            if risco <75:
                print(f'O ativo {ativo.nome} é recomendado para {pessoa.nome}')
                pessoa.comprar(ativo,1)
            else:
                print(f'O ativo {ativo.nome} não é recomendado para {pessoa.nome}')
            
        # a para avesso o risco
        elif perfil == 'a':
            if risco > 25:
                print(f'O ativo {ativo.nome} é recomendado para {pessoa.nome}')
                pessoa.comprar(ativo,1)
            else:
                print(f'O ativo {ativo.nome} não é recomendado para {pessoa.nome}')
        else:
            print(f'{pessoa.nome} não possui perfil valido')