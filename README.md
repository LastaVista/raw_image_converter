# Raw Image Converter

## 概要
Raw Image Converterは、バイナリファイルを指定された設定に基づいて数値に変換し、CSV形式でテキストファイルに出力するツールです。バイナリファイルはRaw画像を想定しており，出力される数値は２次元に配置されます．

## 特徴
- バイナリファイルの読み込み
- 指定されたエンディアンとバイトサイズに基づくデータ変換
- 変換されたデータをテキストファイルとして出力

## インストール
raw_image_conveter.exeをダウンロードします．

## 使い方
以下のコマンドを実行します．  
raw_image_conveter.exe \<config_file_path> \<binary_file_path> \<output_file_path>
- config_file_path: 設定ファイルのパス
- binary_file_path: バイナリファイルのパス
- output_file_path: テキストファイルの出力先

```sh
raw_image_converter.exe .\config.json .\image.raw .\output.csv
```

### 設定ファイルの書き方
設定ファイルは，json形式で記述します．

```json
{
    "endian": "little",
    "byte_size": 2, 
    "width": 1920,
    "height": 1080
}
```
- endian: "little"=リトルエンディアン，"big"=ビッグエンディアン．
- byte_size: １画素あたりのバイト数．1, 2, 4, または8．
- width: 画像の幅．1以上．テキストファイルには，1行あたりwidth個の数値が出力されます．
- height: 画像の高さ．1以上．テキストファイルには，height行が出力されます．