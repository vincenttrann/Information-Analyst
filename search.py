'''
INF 141 - Assignment 3: Search
By: Priscilla Chan & Vincent Tran 
'''
import pickle
import os
from index import Posting


class Search:

    def __init__(self, db):
        self.db = db 

    
    def process_query(self, query):
        queryList = query.split()
        if "AND" in queryList:
            pass 
        return


    def merge(self, p1, p2):
        answer = [] 
        post = self.longer(p1, p2) 
        for p in post: 
            if p1.doc_id == p2.doc_id:
                answer.append(p1.doc_id) 
            elif p1.doc_id < p2.doc_id:
                continue 
            else:
                continue 
        return answer


    def longer(self, p1, p2):
        if p1.length > p2.length:
            return p1 
        else:
            return p2 


    def get_results(self):
        pass 


    def display_results(self):
        pass



if __name__ == '__main__':
    while True:
        query = input('What would you like to search? (Enter q to quit)\n') 
        if query == 'q':
            break 
        else:
            db = open('index.pkl', 'rb')
            pickle.load(db)
            s = Search(db)

