from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from elasticsearch import helpers
# Create your views here.

def index():
    """ INDEX """
    return HttpResponse("Hello word. This is so Fast to make site")

def scan(index_nm):
    """ scan """

    es_node = Elasticsearch(
        [
            {'host':'192.168.110.148', 'port':'9200'}
        ],
        sniffer_timeout=60
    )
    
