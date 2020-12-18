__author__ = 'Abou SANOU'
from Buider import build_data_structures
from weight_function import BM25


class Engine:
    def __init__(self, queries, corpus):
        self.queries = queries
        self.index, self.dlt = build_data_structures(corpus)

    def run(self):
        results = {}
        for query in self.queries:
            results[query[0]] = self.run_query(query[1])
        return results

    def run_query(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                doc_dict = self.index[term]  # retrieve index entry
                for doc_id, freq in doc_dict.items():  # for each document and its word frequency
                    score = BM25(number_docs=len(doc_dict), freq=freq, qf=1, r=0, N=len(self.dlt), doc_length=self.dlt.get_length(doc_id)
                                 ,average_doc_length=self.dlt.get_average_length())  # calculate score
                    if doc_id in query_result:  # this document has already been scored once
                        query_result[doc_id] += score
                    else:
                        query_result[doc_id] = score
        return query_result
