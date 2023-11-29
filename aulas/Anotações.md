**Terminal:** py -> abre o console do python (para sair, exit())

    >>> assert 3 == 4
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AssertionError
    >>> assert 3 == 3

_Isso retorna que deu erro, mas não especifica._
    
    >>> assert 3 == 2, "3 não é igual a 2"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AssertionError: 3 não é igual a 2
    >>>
_^ Especificando o erro._

## Frameworks - Teste de Código

