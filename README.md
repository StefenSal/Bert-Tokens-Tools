# Bert tokens Tools

A useful tools to handle problems when you use Bert.

## Installation

### With Pip
This repository is tested on Python 3.6+, and can be installed using pip as follows:
```shell
pip install bert-tokens
```

## Usage

### Tokenization and token-span-convert
WordPiece tokenization for BERT, which can be universally applicable for different language versions for BERT. The supported BERT checkpoints including but not limited to:
- **[`BERT-Base, Uncased`](https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip)**
- **[`BERT-Base, Chinese`](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)**
- **[`BERT-Base, Multilingual Cased`](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip)**

### Token-span-convert
Convert token span from char-level to wordpiece-level. This usually happens in multi-lingual scenarios.

For example, query="播放mylove"，the char-level index of sequence "mylove" is [2,8], while the token index after bert tokenization should be [2,4]

### Example
```python
from bert_tokens.bert_tokenizer import Tokenizer
from bert_tokens.convert_word_span import convert_word_span

dict_path = "vocab/vocab.txt"
tokenizer = Tokenizer(dict_path, do_lower_case=True)
tokens = tokenizer.tokenize("播放MYLOVE")
print(tokens)
## ['播', '放', 'my', '##love']
convert_word_span("播放MYLOVE", [2,8], tokenizer)
print(convert_word_span)
## [2, 4]
```
