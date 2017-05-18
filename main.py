# -*- coding: UTF-8 -*-
import sys
import web

from db_action import db_action

from index import index_html_string
from api_list_manage import get_no_filted_html_string
from api_list_manage import post_selected_api_list_html_string
from api_add_page import get_add_an_api_html_string
from utility import *

reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'index',
    '/show_apis', 'show_api_list',
    '/change_status', 'change_status',
    '/new_a_api', 'new_a_api'
)

class index:
    def GET(self):
        return index_html_string

class show_api_list:
    def GET(self):
        d_a = db_action()
        result_set = d_a.get_all_api_list()
        return get_no_filted_html_string(result_set)
    def POST(self):
        d_a = db_action()
        i = web.input('module')
        result_set = d_a.get_api_list_by_module_id(i.module)
        return post_selected_api_list_html_string(result_set)

class change_status:
    def POST(self):
        i = web.input('r_id')
        print i.r_id
        d_a = db_action()
        d_a.change_api_status(i.r_id)
        return web.seeother('/show_apis')

class new_a_api:
    def GET(self):
        return get_add_an_api_html_string()
    def POST(self):
        d_a = db_action()
        module = web.input('api_add_module')
        module_name = make_module_name(module.api_add_module)
        api = web.input('api_add_name')
        method = web.input('api_http_method')
        url = web.input('api_add_url')
        cmt = web.input('api_add_cmt')
        parameters = web.input('parameter_list')
        max_id = d_a.get_max_id()
        max_specific_module_id = d_a.get_max_specific_module_id(module.api_add_module)
        wanted_id = make_id_key(max_id)
        wanted_max_specific_module_id = make_module_id(max_specific_module_id)
        wanted_table_name = make_table_name(module.api_add_module, wanted_max_specific_module_id)
        print make_insert_sql(module.api_add_module,module_name,api,method,url,cmt,wanted_id, wanted_max_specific_module_id,wanted_table_name)
        return web.seeother('/show_apis')

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()