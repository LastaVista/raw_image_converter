from config_reader import ConfigReader
from binary_file_reader import BinaryFileReader
from converter import Converter
from text_file_writer import TextFileWriter

class RawImageConverter:
    def __init__(self):
        self.config_reader = ConfigReader()
        self.binary_file_reader = BinaryFileReader()
        self.converter = Converter()
        self.text_file_writer = TextFileWriter()

    def execute_program(self, config_file_path, binary_file_path, output_file_path):
        config = self.config_reader.read_config(config_file_path=config_file_path)
        binary_data = self.binary_file_reader.read_binary_file(binary_file_path=binary_file_path)
        converted_data = self.converter.convert(binary_data=binary_data, config=config)
        success = self.text_file_writer.write_text_file(output_file_path=output_file_path, converted_data=converted_data, config=config)
        return success

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python main.py <configFilePath> <binaryFilePath> <outputFilePath>")
        sys.exit(1)

    config_file_path = sys.argv[1]
    binary_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    raw_image_converter = RawImageConverter()
    result = raw_image_converter.execute_program(config_file_path, binary_file_path, output_file_path)
    if result:
        print("File conversion successful.")
    else:
        print("File conversion failed.")