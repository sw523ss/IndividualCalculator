import csv
from pprint import pprint
from pathlib import Path

def classFactory (class_name, dictionary):
    return type(class_name, (object,), dictionary)


