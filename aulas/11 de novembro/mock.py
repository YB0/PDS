# Quando a API não está disponível mas se quer testar mesmo assim, chamar um método criado para se passar pela API;
# retorna uma resposta esperada, como se fosse a resposta que seria dada pela API.

from random import randint
def velocidade():

    return randint(40,120)
    #retorna números aleatórios entre 40 e 120;

def alerta():

    v = velocidade()
    if v < 60 or v > 100:
        
        return True
        # v fora do intervalo de velocidade aceita
    
    return False

from unittest.mock import Mock
mock_velocidade = Mock()
mock_velocidade.return_value = 70
alerta()

# Pra não precisar depender da velocidade gerar um número aleatório entre 60 e 100, cria um mock que dá sempre um valor entre esses números.
# Retorna o resultado de uma função.

