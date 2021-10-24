#!/usr/bin/env python

with open("ice_train.tsv", "r") as in_file:
    g_file = open("train.ice.g", "w")
    devg_file = open("dev.ice.g", "w")
    testg_file = open("test.ice.g", "w")
    
    p_file = open("train.ice.p", "w")
    devp_file = open("dev.ice.p", "w")
    testp_file = open("test.ice.p", "w")

    for line in in_file:
        word = line.split("\t")[0]
        phones = line.split("\t")[1]
        graphemes = " ".join(word)
        g_file.write(graphemes+"\n")
        devg_file.write(graphemes+"\n")
        testg_file.write(graphemes+"\n")
        p_file.write(phones)
        devp_file.write(phones)
        testp_file.write(phones)


    g_file.close()
    devg_file.close()
    testg_file.close()
    
    p_file.close()
    devp_file.close()
    testp_file.close()

