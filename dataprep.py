import numpy as np
import os
from collections import Counter

def load_data(path):
    text_file = os.path.join(path)
    with open(text_file,'r') as f:
        data = f.read()
    return data

def word_embeddings(text):
    char_counts = Counter(text)
    char_counts = sorted(char_counts,key=char_counts.get,reverse=True)
    vocab_to_int = {char_counts[x]:x for x in range(len(char_counts))}
    int_to_vocab = {x:char_counts[x] for x in range(len(char_counts))}
    return vocab_to_int,int_to_vocab

data_dir = './data/lyrics.txt'
text = load_data(data_dir)

print (len(text))

v,i = word_embeddings(text)
print(i)