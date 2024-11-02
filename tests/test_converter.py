import unittest
from converter import Converter
from config_reader import Config

class TestConverter(unittest.TestCase):
    def test_convert_little_endian(self):
        converter = Converter()
        config = Config(endian='little', byte_size=2, width=0, height=0)
        binary_data = b'\x01\x00\x02\x00'
        result = converter.convert(binary_data, config)
        self.assertEqual(result, [1, 2])

    def test_convert_big_endian(self):
        converter = Converter()
        config = Config(endian='big', byte_size=2, width=0, height=0)
        binary_data = b'\x00\x01\x00\x02'
        result = converter.convert(binary_data, config)
        self.assertEqual(result, [1, 2])

    def test_invalid_endian(self):
        converter = Converter()
        config = Config(endian='invalid', byte_size=2, width=0, height=0)
        binary_data = b'\x01\x00\x02\x00'
        with self.assertRaises(ValueError):
            converter.convert(binary_data, config)

    def test_convert_byte_size_is_1(self):
        converter = Converter()
        config = Config(endian='little', byte_size=1, width=0, height=0)
        binary_data = b'\x01\x02\x03\x04'
        result = converter.convert(binary_data, config)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_convert_byte_size_is_4(self):
        converter = Converter()
        config = Config(endian='little', byte_size=4, width=0, height=0)
        binary_data = b'\x01\x00\x00\x00\x02\x00\x00\x00'
        result = converter.convert(binary_data, config)
        self.assertEqual(result, [1, 2])

    def test_convert_byte_size_is_8(self):
        converter = Converter()
        config = Config(endian='little', byte_size=8, width=0, height=0)
        binary_data = b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'
        result = converter.convert(binary_data, config)
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    unittest.main()