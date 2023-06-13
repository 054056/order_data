#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data17
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/05/24(Created:2023/05/24)'

from gene_settings.gene_set import GeneSet as gs

class Data17:
    def main(self):
        train_list = []
        for i in range(200000):
            quantity = gs().quantity()
            sequence = gs().gene_sequence_16digit(quantity)
            self.gene_question(sequence)


    def gene_question(self, sequence):
        length = len(sequence)
        first_order_number, second_order_number = gs().second_order_number(length)
        first_order = gs().num_to_ord(first_order_number)
        second_order = gs().num_to_ord(second_order_number)
        sequence_str = gs().sequence_str(sequence)

        f = open('data/data17.txt', 'a')
        f.write("What is the ")
        f.write(second_order)
        f.write(" number to the right counting from the ")
        f.write(first_order)
        f.write(" in the sequence ")
        f.write(sequence_str)
        f.write("?\n")
        f.write(str(sequence[first_order_number+second_order_number-1]))
        f.write("\n")


if __name__ == "__main__":
    data = Data17()
    data.main()
