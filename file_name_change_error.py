# 目的のファイルの拡張子名を指定してディレクトリ内にあるファイル名を一括変更するプログラム

# globモジュールのglob()関数を使用
# globモジュールはディレクトリ内で指定した拡張子のファイルを返す
import glob

# ファイル、ディレクトリのパス操作を行うためにosモジュールを使用
import os

# input()関数を使用して一括変更したいファイルの拡張子名を指定
extension = input("一括変更したいファイルの拡張子名の入力（例）テキストファイルの場合は「txt」⇒ ")

# input()関数を使用して新しいファイル名の入力
enter_new_name = input("新しいファイル名の入力 ⇒ ")

# 拡張子名を指定したファイルを"files"と命名
files = glob.glob("*." + extension)

# enumerate()関数を使用して"files"にインデックス番号を設定して抽出
for i, old_name in enumerate(files):

    # 新しいファイル名の決定
    # 新しいファイル名に「_001」などと番号をつけるために"_{0:03d}"を追加
    new_name = enter_new_name + "_{0:03d}." + extension.format(i + 1)

    # ファイル名の変更
    os.rename(old_name, new_name)

    # 変更の表示
    print(old_name + " ⇒ " + new_name)

# enterキーでコマンドプロンプトを終了
input()
