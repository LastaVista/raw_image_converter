import unittest
from unittest.mock import patch, MagicMock
from raw_image_converter import RawImageConverter
from config_reader import Config

class TestRawImageConverter(unittest.TestCase):
    def setUp(self):
        self.converter = RawImageConverter()

    @patch('config_reader.ConfigReader.read_config')
    @patch('binary_file_reader.BinaryFileReader.read_binary_file')
    @patch('converter.Converter.convert')
    @patch('text_file_writer.TextFileWriter.write_text_file')
    def test_execute_program(self, mock_write_text_file, mock_convert, mock_read_binary_file, mock_read_config):
        # モックの設定
        mock_read_config.return_value = Config(endian='little', byte_size=2, width=2, height=2)
        mock_read_binary_file.return_value = b'\x01\x00\x02\x00'
        mock_convert.return_value = ['1', '2', '3', '4']
        mock_write_text_file.return_value = True

        # テスト対象メソッドの実行
        result = self.converter.execute_program('config.json', 'binary_file.bin', 'output.txt')

        # アサーション
        self.assertTrue(result)
        mock_read_config.assert_called_once_with(config_file_path='config.json')
        mock_read_binary_file.assert_called_once_with(binary_file_path='binary_file.bin')
        mock_convert.assert_called_once_with(binary_data=b'\x01\x00\x02\x00', config=mock_read_config.return_value)
        mock_write_text_file.assert_called_once_with(output_file_path='output.txt', converted_data=['1', '2', '3', '4'], config=mock_read_config.return_value)

    @patch('config_reader.ConfigReader.read_config')
    @patch('binary_file_reader.BinaryFileReader.read_binary_file')
    @patch('converter.Converter.convert')
    @patch('text_file_writer.TextFileWriter.write_text_file')
    def test_execute_program_failure(self, mock_write_text_file, mock_convert, mock_read_binary_file, mock_read_config):
        # モックの設定
        mock_read_config.return_value = Config(endian='little', byte_size=2, width=2, height=2)
        mock_read_binary_file.return_value = b'\x01\x00\x02\x00'
        mock_convert.return_value = ['1', '2', '3', '4']
        mock_write_text_file.return_value = False

        # テスト対象メソッドの実行
        result = self.converter.execute_program('config.json', 'binary_file.bin', 'output.txt')

        # アサーション
        self.assertFalse(result)
        mock_read_config.assert_called_once_with(config_file_path='config.json')
        mock_read_binary_file.assert_called_once_with(binary_file_path='binary_file.bin')
        mock_convert.assert_called_once_with(binary_data=b'\x01\x00\x02\x00', config=mock_read_config.return_value)
        mock_write_text_file.assert_called_once_with(output_file_path='output.txt', converted_data=['1', '2', '3', '4'], config=mock_read_config.return_value)

if __name__ == '__main__':
    unittest.main()