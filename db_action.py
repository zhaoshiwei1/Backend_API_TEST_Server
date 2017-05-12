from db_module import db

class db_action:
    def __init__(self):
        self.db = db()
    def get_module_list(self):
        rec = self.db.cu.execute("SELECT DISTINCT MODEL_NAME FROM common")
        result_set = self.db.cu.fetchall()
        return  result_set
    def get_api_list_by_module_id(self, id):
        rec = self.db.cu.execute("SELECT API_NAME, API_CMT, IF_VALID FROM common WHERE MODEL_ID =" + "\'"+ id + "\'")
        result_set = self.db.cu.fetchall()
        return result_set
    def get_api_list_title(self, id):
        rec = self.db.cu.execute("SELECT API_NAME, API_CMT, IF_VALID FROM common WHERE MODEL_ID =" + "\'"+ id + "\'")
        col_name_list = [tuple[0] for tuple in rec.description]
        return col_name_list