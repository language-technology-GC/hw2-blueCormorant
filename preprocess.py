#!/usr/bin/env python

with open("ice_train.tsv", "r") as in_file:
    with open("train.ice.g", "w") as gfile:
        with open("train.ice.p", "w") as pfile:
            for line in in_file:
                word = line.split("\t")[0]
                phones = line.split("\t")[1]
                graphemes = " ".join(word)
                gfile.write(graphemes+"\n")
                pfile.write(phones)

with open("ice_test.tsv", "r") as in_file:
    with open("test.ice.g", "w") as gfile:
        with open("test.ice.p", "w") as pfile:
            for line in in_file:
                word = line.split("\t")[0]
                phones = line.split("\t")[1]
                graphemes = " ".join(word)
                gfile.write(graphemes+"\n")
                pfile.write(phones)

with open("ice_dev.tsv", "r") as in_file:
    with open("dev.ice.g", "w") as gfile:
        with open("dev.ice.p", "w") as pfile:
            for line in in_file:
                word = line.split("\t")[0]
                phones = line.split("\t")[1]
                graphemes = " ".join(word)
                gfile.write(graphemes+"\n")
                pfile.write(phones)

