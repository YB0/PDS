import unittest
from unittest.mock import Mock
import odometria_mock

class TestOdometria(unittest.TestCase):

    def test_alerta_normal(self):

        odometria_mock.velocidade = Mock()
        odometria_mock.velocidade.return_value = 70
        self.assertFalse(odometria_mock.alerta())

    def test_alerta_velocidade_alta(self):

        odometria_mock.velocidade = Mock()
        odometria_mock.velocidade.return_value = 101
        self.assertTrue(odometria_mock.alerta())

    def test_alerta_velocidade_baixa(self):

        odometria_mock.velocidade = Mock()
        odometria_mock.velocidade.return_value = 59
        self.assertTrue(odometria_mock.alerta())

#python -m unittest odometria_unittest.py -v