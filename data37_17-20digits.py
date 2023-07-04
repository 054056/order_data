#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data37_17-20digits
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data37_17-20digits.txt'
        interporate_path = 'data/interporate/data37_17-20digits.txt'
        for i in range(160000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_20digit(quantity)
            self.gene_question(sequence, train_path)

        for i in range(40000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_20digit(quantity)
            self.gene_question(sequence, interporate_path)


    def gene_question(self, sequence, path):
        length = len(sequence)
        first_order_number, second_order_number = gs().between_skill3(length)
        first_order = gs().num_to_ord(first_order_number)
        second_order = gs().num_to_ord(second_order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("Howm many are there between the ")
        f.write(first_order)
        f.write(" and ")
        f.write(second_order)
        f.write(" from the left in the sequence of ")
        f.write(str(length))
        f.write(" numbers ")
        f.write(sequence_str)
        f.write("?\n")
        f.write(str(second_order_number - first_order_number - 1))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
