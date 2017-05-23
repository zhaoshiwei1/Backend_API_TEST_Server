# -*- coding: UTF-8 -*-
import sys
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
                <h1>接口管理!</h1>
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
                <h1>接口管理!</h1>
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

    end_string = """

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

    return header_string+filter_1+end_string