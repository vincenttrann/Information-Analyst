'''
INF 141 - Assignment 3 
By: Priscilla Chan & Vincent Tran
'''
import os
import sys
import re
import nltk


class InvertedIndex:

    def __init__(self):
        self.db = {}
        self.files = []

    
    #extracts all the files from a given directory
    def getData(self, path: 'directory path'):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.files.append(name)


    def parse_json(self, file):
        pass 


    #tokenizer from assignment 1, might modify later
    def tokenize(self, content) -> list:
        tokens = []
        for line in content:
            line = line.strip().lower()
            words = re.findall("[\w]+", line, flags=re.ASCII)
            tokens.extend(words)
        return tokens 


    def stem(self, token) -> str:
        pass


    def add_to_db(self):
        pass 









if __name__ == '__main__':
    i = InvertedIndex() 
    path = sys.argv[1] 
    i.getData(path)