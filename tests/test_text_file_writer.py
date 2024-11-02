import unittest
import os
from text_file_writer import TextFileWriter
from config_reader import Config

class TestTextFileWriter(unittest.TestCase):
    def setUp(self):
        # テスト用の出力ファイルパスを設定します。
        self.test_file_path = 'test_output.txt'

    def tearDown(self):
        # テスト用の出力ファイルを削除します。
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_write_text_file(self):
        writer = TextFileWriter()
        config = Config(endian='little', byte_size=2, width=2, height=2)
        converted_data = [1, 2, 3, 4]
        success = writer.write_text_file(self.test_file_path, converted_data, config)
        self.assertTrue(success)

        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertEqual(content, '1,2\n3,4\n')

    def test_write_text_file_with_invalid_path(self):
        writer = TextFileWriter()
        config = Config(endian='little', byte_size=2, width=2, height=2)
        converted_data = [1, 2, 3, 4]
        # 無効なパスを指定して書き込みが失敗することを確認します。
        success = writer.write_text_file('/invalid_path/test_output.txt', converted_data, config)
        self.assertFalse(success)

    def test_write_text_file_with_extra_data(self):
        writer = TextFileWriter()
        config = Config(endian='little', byte_size=2, width=2, height=2)
        converted_data = [1, 2, 3, 4, 5, 6]
        success = writer.write_text_file(self.test_file_path, converted_data, config)
        self.assertTrue(success)

        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertEqual(content, '1,2\n3,4\n')

    def test_write_text_file_with_insufficient_data(self):
        writer = TextFileWriter()
        config = Config(endian='little', byte_size=2, width=2, height=2)
        converted_data = [1, 2, 3]
        success = writer.write_text_file(self.test_file_path, converted_data, config)
        self.assertTrue(success)

        with open(self.test_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertEqual(content, '1,2\n3\n')

if __name__ == '__main__':
    unittest.main()