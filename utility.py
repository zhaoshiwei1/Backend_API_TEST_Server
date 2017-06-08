# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def make_id_key(max_id):
    return str(max_id+1)

def make_module_id(max_specific_module_id):
    if(max_specific_module_id<9):
        return  "0" + str(max_specific_module_id+1)
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


def make_insert_sql(module_id,module_name, api_name, http_method, url, cmt, wanted_id, wanted_max_specific_module_id, wanted_table_name):
    sql_string = """INSERT INTO general VALUES("""
    sql_string += ("\'"+ wanted_id +"\',")
    sql_string += ("\'"+ module_id +"\',")
    sql_string += ("\'"+ module_name +"\',")
    sql_string += ("\'"+ wanted_max_specific_module_id +"\',")
    sql_string += ("\'"+ api_name +"\',")
    sql_string += ("\'"+ cmt +"\',")
    sql_string += ("\'"+ wanted_table_name +"\',")
    sql_string += ("\'"+ http_method +"\',")
    sql_string += ("\'"+ url +"\',")
    sql_string += """'YES') """
    return sql_string

def make_create_table_sql(table_name, parameters_string):
    create_table_string = """"""
    parameter_list = parameters_string.split("#")
    create_table_string += """CREATE TABLE """ + table_name
    create_table_string += """(ID TEXT NOT NULL,"""
    for parameter in parameter_list:
        create_table_string += parameter + """  TEXT NOT NULL,"""
    create_table_string +="""PRIMARY KEY (ID))"""
    return create_table_string

def make_insert_sql_by_selected_api_id(tb_name, wanted_id, parameter_name_list, parameter_value_list):
    sql_string = """"""

