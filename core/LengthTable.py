from config.Config import ConfigFile


class LengthTable:
    """
    This class will contained some information about each document
    :length
    :average_length of all documents
    """
    def __init__(self):
        self.table = dict()

    def __len__(self):
        return len(self.table)

    def persist(self):
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(ConfigFile().get_data_config("persist_length"), 'wb') as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)

    def __contains__(self, item):
        return item in self.table

    def add(self, doc_id, length):
        self.table[doc_id] = length

    def get_length(self, doc_id):
        if int(doc_id) in self.table.keys():
            return self.table[int(doc_id)]
        else:
            raise LookupError('%s not found in table' % str(doc_id))

    def get_average_length(self):
        sum = 0
        for length in self.table.values():
            sum += length
        return float(sum) / float(len(self.table))

    @staticmethod
    def get_instance():
        try:
            import cPickle as pickle
        except ImportError:  # Python 3.x
            import pickle
        with open(ConfigFile().get_data_config("persist_length"), 'rb') as file:
            return pickle.load(file)
