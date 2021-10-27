#!/usr/bin/env python

word_errors = 0

with open("outcomes.txt", "r") as in_file:
    for line in in_file:
        split_line = line.split("\t")
        gold = split_line[1].strip()
        hypo = split_line[4].strip()
        if gold != hypo:
            word_errors += 1
        
print(f"WER = {word_errors}")

