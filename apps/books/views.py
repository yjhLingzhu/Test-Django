from django.shortcuts import render
from elasticsearch import Elasticsearch
import json
from django.http import HttpResponse

from books.models import Book

es = Elasticsearch(hosts="8.135.13.128",
                   port=10187,
                   http_auth=('mysql_writer', ''))


# Create your views here.


def index(requset):
    if requset.method == "GET":
        # page = 1
        response = es.search(
            index="th-pytoes-publicitycompany-no-analyzer",
            body={
                "track_total_hits": True,
                "query": {
                    "bool": {
                        "must": [],
                        "filter": [
                            {
                                "bool": {
                                    "should": [
                                        {
                                            "match_phrase": {
                                                "company": {
                                                    "query": "新世纪彩艺包装有",
                                                }
                                            }
                                        }
                                    ],
                                    "minimum_should_match": 1
                                }
                            },
                            # {
                            #     "range": {
                            #         "@timestamp": {
                            #             "gte": "2021-11-01T16:00:00.000Z",
                            #             "lte": "2021-11-02T15:59:59.999Z",
                            #             "format": "strict_date_optional_time"
                            #         }
                            #     }
                            # }
                        ],
                        "should": [],
                        "must_not": [
                            {
                                "match_phrase": {
                                    "user.name": "ccw40query"
                                }
                            }
                        ]
                    }
                },
                "version": True,
                # "from": (page - 1) * 50,
                "size": 5,
                "sort": [
                    {
                        "@timestamp": {
                            "order": "desc",
                            "unmapped_type": "boolean"
                        }
                    }
                ]
            }
        )
        print(response)
        print(json.dumps(response, indent=4, ensure_ascii=False))
        return render(requset, "index.html")


def test_model(requset):
    a = Book()
    # 获取分表数据
    b = Book._meta.db_table
    obj = Book.objects.filter(id=1).first()
    # print("b: ", b, "obj: ", obj.__dict__)

    db_table = Book.get_app_log_model("test")
    print("new: ", db_table, db_table._meta.db_table)
    result = db_table.objects.filter(id=2).first()
    print("result: ", result, result.__dict__)
    return HttpResponse("ni")


def parse_model(request):
    from django.core import serializers
    instance = Book.objects.first()
    data = serializers.serialize("json", [instance])
    # print(data)
    sql = """select * from test_books_book limit 2, 2"""
    res = Book.objects.raw(sql)
    print("res: ", len(res))
    for each in res:
        print(each.__dict__)
    return HttpResponse("ni123")
