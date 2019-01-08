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
    print(data)
    print(data['total_score'])
    pipeline=[
            {'$group':{
                '_id':'$user_id',
                'total_score':{'$sum':'$score'},
                'total_time':{'$sum':'$submit_time'}
                }},
                {'$match':{
                    '$or':[
                        {'total_score':{'$gt':data['total_score']}},
                        {'total_time':{'$lt':data['total_time']},
                        'total_score':data['total_score']
                        } 
                        ]
                    }},
                {'$group':{'_id':None,'count':{'$sum':1}}}
                ]
    results=list(db.contests.aggregate(pipeline))
    print(results)
    if len(results)>0:
        rank=results[0]['count']+1
    else:
        rank=1
    return rank,data['total_score'],data['total_time']

if __name__ == '__main__':
    user_id=int(sys.argv[1])
    print(user_id)
    #get_rank(user_id)
    userdata = get_rank(user_id)
    print(userdata)
