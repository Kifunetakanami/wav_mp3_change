# globモジュールのglob()関数を使用
# globモジュールはディレクトリ内で指定した拡張子のファイルを返す
import glob

# ファイル、ディレクトリのパス操作を行うためにosモジュールを使用
import os

# input()関数を使用して新しいファイル名の入力
enter_new_name = input("新しいファイル名の入力 ⇒ ")

# --------------------------------------------------------------------------------------
# .wav

# 名前を変更するファイルを"files"と命名
files = glob.glob("*.wav")

# enumerate()関数を使用して"files"にインデックス番号を設定して抽出
for i, old_name in enumerate(files):

    # 新しいファイル名の決定
    # 新しいファイル名に「_001」を始めとする番号をつけるために"_{0:03d}"と"(i + 1)"を追加
    new_name = enter_new_name + "_wav_{0:03d}.wav".format(i + 1)

    # ファイル名の変更
    os.rename(old_name, new_name)

    # 変更の表示
    print(old_name + " ⇒ " + new_name)

# --------------------------------------------------------------------------------------
# .mp3

files = glob.glob("*.mp3")

for i, old_name in enumerate(files):

    new_name = enter_new_name + "_mp3_{0:03d}.mp3".format(i + 1)

    os.rename(old_name, new_name)

    print(old_name + " ⇒ " + new_name)

# --------------------------------------------------------------------------------------

# enterキーでコマンドプロンプトを終了
input()
