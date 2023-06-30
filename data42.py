#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data42
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data42:
    def main(self):
        train_path = 'data/train/data42.txt'
        interporate_path = 'data/interporate/data42.txt'
        for i in range(160000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_20digit(quantity)
            self.gene_question(sequence, train_path)

        for i in range(40000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_20digit(quantity)
            self.gene_question(sequence, interporate_path)

#How many are in the number sequence 2,47,434,535
    def gene_question(self, sequence, path):
        length = len(sequence)
        order_number = gs().order_number(length)
        order = gs().num_to_ord(order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("How many are in the number sequence")
        f.write(sequence_str)
        f.write("?\n")
        f.write(str(length))
        f.write("\n")


if __name__ == "__main__":
    data = Data42()
    data.main()
