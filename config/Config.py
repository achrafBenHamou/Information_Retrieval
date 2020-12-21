import io


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigFile(metaclass=Singleton):
    def __init__(self):
        import yaml
        with open("config.yml", "r") as file:
            self.cfg = yaml.load(file, Loader=yaml.FullLoader)

    def get_data_config(self, item):
        return self.cfg["data"][item]
