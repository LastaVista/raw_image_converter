import json
from typing import Any, Dict

class Config:
    def __init__(self, endian: str, byte_size: int, width: int, height: int) -> None:
        """
        コンストラクタ。

        Args:
            endian (str): エンディアンの種類。
            byte_size (int): バイトサイズ。
            width (int): 画像の幅。
            height (int): 画像の高さ。
        """
        self.endian = endian
        self.byte_size = byte_size
        self.width = width
        self.height = height

class ConfigReader:
    def read_config(self, config_file_path: str) -> Config:
        """
        指定された設定ファイルを読み込み、Configオブジェクトを返します。
        Args:
            config_file_path (str): 設定ファイルのパス。
        Returns:
            Config: 設定ファイルから読み込んだ設定を含むConfigオブジェクト。
        Raises:
            ValueError: エンディアンが 'big' または 'little' でない場合。
            ValueError: バイトサイズが 1, 2, 4, 8 のいずれかでない場合。
            ValueError: 幅が整数でないか、1未満の場合。
            ValueError: 高さが整数でないか、1未満の場合。
        """
        with open(config_file_path, 'r') as file:
            config_data: Dict[str, Any] = json.load(file)

            endian: str = config_data.get('endian', 'little')
            byte_size: int = config_data.get('byte_size', 2)
            width: int = config_data.get('width', 640)
            height: int = config_data.get('height', 480)

            if endian not in ('big', 'little'):
                raise ValueError("Invalid endian value. Must be 'big' or 'little'.")
            if byte_size not in (1, 2, 4, 8):
                raise ValueError("Invalid byte size value. Must be 1, 2, 4, or 8.")
            if not isinstance(width, int) or width < 1:
                raise ValueError("Width must be an integer and at least 1.")
            if not isinstance(height, int) or height < 1:
                raise ValueError("Height must be an integer and at least 1.")
            
            return Config(endian=endian, byte_size=byte_size, width=width, height=height)