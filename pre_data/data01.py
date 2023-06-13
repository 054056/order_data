#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data01
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data01:
    def main(self):
        train_list = []
        for i in range(200000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet)


    def gene_question(self, sequence):
        length = len(sequence)
        order_number = gs().order_number(length)
        order = gs().num_to_ord(order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open('data/data01.txt', 'a')
        f.write("What is the ")
        f.write(order)
        f.write(" in the sequence of alphabet ")
        f.write(sequence_str)
        f.write("?\n")
        f.write(str(sequence[order_number-1]))
        f.write("\n")


if __name__ == "__main__":
    data = Data01()
    data.main()
