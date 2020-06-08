# Word Embedding Attention Network

Code for "Word Embedding Attention Network: Generating Words by Querying Distributed Word Representations for Paraphrase Generation" [[pdf]](https://arxiv.org/abs/1803.01465)

## Requirements

* Ubuntu 16.04
```
AWS - Deep Learning Base AMI (Ubuntu 16.04) Version 24.0 (ami-047abd49e556a94fe)
```
* Python 3.6
Install pre-requisites:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
sudo apt install libedit-dev
```
Then:
```
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar xvf Python-3.6.9.tgz
cd Python-3.6.9
./configure --enable-optimizations --enable-shared --with-ensurepip=install
make -j8
sudo make altinstall
python3.6
```
* Pytorch 1.0.0
* allennlp 0.7.2
* torchfile
```
pip3 install -r requirements.txt
```

## Data Preparation

- Step 1: Download the [PWKP dataset](https://github.com/XingxingZhang/dress) and put it in the folder *data/*.
- Step 2: Preprocess the dataset
```bash
cd preprocess/
python3 process_pkwp.py
```

## Train
```bash
python3 run.py -gpu 0 -mode train -dir save_path
```

## Evaluate
- Step 1: Download the pretrained model, best.th from [here](https://drive.google.com/file/d/1pH5OG5-gXFtmnD4Rt_iUjaW5R6L_0IDX/view?usp=sharing)
- Step 2: Restore and evaluate the model with the BLEU metric
```bash
python3 run.py -gpu 0 -mode evaluate -restore path_to_model/best.th
```

## Predict
- Step 1: Download the pretrained model, best.th from [here](https://drive.google.com/file/d/1pH5OG5-gXFtmnD4Rt_iUjaW5R6L_0IDX/view?usp=sharing)
- Step 2: Restore and predict a paraphrase for a sentence
```bash
python3 run.py -gpu 0 -mode predict -restore path_to_model/best.th
```
