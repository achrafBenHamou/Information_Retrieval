class InvertedIndex:

    def __init__(self):
        self.payload = dict()

    def __contains__(self, item):
        return item in self.index

    def __getitem__(self, item):
        return self.index[item]

    def add(self, word, doc_id):
        if word in self.index:
            if doc_id in self.index[word]:
                self.index[word][doc_id] += 1
            else:
                self.index[word][doc_id] = 1
        else:
            dict_word = dict()
            dict_word[doc_id] = 1
            self.index[word] = dict_word

    def get_document_frequency(self, word, doc_id):
        if word in self.index:
            if doc_id in self.index[word]:
                return self.index[word][doc_id]
            else:
                raise LookupError('%s not in document %s' % (str(word), str(doc_id)))
        else:
            raise LookupError('%s not in index' % str(word))

    def get_index_frequency(self, word):
        """
        :param word: the word
        :return: number of document contained the word
        """
        if word in self.index:
            return len(self.index[word])
        else:
            raise LookupError('%s not in index' % word)
