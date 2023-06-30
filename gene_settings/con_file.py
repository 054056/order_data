#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ファイルの連結とランダムの並べ替え
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/06/20(Created:2023/06/20)'

import os
from collections import defaultdict

class Con_file:
    def main(self):
        train_directory_path = './../data/train'
        interporate_directory_path = './../data/interporate'

        train_output_file = './../data/train_fine.txt'
        interporate_output_file = './../data/interporate_fine.txt'

        files = [file for file in os.listdir(train_directory_path) if file.endswith('.txt')]

        # テキストファイルを結合する
        with open(train_output_file, 'w', encoding='utf-8') as output:
            for file in files:
                file_path = os.path.join(train_directory_path, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    output.write(text)


        files = [file for file in os.listdir(interporate_directory_path) if file.endswith('.txt')]

        with open(interporate_output_file, 'w', encoding='utf-8') as output:
            for file in files:
                file_path = os.path.join(interporate_directory_path, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    output.write(text)

        print("テキストファイルの結合が完了しました。")


if __name__ == "__main__":
    data = Con_file()
    data.main()