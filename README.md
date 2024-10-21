# Navigable Graphs Python
Python based research tool for studying navigable graphs for nearest neighbour search


Download dataset
```bash
mkdir -p datasets
pushd datasets
    wget ftp://ftp.irisa.fr/local/texmex/corpus/siftsmall.tar.gz -o dataset.tar.gz
    tar -xvf siftsmall.tar.gz
popd
```

Using the SIFT dataset:
```
python navigable-graphs.py --dataset sift
```

Using synthetic data with 3D vectors:
```
python navigable-graphs.py --dataset synthetic --K 20 --k 5 --dim 3 --n 500 --nq 100 --ef 20 --M 2
```