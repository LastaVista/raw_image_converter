from typing import List

from config_reader import Config

class Converter:
    def convert(self, binary_data: bytes, config: Config) -> List[int]:
        """
        バイナリデータを指定されたエンディアンとバイトサイズで整数のリストに変換します。

        Args:
            binary_data (bytes): 変換するバイナリデータ。
            config (Config): 変換に関する設定を含むConfigオブジェクト。

        Returns:
            List[int]: 変換された整数のリスト。

        Raises:
            ValueError: 無効なエンディアンタイプが指定された場合。
        """
        result: List[int] = []
        for i in range(0, len(binary_data), config.byte_size):
            chunk = binary_data[i:i + config.byte_size]
            if config.endian == 'little':
                result.append(int.from_bytes(chunk, byteorder='little', signed=False))
            elif config.endian == 'big':
                result.append(int.from_bytes(chunk, byteorder='big', signed=False))
            else:
                raise ValueError("Invalid endian type. Use 'little' or 'big'.")
        return result