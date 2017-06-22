# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def show_all_test_plan_html_string(test_plan_list):
    header_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h1>测试计划!</h1>
                <br>
                <br>
    """
    body_string = """
            <table width = "45%" border = "0">
                <tr>
                    <th align = "left" >测试计划</th>
                    <th> </th>
    """
    for test_plan in test_plan_list:
        body_string += """<tr>
        """
        body_string += """<td>""" + test_plan[1] + """</td>"""
        body_string += """
            <td>
                <form action = "/delete_test_plan" method = "post">
                    <input type = "text" name = "test_plan_id" value = """ + test_plan[0] + """ style = "display:none">
                    <input type = "text" name = "module_id" value = """ + test_plan[2] + """ style = "display:none">
                    <button type = "submit">删除</button>
                    <button type = "submit" formaction = "">历史</button>
                    <button type = "submit" formaction = "/show_test_case_list" method = "post">Run</button>
                </form>
            </td>
        </tr>
        """
    body_string += """</table>"""

    return header_string + body_string

def get_case_list_by_default(test_plan_id, test_plan_name, case_string):
    header_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h2>""" + test_plan_name + """</h2>
                <br>
                <br>
        """
    tc_name_list = case_string[1]
    tc_id_list = case_string[0]

    body_string = """
        <form action = "/run_test_case" method = "post">
            <table width = "35%" border = "1">
                <th align = 'left'>
                    <button>全选</button>
                </th>
                <th align = "left">
                    测试用例名
                </th>
        """
    for i in range(0, len(tc_id_list)):
        body_string += """<tr><td><input type="checkbox" name="tc_id_whole" value= """ + "\"" \
                       + tc_id_list[i] + "\""+"""/></td>"""
        body_string += """<td align = 'left'>""" + tc_name_list[i] + """</td></tr>"""
    body_string += """</table>"""
    body_string += """<input type = "text" name = "test_plan_id" value = """ + test_plan_id \
                   + """ style = "display:none">"""
    body_string += "<button type='submit'>执行</button></form></BODY></HTML>"
    return header_string + body_string


def get_active_case_list(test_plan_id, test_plan_name, case_string, active_case_string):
    header_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h2>""" + test_plan_name + """</h2>
                <br>
                <br>
        """
    tc_name_list = case_string[1]
    tc_id_list = case_string[0]

    body_string = """
        <form action = "/run_test_case" method = "post">
            <table width = "35%" border = "1">
                <th align = 'left'>
                    <button>全选</button>
                </th>
                <th align = "left">
                    测试用例名
                </th>
        """
    for i in range(0, len(tc_id_list)):
        if tc_id_list[i] in active_case_string:
            body_string += """<tr><td><input type="checkbox" name="tc_id_whole" value= """ + "\"" \
                           + tc_id_list[i] + "\""+""" checked ='checked'/></td>"""
            body_string += """<td align = 'left'>""" + tc_name_list[i] + """</td></tr>"""
        else:
            body_string += """<tr><td><input type="checkbox" name="tc_id_whole" value= """ + "\"" \
                           + tc_id_list[i] + "\""+"""/></td>"""
            body_string += """<td align = 'left'>""" + tc_name_list[i] + """</td></tr>"""
    body_string += """</table>"""
    body_string += """<input type = "text" name = "test_plan_id" value = """ + test_plan_id \
                   + """ style = "display:none">"""
    body_string += "<button type='submit'>执行</button></form></BODY></HTML>"
    return header_string + body_string
