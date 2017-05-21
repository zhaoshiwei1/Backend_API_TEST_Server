# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
            <form action = "" method = "post" width = "90%">
                <select name = "module_list">
                    <option>------------------------------</option>
                    <option value="01">----------ORDER----------</option>
                    <option value="02">----------CHARGE----------</option>
                    <option value="03">----------SETTLEMENT----------</option>
                    <option value="04">----------PAY----------</option>
                    <option value="05">----------UC----------</option>
                </select>
                <button type = "submit">过滤</button>
                <br/>
                <select name = "api_list">
                    <option>------------------------------</option>
                </select>
                <button type = "submit" formation = "">确定</button>
            </form>
        </BODY>
    </HTML>
"""