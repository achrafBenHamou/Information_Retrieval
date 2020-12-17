from DocumentMetric import LengthTable
from InvertedIndex import InvertedIndex


def build_data_structures(corpus):
    invertedIndex = InvertedIndex()
    dlt = LengthTable()
    for doc_id in corpus:
        for word in corpus[doc_id]:
            invertedIndex.add(str(word), str(doc_id))
        length = len(corpus[str(doc_id)])
        dlt.add(doc_id, length)
    return invertedIndex, dlt
