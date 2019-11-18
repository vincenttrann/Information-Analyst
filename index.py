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
from collections import defaultdict
import pickle


class Posting:

    def __init__(self, doc_id, tf_idf, fields):
        self.doc_id = doc_id 
        self.tf_idf = tf_idf
        self.fields = fields


    def update_idf(self, tf, idf):
        pass


class InvertedIndex:

    def __init__(self):
        self.db = defaultdict(list)
        self.files = []
        self.doc_id = 0

    
    #extracts all the files from a given directory
    def getData(self, path: 'directory path'):
        for root, dirs, files in os.walk(path):
            for name in files:
                self.files.append(os.path.join(root, name))


    #parses json file into url and content tuple
    def parse_json(self, file) -> tuple:
        with open(file) as f:
            data = json.load(f) 
            return (data['url'], data['content']) 


    #tokenizer from assignment 1, might modify later
    def tokenize(self, content) -> list:
        tokens = []
        for line in content.split("\n"):
            line = line.strip().lower()
            words = re.findall("[\w]+", line, flags=re.ASCII)
            tokens.extend(words)
        return tokens 


    #Uses porter stemmer to normalize tokens
    def stem(self, tokens:list) -> list:
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]


    def get_text(self, doc):
        soup = BeautifulSoup(doc, 'html.parser') 
        return soup.get_text()


    #parse the html provided in content section of json file
    #for now, just retreiving all the text 
    #will deal with titles/headers/bold text later
    def parse_html(self, html_doc:str, tokens:list) -> dict:
        soup = BeautifulSoup(html_doc, 'html.parser') 
        token_dict = defaultdict(set)
        for item in soup.find_all():
            for token in sorted(set(tokens)):
                if item.name == 'title' or item.name == 'body' \
                    or re.match('^h[1-3]$',item.name) or item.name == 'b':
                    token_dict[token].add(item.name)
        return token_dict


    #adds files to database
    def add_to_db(self):
        with open("doc_id.txt", "w", encoding="utf-8") as f:
            for file in self.files:
                self.doc_id+=1
                doc_id =  self.doc_id 
                name = self.parse_json(file)[0]
                content = self.parse_json(file)[1] 
                html_doc = self.get_text(content)
                tokens = self.stem(self.tokenize(html_doc))
                fields_dict = self.parse_html(content, tokens) 
                f.write(str(doc_id)+" "+str(name)+"\n")
                for token in sorted(set(tokens)):
                    count = tokens.count(token) 
                    fields = list(fields_dict[token])
                    self.db[token].append(Posting(doc_id, count, fields))


    def get_db(self):
        return self.db



if __name__ == '__main__':
    i = InvertedIndex() 
    path = sys.argv[1] 
    i.getData(path)
    i.add_to_db()
    db = i.get_db() 
    with open('index.pkl', 'wb') as f:
        pickle.dump(db, f)
    print("Done!")
    

    