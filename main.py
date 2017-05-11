# -*- coding: UTF-8 -*-
import sys
import web
reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'index',
    '/show_apis', 'show_api_list',
    '/filter_apis', 'filter_apis'
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
        <form action = "/filter_apis" method = "post" width = "90%">
            <table width = "30%" border = "0">
                <tr>
                    <td>
                        <select name = "module">
                            <option value="01">----------Volvo----------</option>
                            <option value="02">----------Saab----------</option>
                            <option value="03" selected="selected">----------Fiat----------</option>
                            <option value="04">----------Audi----------</option>
                            <option value="05">----------汽车----------</option>
                        </select>
                    </td>
                    <td>
                        <button type = "submit">过滤</button>
                    </td>
                </tr>
        </form>
        """
        return header + filter + end

class filter_apis:
    def POST(self):
        i = web.input("module")
        print i.module
        return web.seeother('/show_apis')
    def GET(self):
        return web.seeother('/show_apis')
if __name__=="__main__":
    app = web.application(urls,globals())
    app.run()