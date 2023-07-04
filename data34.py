#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
data34
"""
__author__ = 'Hayashi Kanji'
__version__ = '1.0.0'
__data__ = '2023/06/27(Created:2023/06/27)'

from gene_settings.gene_set import GeneSet as gs

class Data:
    def main(self):
        train_path = 'data/train/data34.txt'
        interporate_path = 'data/interporate/data34.txt'
        for i in range(160000):
            self.gene_question(i, train_path)

        for i in range(40000):
            self.gene_question(i, interporate_path)

    def gene_question(self, i, path):
        order = gs().num_to_ord(i+1)

        f = open(path, 'a')
        f.write("How many natural numbers are there from the smallest to the ")
        f.write(order)
        f.write("?\n")
        f.write(str(i+1))
        f.write("\n")


if __name__ == "__main__":
    data = Data()
    data.main()
