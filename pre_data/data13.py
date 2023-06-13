#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data13
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data13:
    def main(self):
        train_list = []
        for i in range(200000):
            quantity = gs().alphabet_quantity()
            sequence_alphabet = gs().gene_alphabet(quantity)
            self.gene_question(sequence_alphabet)


    def gene_question(self, sequence):
        length = len(sequence)
        first_order_number, second_order_number = gs().second_order_number(length)
        first_order = gs().num_to_ord(first_order_number)
        second_order = gs().num_to_ord(second_order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open('data/data13.txt', 'a')
        f.write("What is the ")
        f.write(second_order)
        f.write(" letter in the alphabetical sequence ")
        f.write(sequence_str)
        f.write(" counting from the ")
        f.write(first_order)
        f.write(" to the right")
        f.write("?\n")
        f.write(str(sequence[first_order_number+second_order_number-1]))
        f.write("\n")


if __name__ == "__main__":
    data = Data13()
    data.main()
