from core.Engine import Engine
from core.io.RunBuilder import RunBuilder

from core.io.CorpusParser import CorpusParser
from core.io.QueryParser import QueryParser


if __name__ == "__main__":
    corpus = CorpusParser()
    queries = QueryParser()
    engine = Engine(queries.get_queries(), corpus.get_corpus(), corpus.page_rank)
    results = engine.run()
    print("")
    print(results)
    builder = RunBuilder(results)