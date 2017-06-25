# -*- coding: UTF-8 -*-
import datetime
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
                    <button type = "submit" disabled = "disabled">删除</button>
                    <button type = "submit" formaction = "/show_test_result_history">历史</button>
                    <button type = "submit" formaction = "/show_test_case_list" method = "post">Run</button>
                </form>
            </td>
        </tr>
        """
    body_string += """</table>"""
    body_string += """<a href="/add_test_plan"><h4><i>__新增测试计划__</i></h4></a>"""
    body_string += """</BODY></HTML>"""
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
                    <button disabled = "disabled">全选</button>
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
                    <button disabled = "disabled">全选</button>
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


def get_add_test_plan_html_page():
    head_string = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
    <HTML>
        <HEAD>
            <meta http-equiv="X-UA-Compatible" content="IE=8" />
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <TITLE> 后台接口测试平台</TITLE>
        </HEAD>
        <BODY>
            <h2>新增测试计划!</h2>
            <br/>
    """
    body_string = """
        <form action = "/add_test_plan" method = "post">
        <table width = "30%" border = "0">
            <tr>
                <td align = "right">
                    模块
                </td>
                <td align = "center">
                :
                </td>
                <td align = "left">
                    <select name = "module_add_test_plan">
                        <option value="01">----------ORDER----------</option>
                        <option value="02">----------CHARGE----------</option>
                        <option value="03">----------SETTLEMENT----------</option>
                        <option value="04">----------PAY----------</option>
                        <option value="05">----------UC----------</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td align = "right">
                    测试计划名称
                </td>
                <td align = "center">
                    :
                </td>
                <td align = "left">
                    <input type = "text" name = "name_add_test_plan"/>
                </td>
            </tr>
            <tr>
                <td align = "right">
                    BASE_URL
                </td>
                <td align = "center">
                    :
                </td>
                <td align = "left">
                    <input type = "text" name = "base_url_add_test_plan"/>
                </td>
            </tr>
            <tr>
                <td align = "right">
                    所有者
                </td>
                <td align = "center">
                    :
                </td>
                <td align = "left">
                    <input type = "text" name = "owner_add_test_plan"/>
                </td>
            </tr>
            </table>
            <button>提交</button>
        </form>
        """
    end_string = """
        </BODY>
        </HTML>
        """
    return head_string+body_string+end_string


def get_test_result_history_html(test_result_full_map):
    if len(test_result_full_map) == 0:
        head_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h2>当前测试计划无历史测试结果!</h2>
                <br/>
            </BODY>
        </HTML>
        """
        return head_string
    else:
        head_string = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <HTML>
            <HEAD>
                <meta http-equiv="X-UA-Compatible" content="IE=8" />
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <TITLE> 后台接口测试平台</TITLE>
            </HEAD>
            <BODY>
                <h4>历史测试结果!</h4>
                <br/>
                <br/>
        """
        body_string = """
        """
        body_string += """
        <table width = "50%" border = "0">
        """
        for test_report in test_result_full_map:
            test_report_recod_id = test_report[0]
            test_report_time_flag = test_report[1]
            dateArray = datetime.datetime.utcfromtimestamp(int(test_report_time_flag))
            otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
            body_string += """
            <tr>
            <td align = "left">
            """ + otherStyleTime + """</td>"""
            body_string += """
            <td valign = "middle">
                <form action = "/show_test_result_string" method = "post">
                    <input type = "text" name = "test_report_recod_id" value = """ + test_report_recod_id + """ style = "display:none">
                    <button type = "submit">查看</button>
                </form>
            </td>
            </tr>
                """
        end_string = """
            </table></BODY></HTML>
            """
        return head_string + body_string + end_string