__author__ = 'Abou SANOU'

from core.utils.Builder import build_data_structures
from core.weight_function import BM25, ltn


class Engine:
    def __init__(self, queries, corpus, persit_mode=True):
        self.persit_mode = persit_mode
        self.queries = queries
        self.index, self.dlt = build_data_structures(corpus)

    def run(self):
        results = {}
        for query in self.queries:
            results[query[0]] = self.run_query_ltn(query[1])
        return results

    def run_query(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                for doc_id, freq in self.index[term].items():
                    score = BM25(number_docs=len(self.index[term]), freq=freq, qf=1, r=0, N=len(self.dlt),
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