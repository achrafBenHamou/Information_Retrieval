from config.Config import ConfigFile


class InvertedIndex:

    def __init__(self):
        # word -> [ doc1, doc2 , doc3]
        # word1 -> [doc1]
        self.payload = dict()

    def __contains__(self, item):
        return item in self.payload

    def __getitem__(self, item):
        return self.payload[item]

    def __str__(self):
        return self.payload

    def persist(self):
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(ConfigFile().get_data_config("persist_index"), 'wb') as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, path=ConfigFile().get_data_config("persist_index")):
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(path, 'wb') as file:
            self.payload = pickle.load(file)

    def add(self, word, doc_id):
        if word in self.payload:
            if doc_id in self.payload[word]:
                self.payload[word][doc_id] += 1
            else:
                self.payload[word][doc_id] = 1
        else:
            dict_word = dict()
            dict_word[doc_id] = 1
            self.payload[word] = dict_word

    def get_document_frequency(self, word, doc_id):
        if word in self.payload:
            if doc_id in self.payload[word]:
                return self.payload[word][doc_id]
            else:
                raise LookupError('%s not in document %s' % (str(word), str(doc_id)))
        else:
            raise LookupError('%s not in index' % str(word))

    def get_index_frequency(self, word):
        """
        :param word: the word
        :return: number of document contained the word
        """
        if word in self.payload:
            return len(self.payload[word])
        else:
            raise LookupError('%s not in index' % word)
    @staticmethod
    def get_instance():
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(ConfigFile().get_data_config("persist_index"), 'rb') as file:
            return pickle.load(file)
