from config.Config import ConfigFile


class RunBuilder:

    def __init__(self,
                results,
                group="AbouAchrafAmineAli",
                step=ConfigFile().get_run_config("step"),
                w_func=ConfigFile().get_run_config("w_func"),
                step_min=ConfigFile().get_run_config("step_min"),
                search_level=ConfigFile().get_run_config("search_level")
                ):
        self.results = results
        self.group = group
        self.step = step
        self.step_min = step_min
        self.w_func = w_func
        self.search_level = search_level
        self.display()

    def display(self):
        for query in self.results:
            temp = dict(sorted(self.results[query].items(), key=lambda item: item[1], reverse=True))
            for item in temp:

            print(temp)

    def build_run(self, results):
        path = ConfigFile().get_data_config("run_folder")
        output_file = open(path +
                           self.group +
                           "_" + self.step +
                           "_" + self.step_min +
                           "_" + self.w_func +
                           "_" + self.search_level +
                           ".txt", "a")

    def write_in_file(self, results, output_file, req, count):
        output_file.write("{} {} {} {} {} {} {}\n"
                          .format("req", "Q0", "max_doc[0]", "i", "max_doc[1]", self.group, "/article[1]"))
