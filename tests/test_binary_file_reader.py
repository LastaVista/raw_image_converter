import unittest
from binary_file_reader import BinaryFileReader

class TestBinaryFileReader(unittest.TestCase):
    def setUp(self):
        # テスト用のバイナリファイルを作成します。
        self.test_file_path = 'test_binary_file.bin'
        with open(self.test_file_path, 'wb') as file:
            file.write(b'\x00\x01\x02\x03')

    def tearDown(self):
        # テスト用のバイナリファイルを削除します。
        import os
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_binary_file(self):
        reader = BinaryFileReader()
        data = reader.read_binary_file(self.test_file_path)
        self.assertEqual(data, b'\x00\x01\x02\x03')

if __name__ == '__main__':
    unittest.main()