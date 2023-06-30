#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data43
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data43:
    def main(self):
        train_path = 'data/train/data43.txt'
        interporate_path = 'data/interporate/data43.txt'
        for i in range(160000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet, train_path)

        for i in range(40000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet, interporate_path)

#How many are in the alphabetical sequence a,g,c,s,t,f
    def gene_question(self, sequence, path):
        length = len(sequence)
        order_number = gs().order_number(length)
        order = gs().num_to_ord(order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open(path, 'a')
        f.write("How many alphabetical sequences ")
        f.write(sequence_str)
        f.write(" are there before the ")
        f.write(order)
        f.write("?\n")
        f.write(str(order_number))
        f.write("\n")


if __name__ == "__main__":
    data = Data43()
    data.main()
