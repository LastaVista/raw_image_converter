class BinaryFileReader:
    def read_binary_file(self, binary_file_path: str) -> bytes:
        """
        指定されたバイナリファイルを読み込み、その内容をバイト列として返します。

        Args:
            binary_file_path (str): 読み込むバイナリファイルのパス。

        Returns:
            bytes: ファイルの内容をバイト列として返します。
        """
        with open(binary_file_path, 'rb') as file:
            return file.read()