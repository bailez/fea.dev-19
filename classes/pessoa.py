class Pessoa():

    def __init__(self, nome, idade, nacionalidade, genero,saldo):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.saldo = saldo

    def mostra_saldo(self):
        if self.nacionalidade == 'br':
            print('Seja bem vind{}, {}! Seu saldo é ${}!'.format('o' if self.genero == 'M' else 'a',self.nome,self.saldo))
        else:
            print('Welcome {}! Your balance is ${}!'.format(self.nome,self.saldo))
    
    def calcula_seguro(self):
        mensalidade = 200
        if self.genero == 'M':
            mensalidade =+ 10
        if self.idade < 30 and self.idade > 70:
            mensalidade =+ 50
        if self.saldo < 10000:
            mensalidade =+ 20
        return mensalidade

    def mostra_seguro(self):
        if self.nacionalidade == 'br':
            print('Sua mensalidade é de ${}'.format(self.calcula_seguro()))
        else:
            print('Your monthly payment is ${}'.format(self.calcula_seguro()))
        