__author__ = 'Abou SANOU'

from config.Config import ConfigFile
from core.utils.Builder import build_data_structures
from core.weight_function import BM25, ltn, BM25ATTIRE, BM25ATTIRE_BIS, BM25L, lsn


class Engine:
    def __init__(self, queries, corpus, persit_mode=True):
        self.persit_mode = persit_mode
        self.queries = queries
        self.index, self.dlt = build_data_structures(corpus)

    def run(self, weight_function=ConfigFile().get_run_config("w_func")):
        results = {}
        #print(self.queries)
        for query in self.queries:
            if weight_function == "ltn":
                results[query[0]] = self.run_query_ltn(query[1])
            if weight_function == "lsn":
                results[query[0]] = self.run_query_lsn(query[1])
            if weight_function == "bm25":
                results[query[0]] = self.run_query_bm25(query[1])
            if weight_function == "bm25attire":
                results[query[0]] = self.run_query_bm25_attire(query[1])
            if weight_function == "bm25attirebis":
                results[query[0]] = self.run_query_bm25_attire_bis(query[1])
            if weight_function == "bm25l":
                results[query[0]] = self.run_query_bm25_l(query[1])

        return results

    def run_query_bm25_attire_bis(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = BM25ATTIRE_BIS(df=len(self.index[term]), freq=freq, N=len(self.dlt),
                                           doc_len=self.dlt.get_length(doc_id), avgdl=self.dlt.get_average_length())
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

    def run_query_bm25_l(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = BM25L(df=len(self.index[term]), freq=freq, N=len(self.dlt),
                                  doc_len=self.dlt.get_length(doc_id), avgdl=self.dlt.get_average_length())
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

        pass

    def run_query_bm25_attire(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = BM25ATTIRE(freq=freq, N=len(self.dlt),
                                       doc_len=self.dlt.get_length(doc_id), avgdl=self.dlt.get_average_length())
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

    def run_query_bm25(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = BM25(df=len(self.index[term]), freq=freq, qf=1, r=0, N=len(self.dlt),
                                 doc_length=self.dlt.get_length(doc_id)
                                 , average_doc_length=self.dlt.get_average_length())
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

    def run_query_ltn(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = ltn(self.index.tf(term, doc_id, self.dlt.get_length(doc_id)), len(self.index[term]),
                                len(self.dlt))
                    print(score)
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

    def weigt_query(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = ltn(self.index.tf(term, doc_id, self.dlt.get_length(doc_id)), len(self.index[term]),
                                len(self.dlt))
                    print(score)
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result

    def run_query_lsn(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = lsn(tf=freq, df=len(self.index[term]), N=len(self.dlt))
                    if doc_id in query_result:
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result