import os

from config.Config import ConfigFile
from core.LengthTable import LengthTable
from core.InvertedIndex import InvertedIndex
from core.utils.Util import caching_files_exist, load_dict_page_rank, persit_dict_page_rank


def build_data_structures(corpus, page_rank):
    index = InvertedIndex()
    dlt = LengthTable()
    page_rank = page_rank
    if caching_files_exist() and ConfigFile().get_data_config("caching"):
        index = InvertedIndex().get_instance()
        dlt = LengthTable().get_instance()
        page_rank = load_dict_page_rank()
    else:
        for doc_id in corpus:
            for word in corpus[doc_id]:
                index.add(str(word), str(doc_id))
            length = len(corpus[doc_id])
            dlt.add(doc_id, length)
        index.persist()
        dlt.persist()
        persit_dict_page_rank(page_rank)
    return index, dlt, page_rank
