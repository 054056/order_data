#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
データ作成
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

import random
from collections import defaultdict

class GeneSet:
    def quantity(self):
        """
        何個の整数を生成するか
        """
        quantity = random.randint(3,30)

        return quantity

    def alphabet_quantity(self):
        """
        何個のアルファベットを生成するか
        """
        quantity = random.randint(3,26)

        return quantity


    def gene_alphabet(self, quantity):
        """
        アルファベットの並びを生成
        """
        alphabet = ["a","b,","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        alphabet_list = []
        for _ in range(quantity):
            value = random.randint(0,25)
            alphabet_list.append(alphabet[value])

        return alphabet_list


    def gene_sequence_3digit(self, quantity):
        """
        1~3桁の数で個数分の値を生成
        """
        sequence_3digit = []
        for _ in range(quantity):
            value = random.randint(0, 999)
            sequence_3digit.append(value)
        return sequence_3digit


    def gene_sequence_6digit(self, quantity):
        """
        4~6桁の数で個数分の値を生成
        """
        sequence_6digit = []
        for _ in range(quantity):
            value = random.randint(1000, 999999)
            sequence_6digit.append(value)
        return sequence_6digit


    def gene_sequence_9digit(self, quantity):
        """
        7~9桁の数で個数分の値を生成
        """
        sequence_9digit = []
        for _ in range(quantity):
            value = random.randint(1000000, 999999999)
            sequence_9digit.append(value)
        return sequence_9digit


    def gene_sequence_16digit(self, quantity):
        """
        10~16桁の数で個数分の値を生成
        """
        sequence_16digit = []
        for _ in range(quantity):
            value = random.randint(1000000000, 9999999999999999)
            sequence_16digit.append(value)
        return sequence_16digit


    def gene_sequence_20digit(self, quantity):
        """
        17~20桁の数で個数分の値を生成
        """
        sequence_9digit = []
        for _ in range(quantity):
            value = random.randint(1000000, 999999999)
            sequence_9digit.append(value)
        return sequence_9digit


    def order_number(self, len):
        """
        n番目のnをリストの長さからランダムで抽出
        """

        order_number = random.randint(1, len)

        return order_number


    def second_order_number(self,length):
        """
        2つの順序数をランダムで抽出
        """
        first = random.randint(1,length-1)
        second = random.randint(1, length-first)

        return first, second

    def num_to_ord(self, num) -> str:
        """
        順番を1st,2nd,3rd,4thのように変換
        """
        ordinal_dict = defaultdict(lambda: "th")
        ordinal_dict.update({1: "st", 2: "nd", 3: "rd"})
        q, mod = divmod(num, 10)
        suffix = "th" if q % 10 == 1 else ordinal_dict[mod]

        return f"{num}{suffix}"


    def sequence_str(self, sequence):
        """
        [1,2,3,4] → 1,2,3,4のように括弧を外す
        """

        return str(sequence)[1:-1]
