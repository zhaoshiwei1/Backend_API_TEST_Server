from db_module import db
from utility import *

class db_action:
    def __init__(self):
        self.db = db()

    def get_module_list(self):
        self.db.cu.execute("SELECT DISTINCT MODULE_NAME FROM general")
        result_set = self.db.cu.fetchall()
        return result_set

    def get_api_list_by_module_id(self, id):
        self.db.cu.execute("SELECT ID, API_NAME, API_CMT, IF_VALID FROM general WHERE MODULE_ID =" + "\'"+ id + "\'")
        result_set = self.db.cu.fetchall()
        return result_set

    def get_all_api_list(self):
        self.db.cu.execute("SELECT ID, API_NAME, API_CMT, IF_VALID FROM general")
        result_set = self.db.cu.fetchall()
        return result_set

    def get_api_list_title(self, id):
        rec = self.db.cu.execute("SELECT ID, API_NAME, API_CMT, IF_VALID FROM general WHERE MODULE_ID =" + "\'"+ id + "\'")
        col_name_list = [tuple[0] for tuple in rec.description]
        return col_name_list

    def change_api_status(self, id):
        self.db.cu.execute("SELECT API_NAME, API_CMT, IF_VALID FROM general WHERE ID =" + "\'"+ id + "\'")
        result_set = self.db.cu.fetchall()
        if result_set[0][2] == "YES":
            # print "branch YES"
            # print "UPDATE general SET IF_VALID ='NO' WHERE ID =" + "\'"+ id + "\'"
            self.db.cu.execute("UPDATE general SET IF_VALID ='NO' WHERE ID =" + "\'"+ id + "\'")
            self.db.conn.commit()
        elif result_set[0][2] == "NO":
            # print "branch NO"
            # print "UPDATE general SET IF_VALID ='YES' WHERE ID =" + "\'"+ id + "\'"
            self.db.cu.execute("UPDATE general SET IF_VALID ='YES' WHERE ID =" + "\'"+ id + "\'")
            self.db.conn.commit()

    def get_max_id(self):
        l = []
        self.db.cu.execute("SELECT DISTINCT ID FROM general")
        result_set = self.db.cu.fetchall()
        for m in result_set:
            l.append(int(m[0]))
        return max(l)

    def get_max_specific_module_id(self, module_id):
        # print "***************" + module_id
        l = []
        self.db.cu.execute("SELECT DISTINCT API_ID FROM general WHERE MODULE_ID = " +"\'" + module_id + "\'")
        result_set = self.db.cu.fetchall()
        for m in result_set:
            # print m[0]
            l.append(int(m[0]))
        return max(l)

    def sql_execution(self, sql_string):
        self.db.cu.execute(sql_string)
        self.db.conn.commit()

    def get_apis_by_module_id(self, module_id):
        self.db.cu.execute("SELECT ID, API_NAME FROM general WHERE MODULE_ID = " +"\'"+module_id + "\'"
                           + """AND ID <>5 AND ID<>4 AND ID<>3 AND ID<>2 AND ID <>1 AND IF_VALID ='YES'""")
        result_set = self.db.cu.fetchall()
        return result_set

    def get_list_by_api_id(self, id):
        l = []
        self.db.cu.execute("SELECT API_TB_NAME, API_NAME, API_CMT FROM general WHERE ID = " + "\'" + id + "\'")
        result_set = self.db.cu.fetchall()
        tb_name = result_set[0][0]
        test_case_info = []
        test_case_info.append(result_set[0][1])
        test_case_info.append(result_set[0][2])
        rec = self.db.cu.execute("SELECT * FROM "+ tb_name)
        test_case_list = self.db.cu.fetchall()
        col_name_list = [tuple[0] for tuple in rec.description]
        l.append(col_name_list)
        l.append(test_case_list)
        l.append(test_case_info)
        return l

    def get_test_case_parameter_from_table_by_id(self, tb_name, case_id):
        l = []
        parameter_name = []
        parameter_value = []
        rec = self.db.cu.execute("SELECT * FROM " + "\'" + tb_name + "\'" + " WHERE TEST_CASE_ID = " + "\'" + case_id + "\'")
        parameter = self.db.cu.fetchall()
        col_name_list = [tuple[0] for tuple in rec.description]
        if len(parameter[0]) == len(col_name_list):
            for i in range(0,len(parameter[0])):
                if col_name_list[i] != "test_case_name" and col_name_list[i] != "TEST_CASE_ID":
                    parameter_name.append(col_name_list[i])
                    parameter_value.append(parameter[0][i])
            l.append(parameter_name)
            l.append(parameter_value)
            return l
        else:
            return 0


    def delete_case_by_api_and_id(self, api_id, case_id):
        self.db.cu.execute("SELECT API_TB_NAME FROM general WHERE ID = " + "\'" + api_id + "\'")
        result_set = self.db.cu.fetchall()
        tb_name = result_set[0][0]
        # print "DELETE FROM " + tb_name + " WHERE ID =" + "\'" + case_id + "\'"
        self.db.cu.execute("DELETE FROM " + tb_name + " WHERE TEST_CASE_ID =" + "\'" + case_id + "\'")
        self.db.conn.commit()

    def get_max_id_from_specific_table(self, selected_api_id):
        l = []
        self.db.cu.execute("SELECT API_TB_NAME FROM general WHERE ID = " + "\'" + selected_api_id + "\'")
        result_set_1 = self.db.cu.fetchall()
        tb_name = result_set_1[0][0]
        self.db.cu.execute("SELECT * FROM " + tb_name)
        result_set = self.db.cu.fetchall()
        # print result_set
        if len(result_set) == 0:
            return 0
        else:
            for m in result_set:
                l.append(int(m[0]))
            return max(l)+1

    def insert_test_case_into_specific_table(self, selected_api_id, parameter_name_list,
                                             parameter_value_list, wanted_id):
        self.db.cu.execute("SELECT API_TB_NAME FROM general WHERE ID = " + "\'" + selected_api_id + "\'")
        result_set_1 = self.db.cu.fetchall()
        tb_name = result_set_1[0][0]
        sql_string = make_insert_sql_by_selected_api_id(tb_name, wanted_id, parameter_name_list, parameter_value_list)
        self.db.cu.execute(sql_string)
        self.db.conn.commit()

    def update_test_case_specific_table(self, api_id, case_id, parameter_name_list, parameter_value_list):
        self.db.cu.execute("SELECT API_TB_NAME FROM general WHERE ID = " + "\'" + api_id + "\'")
        result_set_1 = self.db.cu.fetchall()
        tb_name = result_set_1[0][0]
        sql_string = make_update_sql(tb_name, case_id, parameter_name_list, parameter_value_list)
        # print sql_string
        self.db.cu.execute(sql_string)
        self.db.conn.commit()

    def get_specific_test_case(self, api_id, case_id):
        l = []
        test_case_info = []
        self.db.cu.execute("SELECT API_TB_NAME, API_NAME, API_CMT from general WHERE ID = " + "\'" + api_id + "\'")
        result_set_1 = self.db.cu.fetchall()
        tb_name = result_set_1[0][0]
        test_case_name = result_set_1[0][1]
        test_case_cmt = result_set_1[0][1]
        test_case_info.append(test_case_name)
        test_case_info.append(test_case_cmt)
        # print tb_name
        rec = self.db.cu.execute("SELECT * from " + tb_name + " WHERE ID = " + "\'" + case_id + "\'")
        result_set_2 = self.db.cu.fetchall()
        col_name_list = [tuple[0] for tuple in rec.description]
        l.append(test_case_info)
        l.append(col_name_list)
        l.append(result_set_2)
        return l

    def get_test_plan_list(self):
        self.db.cu.execute("SELECT ID, NAME, MODULE_ID from test_plan")
        result_set = self.db.cu.fetchall()
        return result_set

    def delete_test_plan(self, test_plan_id):
        self.db.cu.execute(" DELETE FROM test_plan WHERE ID = " + "\'" + test_plan_id + "\'")
        self.db.conn.commit()

    def get_active_case_string(self, test_plan_id):
        self.db.cu.execute("SELECT ACTIVE_TEST_CASE FROM test_plan WHERE ID = " + "\'" + test_plan_id + "\'")
        result_set = self.db.cu.fetchall()
        return result_set[0][0]

    def get_table_name_list_by_module_id(self, module_id):
        self.db.cu.execute("SELECT API_TB_NAME FROM general WHERE MODULE_ID = " + "\'" + module_id + "\'"
                           + """ AND IF_VALID = 'YES'""")
        tb_name_list = self.db.cu.fetchall()
        return tb_name_list

    def get_test_case_list(self, tb_name):
        self.db.cu.execute("SELECT TEST_CASE_ID, test_case_name FROM" + "\'" + tb_name + "\'")
        test_case_id_list = self.db.cu.fetchall()
        return test_case_id_list

    def get_test_plan_name_by_id(self, test_plan_id):
        self.db.cu.execute("SELECT NAME from test_plan WHERE ID =" + "\'" + test_plan_id + "\'")
        test_plan_name = self.db.cu.fetchall()
        return test_plan_name


    def update_active_case_string_to_test_plan(self, test_plan_id, active_case_string):
        self.db.cu.execute("UPDATE test_plan SET ACTIVE_TEST_CASE = " + "\'" + active_case_string + "\'"
                           + " WHERE ID =" + "\'"+ test_plan_id + "\'")
        self.db.conn.commit()


    def get_base_url_by_test_plan_id(self, test_plan_id):
        self.db.cu.execute("SELECT BASE_URL from test_plan WHERE ID = " +"\'" + test_plan_id + "\'")
        result_set = self.db.cu.fetchall()
        return  result_set[0][0]

    def get_active_case_list_by_test_plan_id(self, test_plan_id):
        self.db.cu.execute("SELECT ACTIVE_TEST_CASE FROM test_plan WHERE ID = " + "\'" + test_plan_id + "\'")
        result_set = self.db.cu.fetchall()
        test_case_list = []
        l = result_set[0][0].split("#")
        for l_element in l:
            test_case_list.append(l_element.split(":"))
        return test_case_list

    def get_test_case_info_by_table_name(self, tb_name):
        self.db.cu.execute("SELECT API_URL, HTTP_METHOD FROM general WHERE API_TB_NAME = " + "\'" + tb_name + "\'")
        result_set = self.db.cu.fetchall()
        return result_set


    def add_new_test_plan(self, name, base_url, module_id, owner):
        test_plan_id = self.get_max_id_from_test_plan_table()
        sql_string = """
        INSERT INTO test_plan VALUES (
        """
        sql_string += "\'" + str(test_plan_id) + "\'" + ", " + "\'" + name + "\'" + ", " + "\'" + base_url + "\'" + ", " + "\'" + module_id + "\'" + ", " + "\'" + owner + "\'"
        sql_string += """
        , '0', '0')
        """
        self.db.cu.execute(sql_string)
        self.db.conn.commit()

    def get_max_id_from_test_plan_table(self):
        l = []
        self.db.cu.execute("SELECT * FROM test_plan")
        result_set = self.db.cu.fetchall()
        # print result_set
        if len(result_set) == 0:
            return 0
        else:
            for m in result_set:
                l.append(int(m[0]))
            return max(l)+1

    def add_new_record_to_test_report(self, test_plan_id, time_flag, test_report_string):
        test_report_id = self.get_max_id_from_test_report_table()
        sql_string = """
        INSERT INTO TEST_REPORT VALUES (
        """
        sql_string += "\'" + str(test_report_id) + "\'" + ", " + "\'" + test_plan_id + "\'" + ", " + "\'" + time_flag \
                      + "\'" + ", " + "\'" + test_report_string + "\'"
        sql_string += """)"""
        self.db.cu.execute(sql_string)
        self.db.conn.commit()

    def get_max_id_from_test_report_table(self):
        l = []
        self.db.cu.execute("SELECT * FROM TEST_REPORT")
        result_set = self.db.cu.fetchall()
        # print result_set
        if len(result_set) == 0:
            return 0
        else:
            for m in result_set:
                l.append(int(m[0]))
            return max(l)+1


    def get_test_result_history_of_test_pan(self, test_plan_id):
        self.db.cu.execute("SELECT ID, TIME_FLAG FROM TEST_REPORT WHERE TEST_PLAN_ID = " + "\'" + test_plan_id + "\'")
        result_set = self.db.cu.fetchall()
        return result_set

    def get_test_report_string(self, test_report_recod_id):
        self.db.cu.execute("SELECT TEST_RESULT FROM TEST_REPORT WHERE ID = " + "\'" + test_report_recod_id + "\'")
        return self.db.cu.fetchall()

