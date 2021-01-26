author__ = 'Abou SANOU'
import os
from config.Config import ConfigFile


def caching_files_exist(index_path=ConfigFile().get_data_config("persist_index"),
                        length_table=ConfigFile().get_data_config("persist_length")):
    return os.path.isfile(index_path) and os.path.isfile(length_table)


def persit_dict_page_rank(my_dict):
    import json
    file = open(ConfigFile().get_data_config("persist_page_rank"), 'w')
    json.dump(my_dict, file)


def load_dict_page_rank():
    import json
    file = open(ConfigFile().get_data_config("persist_page_rank"), 'r')
    my_dict = json.load(file)
    return my_dict
