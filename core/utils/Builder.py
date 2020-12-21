import os

from config.Config import ConfigFile
from core.LengthTable import LengthTable
from core.InvertedIndex import InvertedIndex
from core.utils.Util import caching_files_exist


def build_data_structures(corpus):
    index = InvertedIndex()
    dlt = LengthTable()
    if ConfigFile().get_data_config("caching"):
        if caching_files_exist():
            index = InvertedIndex().get_instance()
            dlt = LengthTable().get_instance()
        else:
            for doc_id in corpus:
                for word in corpus[doc_id]:
                    index.add(str(word), str(doc_id))
                length = len(corpus[doc_id])
                print(doc_id, length)
                dlt.add(doc_id, length)
            index.persist()
            dlt.persist()
    return index, dlt
