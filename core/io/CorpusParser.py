import re
import xml.etree.ElementTree as ET
import logging

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from config.Config import ConfigFile
from core.utils.Util import caching_files_exist
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

class CorpusParser:

    def __init__(self, filename=None, cleaning=[], lemmatizer=WordNetLemmatizer()):
        self.lemmatizer = lemmatizer
        self.filename = filename if filename is not None else ConfigFile().get_data_config("filename")
        self.corpus = dict()
        self.cleaning = cleaning
        if not (caching_files_exist() and ConfigFile().get_data_config("caching")):
            self.parse()

    def doc_preprocessing(self, text):
        list_lemma = []
        text = text.lower()
        text = re.sub(r"\n", " ", text)
        #text = re.sub(r"https?://.*[\s]*", "", text)
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
        with open(self.filename, encoding="utf8") as file:
            xml_object = ET.fromstringlist(["<root>", str(file.read()), "</root>"])
            for idx in range(len(xml_object)):
                self.corpus[int(xml_object[idx][0].text)] = self.doc_preprocessing(xml_object[idx][0].tail)
        logging.info("Parsing done !!")

    def parseXml(self):
        pass

    def get_doc(self, doc_id):
        self.corpus.get(doc_id)

    def get_corpus(self):
        return self.corpus

    def get_nb_docs(self):
        return len(self.corpus)

