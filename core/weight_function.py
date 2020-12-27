

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
    print("tf :", tf, " the idf : ", log(N / dft))
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
    tf= 1
    norm = 1
    if is_present:
        idf = log(N / df)
        return tf * idf * 1
    else:
        return 0


def lsn(tf, df, N):
    tfl = 1 + log(tf)
    idf = (log((N + 1) / df))**2
    return tfl * idf


def ntn(tf, df, N):
    tfn= tf
    idf= log(N / df)
    Norm= 1
    return tfn * idf * Norm


def nnn(tf):
    tfn= tf
    idf= 1
    norm= 1
    return tfn * idf * norm
         
          
def nfn(tf, df):
    tfn = tf
    idf = 1 / df
    norm = 1
    return tfn * idf * norm


def npn(tf, df, N):
    tfn= tf
    idf= log((N - df) / df)
    Norm= 1
    return tfn * idf * Norm


def nsn(tf, df, N):
    tfn= tf
    idf= (log((N + 1) / df)) ** 2
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


