from config.Config import ConfigFile


class RunBuilder:

    def __int__(self, results, group="AbouAchrafAmineAli"):
        self.results = results
        self.group = group
        self.step = ConfigFile.get_run_config("step")
        self.step_min = ConfigFile.get_run_config("step_min")
        self.w_func = ConfigFile.get_run_config("w_func")
        self.search_level = ConfigFile.get_run_config("search_level")

    def build_run(self, results):
        path = ConfigFile().get_data_config("run_folder")
        output_file = open(path +
                           self.group +
                           "_" + self.step +
                           "_" + self.step_min +
                           "_" + self.w_func +
                           "_" + self.search_level +
                           ".txt", "a")

    def write_in_file(self, results,output_file):

        output_file.write("{} {} {} {} {} {} {}\n".format("req", "Q0", "max_doc[0]", "i", "max_doc[1]", self.group, "/article[1]"))

