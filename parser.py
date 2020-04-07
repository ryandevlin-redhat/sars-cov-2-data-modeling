# ==========================================================================================================
#
#   Simple parser class for generating dataframes representing the COVID-19 Open Research Dataset (CORD-19)
#
# ==========================================================================================================
import json
import pandas as pd
import glob
import os
import numpy as np
import multiprocessing


# This class assumes you have created a folder called 'dataset' within the directory of parser.py which contains the unzipped COVID-19 Open Research Dataset
class Parser():
    df_columns = ['paper_id', 'title', 'authors', 'abstract', 'body']
    unzipped_data_dir = "./dataset"

    def __init__(self):
        self.datapaths = self.get_datapaths() # a list of strings leading to folders containing json data files
                                              # The format of the json data files follows the conventions of json_schema.txt

    def get_datapaths(self):
        paths = [x[0] for x in os.walk(self.unzipped_data_dir)]
        return([item for item in paths if "json" in item])

    # This method builds a dataframe for the entire dataset
    def construct(self):
        df_dataset = pd.DataFrame(columns=self.df_columns)
        for datapath in self.datapaths:
            df_subset = self.construct_individual(datapath)
            df_dataset = pd.concat([df_dataset, df_subset], ignore_index=True)
        return(df_dataset)

    # This method builds a dataframe of papers in each json folder of the dataset
    def construct_individual(self, datapath):
        files = glob.glob(datapath + "/*.json")

        # Scale our processes to the number of cores on the machine
        # Potentially scale up to double number of cores because of I/O idling due to disk reads
        proc_count = min(2 * multiprocessing.cpu_count(), len(files))   
        pool = multiprocessing.Pool(processes=proc_count)
        
        results = pool.map(self.paper_to_dataframe, files)
        df_set = pd.concat(results, ignore_index=True)

        return(df_set)
      
    # This method builds a dataframe for a single paper formatted in the json_schema.txt format
    def paper_to_dataframe(self, file):
        with open(file) as f:
            data = json.loads(f.read())
            
            # Extract relevant paper data
            paper_id = data["paper_id"]
            title = data["metadata"]["title"]

            authors = ""
            for author in data["metadata"]["authors"]:
                authors += author["first"] + ":" + ' '.join(author["middle"]) + ":" + author["last"] + " "

            # some papers do not contain an abstract section, thus the try except
            abstract = ""
            try:
                for line in data["abstract"]:
                    abstract += (line["text"]) + " "
            except:
                abstract = np.nan
                # print("No abstract found for: " + file) # Debugging only

            body = ""
            for line in data["body_text"]:
                body += (line["text"]) + " "

            # Build a dictionary to create a dataframe object, we need to set each string value as a list to make pandas happy 
            data_dict = {"paper_id": [paper_id], "title": [title], "authors": [authors], "abstract": [abstract], "body": [body]}
            return(pd.DataFrame(data_dict))    

    # internal method for linking metadata from metadata.csv

    # Other internal helper methods