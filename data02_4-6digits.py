#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data02_4-6digits
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data02_4-6digits.txt'
        interporate_path = 'data/interporate/data02_4-6digits.txt'
        for i in range(160000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_6digit(quantity)
            self.gene_question(sequence, train_path)

        for i in range(40000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_6digit(quantity)
            self.gene_question(sequence, interporate_path)


    def gene_question(self, sequence, path):
        length = len(sequence)
        order_number = gs().order_number(length)
        order = gs().num_to_ord(order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("What is the ")
        f.write(order)
        f.write(" from the right in the sequence of numbers ")
        f.write(sequence_str)
        f.write("?\n")
        f.write(str(sequence[length-order_number]))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
