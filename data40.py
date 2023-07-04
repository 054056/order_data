#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data40
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/06/27(Created:2023/06/27)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data40.txt'
        interporate_path = 'data/interporate/data40.txt'
        combinations = gs.generate_combinations(self)
        train_combi = combinations[:160000]
        interporate_combi = combinations[160000:]
        for combi in train_combi:
            self.gene_question(combi, train_path)

        for combi in interporate_combi:
            self.gene_question(combi, interporate_path)

    def gene_question(self, combi, path):
        first_order_number, second_order_number = combi
        first_order = gs().num_to_ord(first_order_number)
        second_order = gs().num_to_ord(second_order_number)

        f = open(path, 'a')
        f.write("How many natural numbers are there between the ")
        f.write(first_order)
        f.write(" from the left and ")
        f.write(second_order)
        f.write("?\n")
        f.write(str(second_order_number-first_order_number-1))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
