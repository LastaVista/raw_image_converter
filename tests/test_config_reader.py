import unittest
import json
import os
from config_reader import ConfigReader, Config

class TestConfigReader(unittest.TestCase):
    def setUp(self):
        # テスト用の設定ファイルを作成します。
        self.test_file_path = 'test_config.json'
        config_data = {
            "endian": "little",
            "byte_size": 4,
            "width": 1920,
            "height": 1080
        }
        with open(self.test_file_path, 'w') as file:
            json.dump(config_data, file)

    def tearDown(self):
        # テスト用の設定ファイルを削除します。
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_config(self):
        reader = ConfigReader()
        config = reader.read_config(self.test_file_path)
        self.assertEqual(config.endian, "little")
        self.assertEqual(config.byte_size, 4)
        self.assertEqual(config.width, 1920)
        self.assertEqual(config.height, 1080)

    def test_invalid_endian(self):
        # 無効なエンディアンを含む設定ファイルを作成します。
        invalid_config_data = {
            "endian": "invalid",
            "byte_size": 4,
            "width": 1920,
            "height": 1080
        }
        with open(self.test_file_path, 'w') as file:
            json.dump(invalid_config_data, file)

        reader = ConfigReader()
        with self.assertRaises(ValueError):
            reader.read_config(self.test_file_path)

    def test_invalid_byte_size(self):
        # 無効なバイトサイズを含む設定ファイルを作成します。
        invalid_config_data = {
            "endian": "little",
            "byte_size": 3,
            "width": 1920,
            "height": 1080
        }
        with open(self.test_file_path, 'w') as file:
            json.dump(invalid_config_data, file)

        reader = ConfigReader()
        with self.assertRaises(ValueError):
            reader.read_config(self.test_file_path)

    def test_invalid_width(self):
        # 無効な幅を含む設定ファイルを作成します。
        invalid_config_data = {
            "endian": "little",
            "byte_size": 4,
            "width": 0,
            "height": 1080
        }
        with open(self.test_file_path, 'w') as file:
            json.dump(invalid_config_data, file)

        reader = ConfigReader()
        with self.assertRaises(ValueError):
            reader.read_config(self.test_file_path)

    def test_invalid_height(self):
        # 無効な高さを含む設定ファイルを作成します。
        invalid_config_data = {
            "endian": "little",
            "byte_size": 4,
            "width": 1920,
            "height": -1
        }
        with open(self.test_file_path, 'w') as file:
            json.dump(invalid_config_data, file)

        reader = ConfigReader()
        with self.assertRaises(ValueError):
            reader.read_config(self.test_file_path)
            
if __name__ == '__main__':
    unittest.main()