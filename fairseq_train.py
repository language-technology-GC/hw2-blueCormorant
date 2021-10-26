#!/usr/bin/env python

from subprocess import run

cmd = """ fairseq-train \
    data-bin \
    --source-lang ice.g \
    --target-lang ice.p \
    --seed 1 \
    --arch lstm \
    --dropout 0.2 \
    --encoder-bidirectional \
    --encoder-embed-dim 128 \
    --decoder-embed-dim 128 \
    --decoder-out-embed-dim 128 \
    --encoder-hidden-size 512 \
    --decoder-hidden-size 512 \
    --lr 0.001 \
    --optimizer adam \
    --clip-norm 1 \
    --keep-last-epochs -1 \
    --criterion label_smoothed_cross_entropy \
    --max-update 800 \
    --batch-size 50 \
    --label-smoothing 0.1
"""

run(cmd, shell=True)  

'''
    --decoder-output-dim 128 \
    --required-batch-size-multiple 5 
'''


