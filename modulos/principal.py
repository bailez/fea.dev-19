""" 
Para termos as funções e métodos de outro módulo devemos importar o módulo e desta forma conseguimos executar 
"""
import exemplo

exemplo.mensagem()

"""
É possível também apenas importar uma função específica do modulo usando a seguinte sintaxe,
 seguindo esta lógica é possível executar a função de um módulo diretamente sem precisar chamar o módulo antes ao longo do script
"""

from exemplo import mensagem

mensagem()

"""
Para utilizar o módulo ou função com outro nome podemos fazer da sguinte forma:
"""

import exemplo as ex

ex.mensagem()

from exemplo import mensagem as msg

msg()

""" 
Podemos também importar todos as funções presentes dentro de um módulo usando '*':
"""

from exemplo import *

mensagem()
print(soma(4,5))