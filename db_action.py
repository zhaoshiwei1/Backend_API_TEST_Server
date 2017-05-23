from db_module import db

class db_action:
    def __init__(self):
        self.db = db()
    def get_module_list(self):
        rec = self.db.cu.execute("SELECT DISTINCT MODULE_NAME FROM general")
        result_set = self.db.cu.fetchall()
        return  result_set
    def get_api_list_by_module_id(self, id):
        rec = self.db.cu.execute("SELECT ID, API_NAME, API_CMT, IF_VALID FROM general WHERE MODULE_ID =" + "\'"+ id + "\'")
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
        rec = self.db.cu.execute("SELECT API_NAME, API_CMT, IF_VALID FROM general WHERE ID =" + "\'"+ id + "\'")
        result_set = self.db.cu.fetchall()
        if result_set[0][2] == "YES":
            print "branch YES"
            print "UPDATE general SET IF_VALID ='NO' WHERE ID =" + "\'"+ id + "\'"
            self.db.cu.execute("UPDATE general SET IF_VALID ='NO' WHERE ID =" + "\'"+ id + "\'")
            self.db.conn.commit()
        elif result_set[0][2] == "NO":
            print "branch NO"
            print "UPDATE general SET IF_VALID ='YES' WHERE ID =" + "\'"+ id + "\'"
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
        self.db.cu.execute("SELECT ID, API_NAME FROM general WHERE MODULE_ID = " +"\'"+module_id + "\'" + """AND ID <>5 AND ID<>4 AND ID<>3 AND ID<>2 AND ID <>1""")
        result_set = self.db.cu.fetchall()
        return result_set