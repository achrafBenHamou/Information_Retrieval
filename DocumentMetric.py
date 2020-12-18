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
