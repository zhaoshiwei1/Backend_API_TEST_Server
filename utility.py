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

def make_table_name(module_id, specific_module_id):
    return module_id + specific_module_id

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
    sql_string += ("""ID = """+"\'"+ wanted_id +"\',")
    sql_string += ("""MODULE_ID = """+"\'"+ module_id +"\',")
    sql_string += ("""MODULE_NAME = """+"\'"+ module_name +"\',")
    sql_string += ("""API_ID = """+"\'"+ wanted_max_specific_module_id +"\',")
    sql_string += ("""API_NAME = """+"\'"+ api_name +"\',")
    sql_string += ("""API_CMT = """+"\'"+ cmt +"\',")
    sql_string += ("""API_TB_NAME = """+"\'"+ wanted_table_name +"\',")
    sql_string += ("""HTTP_METHOD = """+"\'"+ http_method +"\',")
    sql_string += ("""API_URL = """+"\'"+ url +"\',")
    sql_string += """IF_VALID =YES) """

    return sql_string