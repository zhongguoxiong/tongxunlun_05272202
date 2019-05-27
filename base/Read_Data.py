import sys

import yaml, os
sys.path.append(os.getcwd())
def ret_yaml_data(file_name):
    file_path = os.getcwd() + os.sep + "Data" + os.sep +file_name + ".yml"
    with open(file_path,"r") as f:
        return yaml.load(f)

def return_yaml_data(file_name):
    file_path=os.getcwd()+os.sep+"Data" + os.sep + file_name + ".yml"
    with open(file_path,"r") as f:
         return yaml.load(f)