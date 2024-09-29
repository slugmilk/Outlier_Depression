# -*- coding: utf-8 -*-
"""n그램.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P4Hlq0EYP0x5TPO35LxiTLIfJwqELcln
"""

pip install nltk

pip install konlpy

pip install gensim

pip install spacy

pip install pyLDAvis

pip install matplotlib

import nltk
import konlpy
from konlpy.tag import Komoran
Komoran().pos('했다')
import re
import numpy as np
import pandas as pd
from pprint import pprint
import json
import codecs
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import os
from gensim.models.wrappers import LdaMallet
os.environ['MALLET_HOME'] = 'C:/Users/user/Desktop/Project/mallet'
import spacy
import pyLDAvis
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
import logging
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from google.colab import files

file_uploaded = files.upload()

df = pd.read_excel('kin_excel.xlsx')
df = df[['question','answer']]

df.head()

#리스트로
data = df.values.tolist()
pprint(data[:1])

#토큰화
def sent_to_words(sentences):
  for sentence in sentences:
    yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

data_words = list(sent_to_words(data))

print(data_words[:1])

#Bigram, Trigram 모델

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
trigram = gensim.models.Phrases(bigram[data_words], threshold=100)
#threshold 클수록 단어 붙이기 어려움. 100이 기본값

bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)

print(trigram_mod[bigram_mod[data_words[1]]])