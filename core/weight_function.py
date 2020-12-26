__author__ = 'Abou SANOU'

from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0


# @url of document{http://www.kmwllc.com/index.php/2020/03/20/understanding-tf-idf-and-bm25/}
# nb_docs_term : number of document contained the word
# N : number of document of corpus
# doc_length : length of document
# average_doc_length : average length of all documents
# qf = 1
# r = 0
def BM25(number_docs, freq, qf, r, N, doc_length, average_doc_length):
    K = compute_K(doc_length, average_doc_length)
    td = log(((r + 0.5) / (R - r + 0.5)) / ((number_docs - r + 0.5) / (N - number_docs - R + r + 0.5)))
    idf = ((k1 + 1) * freq) / (K + freq)
    norm = ((k2 + 1) * qf) / (k2 + qf)
    return td * idf * norm


def compute_K(doc_length, average_doc_length):
    return k1 * ((1 - b) + b * (float(doc_length) / float(average_doc_length)))


def ltn(tf, dft, N):
    return (1 + log(tf)) * log(N / dft)


def bnn():
    pass

def xyz():
    pass