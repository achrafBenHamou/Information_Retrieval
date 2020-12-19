import operator
import logging
from Parser import CorpusParser, QueryParser
from Query import Engine

if __name__ == "__main__":

    corpus = CorpusParser()
    queries = QueryParser()
    engine = Engine(queries.get_queries(),
                    corpus.get_corpus())
    results = engine.run()
    print(results)

    qid = 0
    for result in results:
        sorted_x = sorted(result, key=operator.itemgetter(1))
        sorted_x.reverse()
        index = 0
        for i in sorted_x[:100]:
            tmp = (qid, i[0], index, i[1])
            print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
            index += 1
        qid += 1
