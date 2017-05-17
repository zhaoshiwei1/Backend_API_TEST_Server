# -*-coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_add_an_api_html_string():
    head_string = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
    <HTML>
        <HEAD>
            <meta http-equiv="X-UA-Compatible" content="IE=8" />
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <TITLE> 后台接口测试平台</TITLE>
        </HEAD>
        <BODY>
            <h2>新增接口!</h2>
            <br/>
    """
    body_string = """
    <form action = "" method = "post">
    <table width = "30%" border = "0">
        <tr>
            <td align = "right">
                模块
            </td>
            <td align = "center">
            :
            </td>
            <td align = "left">
                <select name = "api_add_module">
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
                接口名
            </td>
            <td align = "center">
                :
            </td>
            <td align = "left">
                <input type = "text" name = "api_add_name"/>
            </td>
        </tr>
        <tr>
            <td align = "right">
                http_method
            </td>
            <td align = "center">
                :
            </td>
            <td align = "left">
                <input type = "text" name = "api_http_method"/>
            </td>
        </tr>
        <tr>
            <td align = "right">
                URL
            </td>
            <td align = "center">
                :
            </td>
            <td align = "left">
                <input type = "text" name = "api_add_url"/>
            </td>
        </tr>
        <tr>
            <td align = "right">
                备注
            </td>
            <td align = "center">
                :
            </td>
            <td align = "left">
                <input type = "text" name = "api_add_cmt"/>
            </td>
        </tr>
        </table>
        <br/>
        字段（字段名之间用逗号隔开， 例如: driver_id, ammount, service_order_id）
        <br/>
        <textarea rows = "15" cols = "78" name = "parameter_list"></textarea>
        <br/>
        <button>提交</button>
    </form>
    """
    end_string = """
    </BODY>
    </HTML>
    """
    return head_string+body_string+end_string