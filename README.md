# Word Embedding Attention Network

Code for "Word Embedding Attention Network: Generating Words by Querying Distributed Word Representations for Paraphrase Generation" [[pdf]](https://arxiv.org/abs/1803.01465)

## Requirements

* Ubuntu 16.04
* Python 3.6
* Pytorch 1.0.0
* allennlp 0.7.2
* torchfile

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