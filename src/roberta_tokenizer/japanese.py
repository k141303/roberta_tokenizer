import os
import json
import codecs

import re

from janome.tokenizer import Tokenizer as JanomeTokenizer
from subword_nmt.apply_bpe import BPE

def load_json(file_path):
  with open(file_path, "r") as f:
    return json.load(f)

class BpeTokenizer(object):
  def __init__(self, codes, separator="@@"):
    self.separator = separator
    codes = codecs.open(codes, encoding="utf-8")
    self.bpe = BPE(codes, separator=separator)

  def tokenize(self, text):
    if len(text) == 0:
      return []
    encoded = self.bpe.process_line(text)
    return encoded.split(" ")

class JapaneseRoBERTaTokenizer(object):
  def __init__(self, version="20220905"):
    self.janome = JanomeTokenizer(wakati=True)

    bpe_codes_path = os.path.join(os.path.dirname(__file__), "data/ja", version, "codes.txt")
    self.bpe = BpeTokenizer(bpe_codes_path)

    vocab_path = os.path.join(os.path.dirname(__file__), "data/ja", version, "vocab.json")
    self.vocab = load_json(vocab_path)

    self.cls_token = "<s>"
    self.pad_token = "<pad>"
    self.sep_token = "</s>"
    self.unk_token = "<unk>"

  def tokenize(self, text):
    tokens = self.janome.tokenize(text)

    l_space = re.match("^(\s*)", text).group(1)
    tokens = [l_space] + list(tokens)

    tokens = [re.sub("\s", " ▁ ", t) for t in tokens]

    tokens = self.bpe.tokenize(" ".join(tokens))
    tokens = list(filter(len, tokens))

    return tokens

  def convert_tokens_to_ids(self, tokens):
    token_ids = [self.vocab.get(t, self.vocab[self.unk_token]) for t in tokens]
    return token_ids
