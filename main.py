# -*- coding: UTF-8 -*-
import sys
import web
from db_action import db_action
reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'index',
    '/show_apis', 'show_api_list',
    '/change_status', 'change_status'
)

class index:
    def GET(self):
        header = """
         <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> 后台接口测试平台</TITLE> </HEAD> <BODY><h1>欢迎访问易到后台测试!</h1>
        """
        end = """
        </BODY></HTML>
        """
        s1 = """
        <br/>
        <br/>
        """
        s2 = """
        <table width = "30%", border = "0">
            <tr>
                <th align = "left" width = 75></th>
                <th align = "left"><a href="/show_apis"><h3>接口管理</h3></a></th>
            </tr>
            <tr>
                <th align = "left" width = 75></th>
                <th align = "left"><a href="/show_apis"><h3>测试用例管理</h3></a></th>
            </tr>
            <tr>
                <th align = "left" width = 75></th>
                <th align = "left"><a href="/show_apis"><h3>测试执行</h3></a></th>
            </tr>
        </table>
        """
        return  header + s1 + s2 +end

class show_api_list:
    def GET(self):
        d_a = db_action()
        result_set = d_a.get_api_list_by_module_id('03')
        col_name_list = d_a.get_api_list_title('03')
        header = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> 后台接口测试平台</TITLE> </HEAD> <BODY><h1>接口管理!</h1>
        """
        end = """
        </BODY></HTML>
        """
        filter = """
        <form action = "/show_apis" method = "post" width = "90%">
            <table width = "30%" border = "0">
                <tr>
                    <td>
                        <select name = "module">
                            <option value="01">----------ORDER----------</option>
                            <option value="02">----------CHARGE----------</option>
                            <option value="03" selected="selected">----------SETTLEMENT----------</option>
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
        show_default_filted = """
        <table width = "45%" border = "0">
            <tr>
        """
        for name in col_name_list:
            show_default_filted = show_default_filted + """<th align="left">"""
            show_default_filted = show_default_filted + name
            show_default_filted = show_default_filted + """</th>"""
        show_default_filted +="""<th>Action</th></tr>"""
        for ret in result_set:
            show_default_filted = show_default_filted + """<tr>"""
            show_default_filted = show_default_filted + """<form action = "/change_status" method = "post"><td align = "left"><input type = "text" name = "id" value ="""+str(ret[0]) + """ disabled="true" >"""
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[1]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[2]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[3]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td><button type = "submit">更改接口有效性</button></td></form></tr>"""

        show_default_filted += """</table>"""
        return header + filter +show_default_filted + end

    def POST(self):
        d_a = db_action()
        i = web.input('module')
        result_set = d_a.get_api_list_by_module_id(i.module)
        col_name_list = d_a.get_api_list_title(i.module)
        header = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> 后台接口测试平台</TITLE> </HEAD> <BODY><h1>接口管理!</h1>
        """
        end = """
        </BODY></HTML>
        """
        filter = """
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
        """

        show_default_filted = """
        <table width = "45%" border = "0">
            <tr>
        """
        for name in col_name_list:
            show_default_filted = show_default_filted + """<th align="left">"""
            show_default_filted = show_default_filted + name
            show_default_filted = show_default_filted + """</th>"""

        show_default_filted +="""<th>Action</th></tr>"""

        for ret in result_set:
            show_default_filted = show_default_filted + """<tr><form action = "/change_status" method = "post">"""
            show_default_filted = show_default_filted + """<td align = "left"><input type = "text" name = "id" value ="""+str(ret[0]) + """ disabled="true" >"""
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[1]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[2]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td align = "left">"""
            show_default_filted = show_default_filted + ret[3]
            show_default_filted = show_default_filted + """</td>"""
            show_default_filted = show_default_filted + """<td><button type = "submit">更改接口有效性</button></td></form></tr>"""

        show_default_filted += """</table>"""
        return header + filter +show_default_filted + end

class change_status:
    def POST(self):
        d_a = db_action()
        i = web.input('id')
        print i.id
        d_a.change_api_status(self, i.id)
        return web.seeother('/show_apis')

if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()