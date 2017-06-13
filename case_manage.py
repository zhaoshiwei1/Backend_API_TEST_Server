# -*- coding: UTF-8 -*-
import sys
from db_action import *
reload(sys)
sys.setdefaultencoding('utf8')

def get_test_case_filter_html_string():
    header_string = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h1>用例管理!</h1>
                <br>
                <br>
                <form action = "/show_test_cases" method = "post" width = "90%">
                <table width = "30%" border = "0">
                    <tr>
                        <td>
                            模块：
                        </td>
                        <td>
                            <select name = "module_list">
                                <option>------------------------------</option>
                                <option value="01">----------ORDER----------</option>
                                <option value="02">----------CHARGE----------</option>
                                <option value="03">----------SETTLEMENT----------</option>
                                <option value="04">----------PAY----------</option>
                                <option value="05">----------UC----------</option>
                            </select>
                        </td>
                        <td>
                            <button type = "submit">过滤</button>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            接口：
                        </td>
                        <td>
                            <select name = "api_list">
                                <option value = "default">------------------------------</option>
                            </select>
                        </td>
                        <td>
                            <button type = "submit" formation = "">确定</button>
                        </td>
                    </tr>
                </table>
                </form>
            </BODY>
        </HTML>
    """
    return header_string

def get_module_filted_html_string(selected_module_id, result_set):
    values = {
        "01":"ORDER",
        "02":"CHARGER",
        "03":"SETTLEMENT",
        "04":"PAY",
        "05":"UC"
    }

    header_string = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h1>用例管理!</h1>
                <br/>
                <br/>
                <form action = "/show_test_cases" method = "post" width = "90%">
                <table width = "30%" border = "0">
                    <tr>
                        <td>
                            模块：
                        </td>
                        <td>
                            <select name = "module_list">
                                <option>------------------------------</option>
    """

    filter_1 = """
    """
    for id in values.keys():
        if id == selected_module_id:
            filter_1 += """<option value=""" +"\"" + id + "\"" + """ selected ="selected">""" + """----------""" + values[id] + """----------</option>"""
        else:
            filter_1 +="""<option value=""" +"\"" + id + "\">" + """----------""" + values[id] + """----------</option>"""

    end_string_1 = """

         </select>
                        </td>
                        <td>
                            <button type = "submit">过滤</button>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            接口：
                        </td>
                        <td>
                            <select name = "api_list">
                                <option value = "default">------------------------------</option>
                                """
    filter_2 = """"""
    for result in result_set:
        filter_2 += """<option value =""" +"\'"+result[0] +"\'" +""">"""  + """----------""" + result[1] + """----------</option>"""
        # print result[0]
        # print result[1]
    end_string_2 ="""
                            </select>
                        </td>
                        <td>
                            <button type = "submit" formation = "">确定</button>
                        </td>
                    </tr>
                </table>
                </form>
            </BODY>
        </HTML>
    """

    return header_string+filter_1+end_string_1+filter_2+end_string_2

