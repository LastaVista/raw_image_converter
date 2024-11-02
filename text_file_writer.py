from typing import List

from config_reader import Config

class TextFileWriter:
    def write_text_file(self, output_file_path: str, converted_data: List[str], config: Config) -> bool:
        """
        指定されたパスにテキストファイルを書き込むメソッド。
        Args:
            output_file_path (str): 出力ファイルのパス。
            converted_data (List[str]): 書き込むデータのリスト。
            config (Config): ファイル書き込みに関する設定を含むConfigオブジェクト。
        Returns:
            bool: 書き込みが成功した場合はTrue、失敗した場合はFalse。
        """
        try:
            width: int = config.width
            height: int = config.height

            with open(output_file_path, 'w', encoding='utf-8') as file:
                for i in range(height):
                    line = ','.join(converted_data[i * width:(i + 1) * width])
                    file.write(line + '\n')
            return True
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            return False