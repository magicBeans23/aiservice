from elasticsearch import Elasticsearch
from django.conf import settings

_elastic_server = settings.ELASTIC_SERVER
_elastic_index = settings.ELASTIC_INDEX
_es = Elasticsearch([_elastic_server])


def ingest(doc, idt=None):
    if settings.ELASTIC:
        _es.index(index=_elastic_index, id=idt, body=doc)
