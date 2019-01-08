#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    

    pipeline=[
            {'$match':{'user_id':user_id}},
            {'$group':{
                '_id':'$user_id',
                'total_score':{'$sum':'$score'},
                'total_time':{'$sum':'$submit_time'}
                }}
            ]
    results=list(db.contests.aggregate(pipeline))
    data=results[0]
    print(data['total_score'])
    pipeline=[
            {'$group':{
                '_id':'$user_id',
                'total_score':{'$sum':'$score'},
                'total_time':{'$sum':'$submit_time'}
                }}
                        ]
    results=list(db.contests.aggregate(pipeline))
    print(len(results))
if __name__ == '__main__':
    user_id=int(sys.argv[1])
    print(user_id)
    #get_rank(user_id)
    userdata = get_rank(user_id)
    print(userdata)
