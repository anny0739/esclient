import json
import logging
from elasticsearch import Elasticsearch, helpers
from elasticsearch.client import ClusterClient
from .models import ItSearchAllGoods


# Create your views here.
# -*- coding: utf-8 -*-
class Indexer(object):
    """
    Indexer Class
    """
    logger = logging.getLogger(__name__)

    def __init__(self, index_nm):
        self.es_storage = Elasticsearch(
            [
                {'host':'http://verify.ezwel.com/esclient', 'port':'9200'}
            ],
            sniffer_timeout=60
        )
        self.index_nm = index_nm

    def bulk(self):
        """
        Get All of Goods Data In DB
        To Elasticsearch
        """
        type_nm = 'goods'
        all_goods = ItSearchAllGoods.objects.all()
        bulk_data = []

        id_count = json.dumps(self.es_storage.count(self.index_nm))

        #bulk_data.append({'doc' : {'goods_seq' : 12345L}})
        count = json.loads(id_count)['count'] + 1
        for element in all_goods:
            count += int(count)
            data_dict = {
                "goods_seq" : element.goods_seq,
                "goods_nm" : element.goods_nm,
                "goods_sub_nm" : element.goods_sub_nm,
                "goods_sale_st" : element.goods_sale_st.replace('.', ''),
                "goods_sale_ed" : element.goods_sale_ed.replace('.', ''),
                "goods_special_price" : element.goods_special_price,
                "goods_sale_price" : element.goods_sale_price,
                "region_name" : element.region_name,
                "img_path" : element.img_path,
                "goods_region_nm" : element.goods_region_nm,
                "goods_gubun" : element.goods_gubun,
                "acc_region" : element.acc_region,
                "reg_dt" : element.reg_dt,
                "modi_dt" : element.modi_dt,
                "accommodation_keyword" : element.accommodation_keyword,
                "use_yn" : element.use_yn
            }

            ix_dict = {
                '_op_type': 'create',
                '_index': str(self.index_nm),
                '_type': str(type_nm),
                '_id': count,
                '_source': data_dict
            }

            bulk_data.append(ix_dict)

        # es_node.bulk(index=index_nm, body=bulk_data, refresh = True)

        try:
            helpers.bulk(self.es_storage, bulk_data)
        except Exception as e:
            print e
        return "SUCCESS"

    def health(self, index_nm):
        """
        check cluster health
        """

        return ClusterClient(self.es_storage).health(index_nm)

    def exist(self, request):
        """
        check goods is exist
        curl -XGET es:9200/index_nm/type_nm/_search?_source&q=goods_seq:goods_seq

        @param : cond_match ex {"goods" : goods}
        """
        print request.GET['goods_nm']
        body = {
            "_source" : True,
            "query" : {
                "term" : {
                    "goods_nm" : request.GET['goods_nm']
                }
            }
        }
        #return json.dumps(self.es_storage.count(self.index_nm))
        search_result = self.es_storage.search(index=self.index_nm,
                                               doc_type="goods",
                                               body=body)
        if search_result != None:
            search_result = json.dumps(search_result)
        return search_result


"""
curl -XPUT 'http://localhost:9200/jongdalsae/' -d '
		{
			"mappings" : {
			"goods": {
            "properties" : {
                "goods_seq": {"type" : "integer",  "index" : "not_analyzed"},
                "goods_nm": {"type" : "text",  "index" : "analyzed",
                             "search_analyzer":"korean_index",
                             "analyzer":"korean_index",
                             "fields" : {
                                 "name" : {
                                     "type" : "text",  "index" : "not_analyzed"
                                 },
                                 "tk" : {
                                     "type" : "text",  "index" : "not_analyzed"
                                 },
                                 "code" : {
                                     "type" : "text",  "index" : "not_analyzed"
                                 }
                             }},
                "goods_sub_nm" : {"type" : "text",  "index" : "analyzed"},
                "goods_sale_st" : {"type" : "date",  "index" : "not_analyzed"},
                "goods_sale_ed" : {"type" : "date",  "index" : "not_analyzed"},
                "goods_special_price" : {"type" : "integer", 
                                         "index" : "not_analyzed"},
                "goods_sale_price" : {"type" : "integer", 
                                      "index" : "not_analyzed"},
                "region_name" : {"type" : "text",  "index" : "not_analyzed"},
                "img_path" : {"type" : "text",  "index" : "not_analyzed"},
                "goods_region_nm" : {"type" : "text",  "index" : "not_analyzed"},
                "goods_gubun" : {"type" : "text",  "index" : "not_analyzed"},
                "reg_dt" : {"type" : "text",  "index" : "not_analyzed"},
                "modi_dt" : {"type" : "text",  "index" : "not_analyzed"},
                "accommodation_keyword" : {"type" : "text", 
                                           "index" : "not_analyzed"},
                "use_yn" : {"type" : "text",  "index" : "not_analyzed"}
          	  }
      	    }
      	  }
     	,
     	    "settings" : {
        "index" : {
            "number_of_shards" : 3, 
            "number_of_replicas" : 2 
        },
        "analysis" : {
   				"analyzer" : {
      		"korean_index" : {
         		"type" : "keyword"
      }
   }
}
    }
  }
    
'

"""