def get_api_filter_html_string(selected_module_id, result_set, selected_api_id):
    d_a = db_action()
    result_full_map = d_a.get_list_by_api_id(selected_api_id)
    col_name_list = result_full_map[0]
    test_case_list = result_full_map[1]
    # print  col_name_list
    # print  test_case_list
    values = {
        "01":"ORDER",
        "02":"CHARGER",
        "03":"SETTLEMENT",
        "04":"PAY",
        "05":"UC"
    }

    header_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h1>用例管理!</h1>
                <br/>
                <br/>
                <form action = "/show_test_cases" method = "post" width = "90%">
                <table width = "30%" border = "0">
                    <tr>
                        <td>
                            模块：
                        </td>
                        <td>
                            <select name = "module_list">
                                <option>------------------------------</option>
        """

    filter_1 = """
        """
    for id in values.keys():
        if id == selected_module_id:
            filter_1 += """<option value=""" +"\"" + id + "\"" + """ selected ="selected">""" + """----------""" + values[id] + """----------</option>"""
        else:
            filter_1 +="""<option value=""" +"\"" + id + "\">" + """----------""" + values[id] + """----------</option>"""

    end_string_1 = """

             </select>
                            </td>
                            <td>
                                <button type = "submit">过滤</button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                接口：
                            </td>
                            <td>
                                <select name = "api_list">
                                    <option value = "default">------------------------------</option>
                                    """
    filter_2 = """"""
    for result in result_set:
        filter_2 += """<option value =""" +"\'"+result[0] +"\'" +""">"""  + """----------""" + result[1] + """----------</option>"""
        # print result[0]
        # print result[1]
    end_string_2 ="""
                                </select>
                            </td>
                            <td>
                                <button type = "submit" formation = "/show_test_cases">确定</button>
                            </td>
                        </tr>
                    </table>
                    </form>
        """
    test_case_string = """
    """
    test_case_string += """
    <table width = "45%" border = "0">
    <tr>
    """
    j = 0
    for name in col_name_list:
        if j == 0:
            test_case_string += """<th align = "left"></th>"""
            j += 1
        else:
            test_case_string += """<th align = "left">""" + name + """</th>"""
            j += 1
    test_case_string += """<th align = "left">Action</th>"""
    test_case_string += """</tr>"""
    for case in test_case_list:
        test_case_string += """<tr>"""
        i = 0
        case_id = ""
        for element in case:
            if i == 0:
                case_id += element
                test_case_string +="""<td></td>"""
                i += 1
            else:
                test_case_string += """<td>""" + element + """</td>"""
                i += 1
        test_case_string += """<td nowrap>
                                    <form action = "/delete_test_case" method = "post" >
                                        <input type = "text" name = "c_id" value = """ + case_id + """ style="display:none">
                                        <input type = "text" name = "a_id" value = """ + selected_api_id + """  style="display:none" >
                                        <button type = "submit">删除</button>
                                        <button type = "submit" formaction = "/modify_test_case">修改</button>
                                    </form>
                                </td></tr>"""
    test_case_string += """</table>"""

    add_case_string = """
    <br>
    <br>
    <form action = "/add_test_case" method = "post" >
        <input type = "text" name = "api_id_new" value = """ + selected_api_id + """  style="display:none" >
        <button type = "submit">新增</button>
    </form>
    """

    end = """
                </BODY>
            </HTML>
        """

    return header_string + filter_1 + end_string_1 + filter_2 + end_string_2 + test_case_string + add_case_string + end

def get_add_test_case_page_html_string(selected_api_id):
    d_a = db_action()
    result_full_map = d_a.get_list_by_api_id(selected_api_id)
    col_name_list = result_full_map[0]
    test_case_info = result_full_map[2]
    head_string1 = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>"""
    head_string2 = """<h1>""" + test_case_info[0] + """</h1>"""
    head_string2 += """<h2>""" + test_case_info[1] + """</h2>"""
    body_string = """
    """
    body_string += """<form action = "/submit_add_test_case" method = "post">
        <table width = "45%" border = "0">
    """
    for parameter in col_name_list:
        if parameter != "ID":
            body_string += """<tr><td>""" + parameter + """</td>""" + """<td align = "center"> : </td>""" + """<td><input type = "text" name = """+ "\""+ parameter + "\"" +""" ></td></tr>"""
    body_string += """</table>"""
    body_string += """<button type = "submit">提交</button></form>"""
    end_string = """
    </BODY>
    </HTML>
    """
    return head_string1 + head_string2 + body_string + end_string


def get_edit_case_page_html_string(api_id, case_id, col_name_list, value_list, test_case_info):
    head_string1 = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>"""
    head_string2 = """<h1>""" + test_case_info[0] + """</h1>"""
    head_string2 += """<h2>""" + test_case_info[1] + """</h2>"""
    body = """"""
    body += """
        <form action = "/submit_modify_test_case" method = "post">
        <table width = "45%" border = "0">
    """
    if len(col_name_list) == len(value_list[0]):
        for i in range(0, len(col_name_list)):
            if i != 0:
                body += """<tr><td>""" + col_name_list[i] + """</td>""" + """<td align = "center"> : </td>""" + """<td><input type = "text" name = """+ "\"" + col_name_list[i] + "\"" +""" value = """ + "\"" + value_list[0][i] +"\""+ """></td></tr>"""
        body += """</table>"""
        body += """
                <input type = "text" name = "c_id" value = """ + case_id + """ style="display:none">
                <input type = "text" name = "a_id" value = """ + api_id + """  style="display:none" >
                """
        body += """<button type = "submit">提交</button></form>"""
        end = """</BODY></HTML>"""
        return head_string1 + head_string2 + body + end
    else:
        print "failed test case"
        return 0