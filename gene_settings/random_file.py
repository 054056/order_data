import random

# テキストファイルのパス
train_file_path = "./../data/train_fine.txt"
train_out_file = "./../data/train_shufle.txt"
interporate_file_path = "./../data/interporate_fine.txt"
interporate_out_file = "./../data/interporate_shufle.txt"
# ファイルを読み込み、質問と答えの組をリストに格納する
qa_pairs = []
with open(train_file_path, "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i + 1].strip()
        qa_pairs.append((question, answer))

# リストの要素をランダムに並び替える
random.shuffle(qa_pairs)

# 並び替えた結果をファイルに書き込む
with open(train_out_file, "w") as file:
    for question, answer in qa_pairs:
        file.write(f"{question}\n{answer}\n")


qa_pairs = []
with open(interporate_file_path, "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i + 1].strip()
        qa_pairs.append((question, answer))

# リストの要素をランダムに並び替える
random.shuffle(qa_pairs)

# 並び替えた結果をファイルに書き込む
with open(interporate_out_file, "w") as file:
    for question, answer in qa_pairs:
        file.write(f"{question}\n{answer}\n")
