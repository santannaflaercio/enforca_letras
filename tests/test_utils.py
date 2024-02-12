import io
import sys
import unittest
from unittest.mock import patch, mock_open
from src.utils import ler_palavras, mostra_jogo


class TestLerPalavras(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        sys.stdout = sys.__stdout__
        
    @patch("builtins.open", new_callable=mock_open, read_data="palavra1\npalavra2\npalavra3")
    def test_ler_palavras(self, mock_file):
        expected_output = {"palavra1", "palavra2", "palavra3"}
        self.assertEqual(ler_palavras(), expected_output)

    @patch("builtins.open", new_callable=mock_open, read_data="palavra1\npalavra2\npalavra2")
    def test_ler_palavras_duplicadas(self, mock_file):
        expected_output = {"palavra1", "palavra2"}
        self.assertEqual(ler_palavras(), expected_output)

    @patch("builtins.open", side_effect=FileNotFoundError())
    def test_ler_palavras_arquivo_nao_encontrado(self, mock_file):
        ler_palavras()
        output = self.capturedOutput.getvalue().strip()
        self.assertIn("Erro: Arquivo 'palavras.txt' não encontrado.", output)


class TestMostraJogo(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_mostra_jogo(self):
        mostra_jogo("python", set("yth"), 2)
        output = self.capturedOutput.getvalue().strip()
        expected_output = "--------------------\nErros: 2\nPalavra: _yth__\nLetras usadas: h t y"
        self.assertEqual(output, expected_output)

        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

        mostra_jogo("python", set("python"), 0)
        output = self.capturedOutput.getvalue().strip()
        expected_output = "--------------------\nErros: 0\nPalavra: python\nLetras usadas: h n o p t y"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
