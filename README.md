# Information retrieval system
## Authors 
* Abou SANOU
* Ali Hani
* Achraf
* Amine RABHI

> This system is a small IRS. It uses the set of xml documents from INEX competition.
> We used a lot of ponderation function from [SMART system](https://en.wikipedia.org/wiki/SMART_Information_Retrieval_System).

In this summary, we will git the different process 


## Installation
Download the project from github repository [link](https://github.com/achrafBenHamou/Information_Retrieval)  

* From the root of the project launch the following command to install the required packages.

To install the required packages, you must run the following command from root of the project.
```sh
pip install -r requirements.txt
```

## Structure explaining :

In this section we will explain the organization of our project:
For more examples and usage, please refer to the [Wiki][wiki].

 * Config : this folder contains all of logic about the configuration of the system.
 * core : 
 * data :
 * documentation :
 * graph :
 * test :
   



## Explaining of the config.yml

The configuration allows to change easily the behaviors of the engine.
* _filename_ : in this line we have to specify the path of the text file containing the documents of collection.
* query : in this line we specify the path of request file where each line contains the request id and the request separate by ":".
* xml_folder : in this line we specify the path of the folder containing the xml files.
* run_folder : in this lin we specify where the runs generated will be stored.
* caching : activate the caching of the system. This feature allows to optimize the indexing of the documents. This feature allows to store the index in pkl file once computed.
* persist_index : the path of persitance of the index.
* persist_length : the path of persistance of the document length.
* persist_page_rank : the path of persistance of the graph of the page_rank
* group : the name of the group needed in the run file.
* use_xml_file : use xml file or text file.


* alpha :
* step :
* step_min :
* w_func :
* search_level :
* activate_page_rank :
* granularity :
```text
data:
    filename: data/Text_Only_Ascii_Coll_MWI_NoSem
    query: data/query/request.txt
    xml_folder: data/coll/
    run_folder: data/runs/last_runs/
    caching: False
    persist_index: data/persist/data_index.pkl
    persist_length: data/persist/data_length.pkl
    persist_page_rank: data/persist/page_rank.pkl
    group: AbouAchrafAmineAli
    use_xml_file : True
run_step:
    alpha: 6
    step: 2
    step_min: 4
    w_func: bm25
    search_level: k1_1.2_b_0.75_k2_100_variant_p_r_articles
    activate_page_rank: True
    granularity: articles
```

## Release History

## Meta


## Contributing

1. Fork it (<https://github.com/achrafBenHamou/Information_Retrieval>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
