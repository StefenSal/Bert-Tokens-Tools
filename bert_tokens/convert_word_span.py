#! -*- coding: utf-8 -*-
# convert word index from char-level to bert tokenized token level
# For example:
# query="播放mylove"，the index of sequence "mylove" is [2,8], while the true index after bert tokenized token should be [2,4]

def convert_word_span(query, span, tokenizer, delete_cls_sep=True):
    if not isinstance(span, list) and not isinstance(span, tuple):
        raise TypeError("Input span must be List or Tuple")

    char_start, char_end = span
    if char_start == 0:
        start = 0
    else:
        start = len(tokenizer.tokenize(query[:char_start]))-2

    end = start + len(tokenizer.tokenize(query[char_start:char_end])) - 2
    return [start, end]
