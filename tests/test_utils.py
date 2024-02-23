import io
import unittest
from unittest.mock import patch, mock_open

from src.utils import read_words, display_game


class TestUtils(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="word1\nword2\nword3")
    def test_read_words(self, mock_file):
        self.assertEqual(read_words(), {"word1", "word2", "word3"})

    @patch("builtins.open", new_callable=mock_open, read_data="word1\nword2\nword2")
    def test_read_words_duplicates(self, mock_file):
        self.assertEqual(read_words(), {"word1", "word2"})

    @patch("builtins.open", side_effect=FileNotFoundError())
    def test_read_words_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            read_words()

    def test_display_game(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            display_game("word", ["w", "o"], 1)
            self.assertEqual(fake_out.getvalue().strip(), "\n".join([
                "--------------------",
                "Mistakes: 1",
                "Word: wo__",
                "Used letters: o w"
            ]))


if __name__ == "__main__":
    unittest.main()
