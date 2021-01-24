import re
import xml.etree.ElementTree as ET
import logging
from xml.etree import ElementTree

import nltk
import xmltodict

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from config.Config import ConfigFile
from core.utils.Util import caching_files_exist
import networkx as nx


def get_only_text(doc, doc_id, graph):
    temp = []
    get_from_element_text(doc, temp, graph, doc_id)
    return " ".join(temp)


def get_id_from_link(text):
    if text is None:
        return -1

    index = text.find(".xml")
    if index > 0:
        tmp = index - 1
        while text[tmp - 1] != '/' and tmp != 0:
            tmp = tmp - 1
        end = tmp
    else:
        return -1
    return text[end:index]


def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def get_from_element_text(doc, text, graph, doc_id):
    if isinstance(doc, dict):
        for (tag, value) in doc.items():
            if tag == 'link' and isinstance(value[0], dict):
                for key in value[0].keys():
                    if get_id_from_link(value[0].get('@xlink:href')) != -1 and get_id_from_link(
                            value[0].get('@xlink:href')).isnumeric():
                        graph.add_edge(doc_id, get_id_from_link(value[0].get('@xlink:href')))
            if tag == 'title' and isinstance(value[0], str):
               alpha = ConfigFile().get_run_config('alpha')
               for i in range(alpha):
                    text.append(value[0])
            get_from_element_text(value, text, graph, doc_id)
    elif isinstance(doc, list):
        for i in doc:
            get_from_element_text(i, text, graph, doc_id)
    elif isinstance(doc, str):
        text.append(doc)
    return text


class CorpusParser:

    def __init__(self, filename=None, cleaning=[], lemmatizer=WordNetLemmatizer(), xml_folder=None):
        self.lemmatizer = lemmatizer
        self.filename = filename if filename is not None else ConfigFile().get_data_config("filename")
        self.xml_folder = xml_folder if xml_folder is not None else ConfigFile().get_data_config("xml_folder")
        self.corpus = dict()
        self.cleaning = cleaning
        self.graph_page = nx.DiGraph()

        # self.ancre = dict()
        # print(self.page_rank)

        if caching_files_exist() and ConfigFile().get_data_config("caching"):
            print("true")
        else:
            if ConfigFile().get_data_config("use_xml_file"):
                self.parse_xml()
            else:
                self.parse()

        self.page_rank = nx.pagerank(self.graph_page, 0.85)
        #print(self.page_rank)

    def doc_preprocessing(self, text):
        list_lemma = []
        text = text.lower()
        text = re.sub(r"\n", " ", text)
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
        # return list_tokens

    def parse(self):
        with open(self.filename, encoding="utf8") as file:
            xml_object = ET.fromstringlist(["<root>", str(file.read()), "</root>"])
            for idx in range(len(xml_object)):
                self.corpus[int(xml_object[idx][0].text)] = self.doc_preprocessing(xml_object[idx][0].tail)
        logging.info("Parsing done !!")

    def parse_xml(self):
        from os import walk
        _, _, filenames = next(walk(self.xml_folder))
        for filename in filenames:
            self.parse_page(filename)
        #for i in range(0, 10):
        #self.parse_page(filenames[i])

    def parse_page(self, filename):
        with open(self.xml_folder + filename) as file:
            # my_root = ET.parse(self.xml_folder + filename).getroot()
            self.graph_page.add_node(filename)
            json_file = xmltodict.parse(file.read(), xml_attribs=True,
                                        force_list=True)
            document = get_only_text(json_file, filename.split(".")[0], self.graph_page)
            doc_id = filename.split(".")[0]
            self.corpus[int(doc_id)] = self.doc_preprocessing(document)
        # print(self.corpus[doc_id])
        # print(my_root.tag)
        # for elem in my_root.iter():
        #    if elem.tag == "link":
        #        if elem.attrib:
        #            self.graph_page.add_edge(filename, elem.attrib.get('{http://www.w3.org/1999/xlink}href'))
        #    else:
        #        pass
        # return None, None
        # pass

    def get_doc(self, doc_id):
        self.corpus.get(doc_id)

    def get_corpus(self):
        return self.corpus

    def get_nb_docs(self):
        return len(self.corpus)

    def get_page_rank_score(self, doc_id):
        return self.page_rank.get(doc_id, 0)

    def get_all_page_rank(self):
        return self.page_rank
