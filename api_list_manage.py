# -*- coding: UTF-8 -*-
# 接口管理页面
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_no_filted_html_string(result_set):
    head_string = """
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
            <form action = "/show_apis" method = "post" width = "90%">
                <table width = "30%" border = "0">
                    <tr>
                        <td>
                            <select name = "module">
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
            </form>
            """

    result_string = """
        <table width = "45%" border = "0">
                    <tr>
                        <th align = "left">编号</th>
                        <th align = "left">名称</th>
                        <th align = "left">备注</th>
                        <th align = "left">有效性</th>
                    </tr>
    """
    for result in result_set:
        if int(result[0]) > 5 :
            result_string += """<tr><td align = "left">"""+ result[0]+"""</td><td align = "left">"""+result[1]+"""</td><td align = "left">"""+result[2]+"""</td><td align = "left">"""+result[3]+"""</td>"""
            result_string += """<td><form action = "/change_status" method = "post"><input type = "text" name = "r_id" value ="""+ "\""+ result[0]+"\""+""" style="display:none"><button type = "submit">修改</form></td></tr>"""
    result_string += """</table>"""
    end_string = """
    <form action = "/new_a_api" method = "get"><button>新增接口</button></form>
        </BODY>
    </HTML>
    """
    return head_string+result_string+end_string

def post_selected_api_list_html_string(api_result_list):
    header = """
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
                <form action = "/show_apis" method = "post" width = "90%">
                    <table width = "30%" border = "0">
                        <tr>
                            <td>
                                <select name = "module">
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
                </form>
                <table width = "45%" border = "0">
                    <tr>
                        <th align = "left">编号</th>
                        <th align = "left">名称</th>
                        <th align = "left">备注</th>
                        <th align = "left">有效性</th>
                    </tr>
        """
    result_string = """
    """
    for result in api_result_list:
        if int(result[0]) > 5 :
            result_string += """<tr><td align = "left">"""+ result[0]+"""</td><td align = "left">"""+result[1]+"""</td><td align = "left">"""+result[2]+"""</td><td align = "left">"""+result[3]+"""</td>"""
            result_string += """<td><form action = "/change_status" method = "post"><input type = "text" name = "r_id" value ="""+ "\""+ result[0]+"\""+""" style="display:none"><button type = "submit">修改</form></td></tr>"""
    result_string += """</table>"""

    end = """
    <form action = "/new_a_api" method = "get"><button>新增接口</button></form>
    </BODY>
    </HTML>
    """
    return header +result_string + end