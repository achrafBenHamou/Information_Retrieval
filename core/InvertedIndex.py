from config.Config import ConfigFile
class InvertedIndex:

    def term_in_doc(self, term, doc_id):
        if self.payload[term]:
            if self.payload[term][doc_id]:
                return self.payload[term][doc_id]
            else:
                return 0
        else:
            return 0

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

    def term_freq_doc(self, word, doc_id):
        if word in self.payload:
            if doc_id in self.payload[word]:
                return self.payload[word][doc_id]
            else:
                return 0
        else:
            return 0

    def tf(self, word, doc_id, doc_len):
        #return self.term_freq_doc(word, doc_id)/doc_len
        return self.term_freq_doc(word, doc_id)

    def get_index_frequency(self, word):
        """
        :param word: the word
        :return: number of document contained the word
        """
        if word in self.payload:
            return len(self.payload[word])
        else:
            raise LookupError('%s not in index' % word)

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

    @staticmethod
    def get_instance():
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(ConfigFile().get_data_config("persist_index"), 'rb') as file:
            return pickle.load(file)
