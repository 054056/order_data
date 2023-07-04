#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data31_alphabet
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data31_alphabet.txt'
        interporate_path = 'data/interporate/data31_alphabet.txt'
        for i in range(160000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet, train_path)

        for i in range(40000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet, interporate_path)

    def gene_question(self, sequence, path):
        length = len(sequence)
        order_number = gs().order_number(length)
        order = gs().num_to_ord(order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("How many of the ")
        f.write(str(length))
        f.write(" alphabetical sequence ")
        f.write(sequence_str)
        f.write(" are there by the ")
        f.write(order)
        f.write("?\n")
        f.write(str(order_number))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
