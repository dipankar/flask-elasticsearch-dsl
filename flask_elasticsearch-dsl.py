from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search 
from flask import current_app, _app_ctx_stack

class ElasticSearchDSL(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ELASTICSEARCH_HOSTS', ['http://localhost'])
        app.teardown_appcontext(self.teardown)

    def connect(self):
        client = Elasticsearch(current_app.config['ELASTICSEARCH_HOSTS'])
        return Search(using=client)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'elasticsearch_dsl'):
            ctx.elasticsearch_dsl = None

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'elasticsearch_dsl'):
                ctx.elasticsearch_dsl = self.connect()
            return ctx.elasticsearch_dsl

