# -*- coding: UTF-8 -*-
import sys
import web

from db_action import db_action

from index import index_html_string
from api_list_manage import get_no_filted_html_string
from api_list_manage import post_selected_api_list_html_string
from api_add_page import get_add_an_api_html_string
from case_manage import get_test_case_filter_html_string
from case_manage import get_module_filted_html_string
from case_manage import get_api_filter_html_string
from case_manage import get_add_test_case_page_html_string
from case_manage import get_edit_case_page_html_string
from test_plan_manage import show_all_test_plan_html_string
from utility import *

reload(sys)
sys.setdefaultencoding('utf8')

global selected_interface_id

urls = (
    '/', 'index',
    '/show_apis', 'show_api_list',
    '/change_status', 'change_status',
    '/new_a_api', 'new_a_api',
    '/show_test_cases', 'show_test_cases',
    '/delete_test_case', 'delete_a_test_case',
    '/add_test_case', 'add_a_test_case',
    '/submit_add_test_case', 'submit_add_test_case',
    '/modify_test_case', 'modify_a_test_case',
    '/submit_modify_test_case', 'submit_modify_test_case',
    '/show_test_plan', 'show_test_plan',
    '/delete_test_plan', 'delete_a_test_plan',
    '/show_test_case_list', 'show_active_test_case'
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
        # print i.r_id
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
        wanted_table_name = make_table_name(module_name, wanted_max_specific_module_id)
        sql_string = make_insert_sql(module.api_add_module,module_name,api.api_add_name,method.api_http_method,url.api_add_url,cmt.api_add_cmt,wanted_id, wanted_max_specific_module_id,wanted_table_name)
        d_a.sql_execution(sql_string)
        create_api_table_sql_string =  make_create_table_sql(wanted_table_name, parameters.parameter_list)
        d_a.sql_execution(create_api_table_sql_string)
        return web.seeother('/show_apis')

class show_test_cases:
    def GET(self):
        return get_test_case_filter_html_string()
    def POST(self):
        d_a = db_action()
        module = web.input('module_list')
        api = web.input('api_list')
        result_set = d_a.get_apis_by_module_id(module.module_list)
        if api.api_list == 'default':
            # print "test flag"
            return get_module_filted_html_string(module.module_list, result_set)
        else:
            return get_api_filter_html_string(module.module_list, result_set, api.api_list)

class delete_a_test_case:
    def GET(self):
        return get_test_case_filter_html_string()
    def POST(self):
        i = web.input('c_id')
        j = web.input('a_id')
        # print i.c_id
        # print j.a_id
        d_a = db_action()
        d_a.delete_case_by_api_and_id(j.a_id, i.c_id)
        return get_test_case_filter_html_string()

class add_a_test_case:
    # it should be migration with the below interface, otherwise the selected_interface_id will be blocked
    def POST(self):
        i = web.input('api_id_new')
        global selected_interface_id
        selected_interface_id = i.api_id_new
        return get_add_test_case_page_html_string(i.api_id_new)

class submit_add_test_case:
    def POST(self):
        l = web.input()
        parameter_name_list = []
        parameter_value_list = []
        for element in l:
            parameter_name_list.append(element)
            parameter_value_list.append(l[element])
        d_a = db_action()
        wanted_id = d_a.get_max_id_from_specific_table(selected_interface_id)
        # print wanted_id
        # print parameter_name_list
        # print parameter_value_list
        d_a.insert_test_case_into_specific_table(selected_interface_id, parameter_name_list, parameter_value_list, str(wanted_id))
        return get_test_case_filter_html_string()

class modify_a_test_case:
    def POST(self):
        i = web.input()
        api_id = i.a_id
        case_id = i.c_id
        d_a = db_action()
        # print api_id
        # print case_id
        l = d_a.get_specific_test_case(api_id, case_id)
        test_case_info = l[0]
        col_name_list = l[1]
        test_case = l[2]
        # print test_case_info
        # print col_name_list
        # print test_case
        return get_edit_case_page_html_string(api_id, case_id, col_name_list, test_case, test_case_info)


class submit_modify_test_case:
    def POST(self):
        i = web.input()
        a_id = i.a_id
        c_id = i.c_id
        parameter_name_list = []
        parameter_value_list = []
        for element in i:
            if element != 'a_id' and element != 'c_id':
                parameter_name_list.append(element)
                parameter_value_list.append(i[element])
        # print parameter_name_list
        # print parameter_value_list
        # print a_id
        # print c_id
        d_a = db_action()
        d_a.update_test_case_specific_table(a_id, c_id, parameter_name_list, parameter_value_list)
        return get_test_case_filter_html_string()


class show_test_plan:
    def GET(self):
        d_a = db_action()
        test_plan_list = d_a.get_test_plan_list()
        return show_all_test_plan_html_string(test_plan_list)


class delete_a_test_plan:
    def POST(self):
        i = web.input()
        test_plan_id = i.test_plan_id
        d_a = db_action()
        d_a.delete_test_plan(test_plan_id)
        return web.seeother('/show_test_plan')

class show_active_test_case:
    def POST(self):
        i = web.input()
        module_id = i.module_id
        test_plan_id = i.test_plan_id
        d_a = db_action()
        active_test_case = d_a.get_active_case_string(test_plan_id)
        if active_test_case == '0':
            case_string = []
            tb_name_list = d_a.get_table_name_list_by_module_id(module_id)
            for tb_name in tb_name_list:
                tc_id_list = d_a.get_test_case_list(tb_name[0])
                for tc_id in tc_id_list:
                    case_element_string = tb_name[0]+":"+tc_id[0]
                    case_string.append(case_element_string)
            return case_string
        else:
            return 0

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
