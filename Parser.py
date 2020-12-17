import re
import xml.etree.ElementTree as ET
import outils


class CorpusParser:

    def __init__(self, filename):
        self.filename = filename
        self.regex = re.compile('^#\s*\d+')
        self.corpus = dict()

    def doc_preprocessing(self,text):
        text = text.lower()
        text = re.sub(r"\n", " ", text)
        text = re.sub(r"https?://.*[\s]*", "", text)
        text = re.sub(r"[^a-z ]*", "", text)
        text = re.sub(r"[\s]+", " ", text)
        return text

    def parse(self):
        with open(self.filename, encoding="utf8") as file:
            xml_object = ET.fromstringlist(["<root>", str(file.read()), "</root>"])
            for idx in range(len(xml_object)):
                self.corpus[xml_object[idx][0].text] = xml_object[idx][0].tail

    def get_doc(self,id):
        self.corpus.get(id)

    def get_corpus(self):
        return self.corpus

    def get_nb_docs(self):
        return len(self.corpus)

    def liste2dicionary(self, liste):
        dicionary = {}
        for word in liste:
            if word in dicionary.keys():
                dicionary[word] += 1
            else:
                dicionary[word] = 1
        return dicionary

    def docs2dicionaryDoc(self):
        dicionaryDocs = {}
        Documents_txt = "./Text_Only_Ascii_Coll_MWI_NoSem/Text_Only_Ascii_Coll_MWI_NoSem"
        with open(Documents_txt, encoding="utf8") as f:
            filecontent = f.read()
        A = outils.cherche_occurrences(filecontent, "<docno>")
        B = outils.cherche_occurrences(filecontent, "</docno>")
        C = outils.cherche_occurrences(filecontent, "</doc>")
        DocsList = outils.getListIDs(filecontent, A, B)
        global nb_docs
        nb_docs = len(DocsList)
        for i in range(0, len(A)):
            filename = DocsList[i]
            doc_content = outils.getTextByIndices(filecontent, A[i] + 8 + len(DocsList[i]), C[i])
            doc_processed_content = outils.doc_preprocessing(doc_content)
            listeOfWords = outils.TextTowords(doc_processed_content)
            dicionaryDocs[filename] = liste2dicionary(listeOfWords)

        return dicionaryDocs

