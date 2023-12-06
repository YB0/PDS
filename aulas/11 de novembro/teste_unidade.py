import unittest

def fun(x):

    return x + 1

class MyTest (unittest.TestCase):

    def test(self):

        self.assertEqual(fun(3), 4)
        #assertEqual testa se é igual

if __name__ == '__main__':

    unittest.main()

# PS C:\Users\20201214010004\PDS> python teste_unidade.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK 
# 
# Adicione -v depois do nome do arquivo e veja o que especificadamente falhou.