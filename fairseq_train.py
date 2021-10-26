#!/usr/bin/env python

from subprocess import run

cmd = """ fairseq-train \
    data-bin \
    --source-lang ice.g \
    --target-lang ice.p \
    --seed 1 \
    --arch lstm \
    --lr 0.001 \
    --optimizer adam \
    --clip-norm 1 \
    --keep-last-epochs -1 \
    --criterion label_smoothed_cross_entropy \
    --max-update 800 \
    --encoder-bidirectional \
    --encoder-embed-dim 128 \
    --decoder-embed-dim 128 \
    --batch-size 64
"""

run(cmd, shell=True)  

'''
    --required-batch-size-multiple 5 
    --decoder-output-dim 128
'''


