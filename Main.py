from core.io.CorpusParser import CorpusParser
from core.io.QueryParser import QueryParser

from core.Engine import Engine
from core.io.RunBuilder import RunBuilder

if __name__ == "__main__":
    corpus = CorpusParser()
    queries = QueryParser()
    engine = Engine(queries.get_queries(), corpus.get_corpus())
    results = engine.run()

    builder = RunBuilder(results)

