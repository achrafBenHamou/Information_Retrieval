from core.io.CorpusParser import CorpusParser
from core.io.QueryParser import QueryParser

from core.Engine import Engine
from core.io.RunBuilder import RunBuilder
from core.ponderation.DynamicCaller import DynamicCaller

if __name__ == "__main__":
    test = DynamicCaller("ltn")
    print(test.get_require_argument())
    corpus = CorpusParser()
    queries = QueryParser()
    engine = Engine(queries.get_queries(), corpus.get_corpus())
    results = engine.run()
    print(results)
    for query in results:
        temp = dict(sorted(results[query].items(), key=lambda item: item[1], reverse=True))
        print(temp)
    builder = RunBuilder(results)
