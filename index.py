# -*- coding: UTF-8 -*-
# 静态页面， 分别导航至各个模块
import sys
reload(sys)
sys.setdefaultencoding('utf8')

index_html_string = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
        <HEAD>
            <meta http-equiv="X-UA-Compatible" content="IE=8" />
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <TITLE> 后台接口测试平台</TITLE> 
        </HEAD> 
    <BODY>
        <h1>欢迎访问易到后台测试!</h1>
            <br/>
            <br/>
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
    </BODY>
</HTML>
"""
