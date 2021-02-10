import math
from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0
epsilon = 0.6


def tf_idf_epsilon(freq, N, df, doc_len, avgdl, epsilon=0.6, b=0.4):
    tmp = (1 + math.log(1 + math.log(((freq) / (1 - b + b * (doc_len / avgdl))) + epsilon)))
    return math.log((N + 1) / df) * tmp


def bm25_plus(freq, N, df, doc_len, avgdl, k1=1.6, epsilon=0.6):
    log_part = math.log((N + 1) / df)
    num = ((k1 + 1) * freq)
    det = (k1 * ((1 - b) + b * (doc_len / avgdl)) + freq)
    return log_part * ((num / det) + epsilon)


"""
ATIRE BM25 
Improvements to BM25 and Language Models Examined
"""


def BM25ATTIRE(freq, N, avgdl, doc_len, delta=0.5, k1=1.5, b=0.75):
    idf = math.log(N - freq + 0.5) - math.log(freq + 0.5)
    tfnorw = freq * (freq * (k1 + 1) /
                     (freq + k1 * (1 - b + b * doc_len / avgdl)))

    return idf * tfnorw


def BM25ATTIRE_BIS(df, freq, N, avgdl, doc_len, delta=0.5, k1=1.5, b=0.75):
    # section 3.1 ATIRE BM25 of the paper
    return math.log(N / df) * (((k1 + 1) * freq) / (k1 * (1 - b + b * (doc_len / avgdl)) + freq))


def BM25L(df, freq, N, avgdl, doc_len, delta=0.5, k1=1.5, b=0.75):
    ctd = freq / (1 - b + b * (doc_len / avgdl))

    return math.log((N + 1) / (df + 0.5)) * ((k1 + 1) * ctd) / (k1 + ctd)


def ltn(tf, dft, N):
    return (1 + log(tf)) * log(N / dft)


def bnn():
    pass


def xyz():
    pass


def bnn(tf):
    idf = 1
    Norm = 1
    return tf * idf * Norm


def btn(is_present, df, N):
    tf = 1
    norm = 1
    if is_present:
        idf = log(N / df)
        return tf * idf * 1
    else:
        return 0


def lsn(tf, df, N):
    tfl = 1 + log(tf)
    idf = (log((N + 1) / df)) ** 2
    return tfl * idf


def ntn(tf, df, N):
    tfn = tf
    idf = log(N / df)
    Norm = 1
    return tfn * idf * Norm


def nnn(tf):
    tfn = tf
    idf = 1
    norm = 1
    return tfn * idf * norm


def nfn(tf, df):
    tfn = tf
    idf = 1 / df
    norm = 1
    return tfn * idf * norm

#<<<<<<< Amine
#def btn(df, N):
#    tf= 1
#    idf= log(N / df)
#    Norm= 1
#    return (tf * idf * Norm)
#=======
#>>>>>>> main

def npn(tf, df, N):
    tfn = tf
    idf = log((N - df) / df)
    Norm = 1
    return tfn * idf * Norm


def nsn(tf, df, N):
    tfn = tf
    idf = (log((N + 1) / df)) ** 2
    Norm = 1
    return tfn * idf * Norm


def bpn(df, N):
    tf = 1
    idf = log((N - df) / df)
    Norm = 1
    return tf * idf * Norm


def bsn(df, N):
    tf = 1
    idf = (log((N + 1) / df)) ** 2
    norm = 1
    return tf * idf * norm


def bfn(df):
    tf = 1
    idf = 1 / df
    Norm = 1
    return tf * idf * Norm


def ssn(tf, df, N):
    tfs = tf ** 2
    idf = (log((N + 1) / df)) ** 2
    norm = 1
    return tfs * idf * norm


def spn(tf, df, N):
    tfs = tf ** 2
    idf = log((N - df) / df)
    Norm = 1
    return tfs * idf * Norm


def sfn(tf, df):
    tfs = tf ** 2
    idf = 1 / df
    Norm = 1
    return tfs * idf * Norm


def stn(tf, df, N):
    tfs = tf ** 2
    idf = log(N / df)
    Norm = 1
    return tfs * idf * Norm


def snn(tf):
    tfs = tf ** 2
    idf = 1
    Norm = 1
    return tfs * idf * Norm


def lnn(tf):
    tfl = 1 + log(tf)
    idf = 1
    Norm = 1
    return tfl * idf * Norm


def lfn(tf, df):
    tfl = 1 + log(tf)
    idf = 1 / df
    Norm = 1
    return tfl * idf * Norm


def lpn(tf, df, N):
    tfl = 1 + log(tf)
    idf = log((N - df) / df)
    Norm = 1
    return tfl * idf * Norm


# @url of document{http://www.kmwllc.com/index.php/2020/03/20/understanding-tf-idf-and-bm25/}
# df : number of document contained the word df
# N : number of document of corpus
# doc_length : length of document
# average_doc_length : average length of all documents
# qf = 1
# r = 0
#1994-trec-p109-robertson
#form Michel Beigbeder Information Retrieval – 3
def bm25(df, freq, qf, r, N, doc_length, average_doc_length):
    K = k(doc_length, average_doc_length)
    td = log(((r + 0.5) / (R - r + 0.5)) / ((df - r + 0.5) / (N - df - R + r + 0.5)))
    idf = ((k1 + 1) * freq) / (K + freq)
    norm = ((k2 + 1) * qf) / (k2 + qf)
    return td * idf * norm


def k(doc_length, average_doc_length):
    return k1 * ((1 - b) + b * (float(doc_length) / float(average_doc_length)))
