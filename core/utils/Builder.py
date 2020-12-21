from core.LengthTable import LengthTable
from core.InvertedIndex import InvertedIndex


def build_data_structures(corpus):
    index = InvertedIndex()
    dlt = LengthTable()
    for doc_id in corpus:
        for word in corpus[doc_id]:
            index.add(str(word), str(doc_id))
        length = len(corpus[doc_id])
        print(doc_id, length)
        dlt.add(doc_id, length)
    if persit_mode:
        index.persist()
    return index, dlt
