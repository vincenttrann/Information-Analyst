'''
INF 141 - Assignment 3 
By: Priscilla Chan & Vincent Tran
'''
import os
import sys


class InvertedIndex:

    def __init__(self):
        self.db = {}
        self.files = []

    
    def getData(self, path: 'directory path'):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.files.append(name)


    def parse_json(self, file):
        pass 


    def tokenize(self, content) -> list:
        pass 


    def stem(self, token) -> str:
        pass


    def add_to_db(self):
        pass 









if __name__ == '__main__':
    i = InvertedIndex() 
    path = sys.argv[1] 
    i.getData(path)