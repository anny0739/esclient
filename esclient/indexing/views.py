from django.shortcuts import render
from django.http import HttpResponse
from .indexer import Indexer

# Create your views here.
# -*- coding: utf-8 -*-    

def bulk(request, index_nm):
    """
    bulk
    """
    if index_nm is None:
        return render(request, "indexing/error.html", "YOU HAVE TO INPUT INDEX_NM")

    ixer = Indexer(index_nm)
    result = ixer.bulk()
    return HttpResponse(result)
    #return render(request, 'indexing/templates/success.html', {"result_msg" : result})

def search(request, index_nm):
    """
    test search
    """
    search_result = Indexer(index_nm).exist(request)
    print search_result
    return HttpResponse(Indexer(index_nm).exist(request))



