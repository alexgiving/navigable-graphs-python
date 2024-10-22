#!/bin/bash

ORIGIN_PATH="results/results_orig_1m.log"
MODIFIED_PATH="results/results_modified_1m.log"
ASSET_PATH="assets"

echo "" &> ${ORIGIN_PATH}
echo "" &> ${MODIFIED_PATH}

python test-hnsw.py --dataset sift-1m --M0 16 --M 8 --ef 64 --hue original >> ${ORIGIN_PATH} 2>&1
python test-hnsw.py --dataset sift-1m --M0 16 --M 8 --ef 64 --hue modified >> ${MODIFIED_PATH} 2>&1

python test-hnsw.py --dataset sift-1m --M0 32 --M 16 --ef 64 --hue original >> ${ORIGIN_PATH} 2>&1
python test-hnsw.py --dataset sift-1m --M0 32 --M 16 --ef 64 --hue modified >> ${MODIFIED_PATH} 2>&1

python test-hnsw.py --dataset sift-1m --M0 64 --M 32 --ef 64 --hue original >> ${ORIGIN_PATH} 2>&1
python test-hnsw.py --dataset sift-1m --M0 64 --M 32 --ef 64 --hue modified >> ${MODIFIED_PATH} 2>&1

python make_chart.py ${ORIGIN_PATH} ${MODIFIED_PATH} --output ${ASSET_PATH}/results_on_1m.png