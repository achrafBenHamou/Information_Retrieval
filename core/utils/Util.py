import os

from config.Config import ConfigFile


def caching_files_exist(index_path=ConfigFile().get_data_config("persist_index"), length_table=ConfigFile().get_data_config("persist_length")):
    return os.path.isfile(index_path) and os.path.isfile(length_table)
