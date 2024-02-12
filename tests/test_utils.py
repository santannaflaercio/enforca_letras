import unittest
from unittest.mock import patch
from src.utils import ler_palavras


class TestUtils(unittest.TestCase):

    def test_ler_palavras_arquivo_valido(self):
        # Simulando o conteúdo do arquivo
        palavras_esperadas = ["Banana", "Maçã", "Laranja"]

        # Simulando a abertura do arquivo
        with patch("builtins.open") as mock_open:
            mock_file = mock_open.return_value
            mock_file.__enter__.return_value.readlines.return_value = palavras_esperadas

            # Chamando a função a ser testada
            palavras_lidas = ler_palavras()

            # Comparando os conjuntos
            self.assertEqual(palavras_lidas, set(palavras_esperadas))


if __name__ == "__main__":
    unittest.main()
