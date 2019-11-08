'''
INF 141 - Assignment 3 
By: Priscilla Chan & Vincent Tran
'''
import os
import sys
import re
from nltk.stem.porter import PorterStemmer
import json
from bs4 import BeautifulSoup


class InvertedIndex:

    docID = 0

    def __init__(self):
        self.db = {}
        self.files = []
        self.docID += 1

    
    #extracts all the files from a given directory
    def getData(self, path: 'directory path'):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.files.append(os.path.join(root,name))


    #parses json file into url and content tuple
    def parse_json(self, file) -> tuple:
        with open(file) as f:
            data = json.load(f) 
            return (data['url'], data['content']) 


    #tokenizer from assignment 1, might modify later
    def tokenize(self, content) -> list:
        tokens = []
        for line in content:
            line = line.strip().lower()
            words = re.findall("[\w]+", line, flags=re.ASCII)
            tokens.extend(words)
        return tokens 


    #Uses porter stemmer to normalize tokens
    def stem(self, tokens:list) -> list:
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]


    def parse_html(self):
        pass


    def add_to_db(self):
        pass 




if __name__ == '__main__':
    i = InvertedIndex() 
    path = sys.argv[1] 
    i.getData(path)
    