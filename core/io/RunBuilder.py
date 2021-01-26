from config.Config import ConfigFile


class RunBuilder:

    def __init__(self,
                 results,
                 group=ConfigFile().get_data_config("group"),
                 step=ConfigFile().get_run_config("step"),
                 w_func=ConfigFile().get_run_config("w_func"),
                 step_min=ConfigFile().get_run_config("step_min"),
                 search_level=ConfigFile().get_run_config("search_level"),
                 page_rank=ConfigFile().get_run_config("activate_page_rank"),
                 alpha=ConfigFile().get_run_config('alpha')
                 ):
        self.results = results
        self.group = group
        self.step = step
        self.step_min = step_min
        self.w_func = w_func
        self.search_level = search_level
        self.page_rank = page_rank
        self.alpha = alpha
        self.make_run()

    def make_run(self, path=ConfigFile().get_data_config("run_folder")):
        output_file = open(path +
                           self.group +
                           "_" + str(self.step) +
                           "_" + str(self.step_min) +
                           "_" + self.w_func +
                           "_alpha_" + str(self.alpha) +
                           "_page_rank" + self.search_level + ".txt", "w")
        for query in self.results:
            temp = dict(sorted(self.results[query].items(), key=lambda item: item[1], reverse=True))
            count = 1
            for doc_id in temp:
                output_file.write("{} {} {} {} {} {} {}\n"
                                  .format(query.strip(), "Q0", doc_id.strip(), count, temp[doc_id], self.group,
                                          "/article[1]"))
                count = count + 1
                if count == 1501:
                    break
