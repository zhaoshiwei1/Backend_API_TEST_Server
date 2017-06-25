# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# from db_action import db_action

def make_id_key(max_id):
    return str(max_id+1)


def make_module_id(max_specific_module_id):
    if max_specific_module_id<9:
        return "0" + str(max_specific_module_id+1)
    else:
        return str(max_specific_module_id+1)


def make_table_name(module_name, specific_module_id):
    return module_name + specific_module_id


def make_module_name(module_id):
    values = {
        "01":"ORDER",
        "02":"CHARGER",
        "03":"SETTLEMENT",
        "04":"PAY",
        "05":"UC"
    }

    return values[module_id]


def make_insert_sql(module_id, module_name, api_name, http_method, url, cmt, wanted_id, wanted_max_specific_module_id,
                    wanted_table_name):
    sql_string = """INSERT INTO general VALUES("""
    sql_string += ("\'" + wanted_id + "\',")
    sql_string += ("\'" + module_id + "\',")
    sql_string += ("\'" + module_name + "\',")
    sql_string += ("\'" + wanted_max_specific_module_id + "\',")
    sql_string += ("\'" + api_name + "\',")
    sql_string += ("\'" + cmt + "\',")
    sql_string += ("\'" + wanted_table_name + "\',")
    sql_string += ("\'" + http_method + "\',")
    sql_string += ("\'" + url + "\',")
    sql_string += """'YES') """
    return sql_string


def make_create_table_sql(table_name, parameters_string):
    create_table_string = """"""
    parameter_list = parameters_string.split("#")
    create_table_string += """CREATE TABLE """ + table_name
    create_table_string += """(TEST_CASE_ID TEXT NOT NULL,"""
    for parameter in parameter_list:
        create_table_string += parameter + """  TEXT NOT NULL,"""
    create_table_string += """PRIMARY KEY (TEST_CASE_ID))"""
    return create_table_string


def make_insert_sql_by_selected_api_id(tb_name, wanted_id, parameter_name_list, parameter_value_list):
    sql_string = """INSERT INTO """ + tb_name + """ ( TEST_CASE_ID, """
    parameter_length = len(parameter_name_list)
    value_length = len(parameter_value_list)
    i = 0
    j = 0
    if parameter_length == value_length:
        for p_name in parameter_name_list:
            i += 1
            if i < parameter_length:
                sql_string += p_name + """ ,"""
            else:
                sql_string += p_name + """) """
        sql_string += """VALUES (""" + "\'" +wanted_id+"\', "
        for p_value in parameter_value_list:
            j += 1
            if j < value_length:
                sql_string += "\'" + p_value + "\', "
            else:
                sql_string += "\'" + p_value + "\')"
        return sql_string
    else:
        return "PARAMETER ERROR"


def make_update_sql(tb_name, case_id, parameter_name_list, parameter_value_list):
    sql_string = """UPDATE """ + tb_name + """ SET """
    for i in range(0, len(parameter_name_list)):
        if i != (len(parameter_name_list)-1):
            sql_string += parameter_name_list[i] + " = " + "\'"+parameter_value_list[i]+"\', "
        else:
            sql_string += parameter_name_list[i] + " = " + "\'"+parameter_value_list[i]+"\' "
    sql_string += """WHERE TEST_CASE_ID = """ + "\'" + case_id + "\'"
    return sql_string


def make_test_report_string(base_url, api_url, http_method, parameter_name_list, parameter_value_list, response_string):
    temp = ""
    temp += format_line("BASE_URL", base_url) + "\r\n"
    temp += format_line("API_URI", api_url) + "\r\n"
    temp += format_line("HTTP_METHOD", http_method) + "\r\n"
    for i in range(0, len(parameter_name_list)):
        temp += format_line(parameter_name_list[i], parameter_value_list[i]) + "\r\n"
    temp += "    " + response_string + "\r\n" + "\r\n" + "\r\n"
    return temp


def format_line(name, value):
    name_line = ""
    name_reverse =reverse3(name)
    if len(name)<50:
        name_line += name_reverse + (50-len(name)) * " "
    else:
        name_line += name_reverse
    name_wanted = reverse3(name_line)
    return name_wanted + " : " + value

def reverse3(s):
    return s[::-1]
