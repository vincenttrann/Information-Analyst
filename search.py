'''
INF 141 - Assignment 3: Search
By: Priscilla Chan & Vincent Tran 
'''
import pickle
import os
from index import InvertedIndex, Posting
from nltk.stem.porter import PorterStemmer
from urllib.parse import urldefrag
from numpy import dot
from numpy.linalg import norm


class Search:

    def __init__(self, db, id_file):
        self.db = db 
        self.id_file = id_file

    
    def process_query(self, query:str) -> list:
        queryList = query.split("AND")
        stemmer = PorterStemmer() 
        tokens = [stemmer.stem(term.strip().lower()) for term in queryList]
        return tokens


    def merge(self, p1:list, p2:list) -> list:
        docid_1 = [p.doc_id for p in p1]
        return [posting for posting in p2 if posting.doc_id in docid_1]


    def get_results(self, query:list) -> list:
        postings = [self.db.get(term) for term in query] 
        postings.sort(key=len)
        if len(query) > 1:
            intersect = self.merge(postings[0], postings[1])
            for i in range(2, len(postings)):
                intersect = self.merge(intersect, postings[i])
            return intersect
        return postings[0]


    def display_results(self, urls:list):
        for i in range(5):
            print(urls[i]+"\n")


    def get_urls(self, postings: list):
        urls = []
        for posting in postings:
            defraged = urldefrag(self.id_file[posting.doc_id])[0]
            if defraged not in urls:
                urls.append(defraged)
        return urls


    def rank(self, postings:list) -> list:
        score = 0
        return sorted(postings, key=(lambda x: x.tf_idf), reverse=True)



if __name__ == '__main__':
    f1 = open('index.pkl', 'rb')
    db = pickle.load(f1)
    f2 = open('doc_id.pkl', 'rb') 
    ids = pickle.load(f2)
    while True:
        query = input('What would you like to search? (Enter q to quit)\n') 
        if query == 'q':
            f1.close() 
            f2.close()
            break 
        else:
            s = Search(db, ids)
            terms = s.process_query(str(query)) 
            results = s.get_results(terms) 
            rank = s.rank(results)
            urls = s.get_urls(rank) 
            s.display_results(urls) 

