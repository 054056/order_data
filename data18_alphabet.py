#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data18_alphabet
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data18_alphabet.txt'
        interporate_path = 'data/interporate/data18_alphabet.txt'
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
        first_order_number, second_order_number, third_order_number = gs().skill3(length)
        first_order = gs().num_to_ord(first_order_number)
        second_order = gs().num_to_ord(second_order_number)
        third_order = gs().num_to_ord(third_order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("What is the ")
        f.write(third_order)
        f.write(" from the right in the alphabetical sequence ")
        f.write(sequence_str)
        f.write(" between the ")
        f.write(first_order)
        f.write(" from the left and ")
        f.write(second_order)
        f.write("?\n")
        f.write(str(sequence[second_order_number-third_order_number-1]))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
