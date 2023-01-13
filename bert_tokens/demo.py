# Show cases

from bert_tokenizer import Tokenizer
from convert_word_span import convert_word_span

dict_path = "bert_tokens/vocab/vocab.txt"
tokenizer = Tokenizer(dict_path, do_lower_case=True)
tokens = tokenizer.tokenize("播放MYLOVE")
print(tokens)

print(convert_word_span("播放MYLOVE", [2,8], tokenizer))