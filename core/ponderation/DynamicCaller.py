from core.ponderation.tf_w_func import b, n, m, a, s, l


class DynamicCaller:
    def __init__(self, function_name):
        self.function_name = list(function_name)
        self.tf_function = self.import_from('core.ponderation.tf_w_func', self.function_name[0])
        self.idf_function = self.import_from('core.ponderation.idf_w_func', self.function_name[1])
        self.norm_function = self.import_from('core.ponderation.norm_w_func', self.function_name[2])
        self.list_require = self.tf_function.__code__.co_varnames + self.idf_function.__code__.co_varnames + self.norm_function.__code__.co_varnames

    def import_from(self, module, name):
        module = __import__(module, fromlist=[name])
        return getattr(module, name)

    def get_require_argument(self):
        return self.list_require