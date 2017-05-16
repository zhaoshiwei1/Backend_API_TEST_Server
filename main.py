# -*- coding: UTF-8 -*-
import sys
import web

from db_action import db_action

from index import index_html_string
from api_list_manage import get_no_filted_html_string
from api_list_manage import post_selected_api_list_html_string

reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'index',
    '/show_apis', 'show_api_list',
    '/change_status', 'change_status'
)

class index:
    def GET(self):
        return index_html_string

class show_api_list:
    def GET(self):
        return get_no_filted_html_string()
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

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()