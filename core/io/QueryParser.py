import re

from nltk import word_tokenize
from nltk.corpus import stopwords
from config.Config import ConfigFile


class QueryParser:

    def __init__(self, filename=None):
        self.filename = filename if filename is not None else ConfigFile().get_data_config("query")
        self.queries = []
        self.parse()

    def doc_preprocessing(self, text):
        list_lemma = []
        text = text.lower()
        text = re.sub(r"\n", " ", text)
        # text = re.sub(r"https?://.*[\s]*", "", text)
        text = re.sub(r"[^a-z ]*", "", text)
        text = re.sub(r"[\s]+", " ", text)
        list_tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        for token in list_tokens:
            lemma = self.lemmatizer.lemmatize(token)
            if lemma not in stop_words:
                list_lemma.append(lemma)
        # after this step, there is always the word with single char, I decide to delete them.
        return [i for i in list_lemma if len(i) > 1]

    def parse(self):
        with open(self.filename) as f:
            lines = ''.join(f.readlines())
        self.queries = [[x.rstrip().split(":")[0], x.rstrip().split(":")[1].rstrip().split()] for x in
                        lines.split('\n')[:-1]]

    def get_queries(self):
        return self.queries

    def get_tf(self, word, req_id):
        self.queries[req_id]