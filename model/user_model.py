import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con= mysql.connector.connect(host="localhost",user="root",password="",database="rest_api")
            print("connection secured")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
        except:
            print("some error")
    

    def user_getall_model(self):
            self.cur.execute("SELECT * FROM users")
            res=self.cur.fetchall()
            print(res)
            if(len(res)>0):
                res=make_response({"payload":res},200)  
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
                return make_response({"message":"no data"},204)

                
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(id, first_name, last_name, company_name, city, state, zip, email, web, age) VALUES({data['id']},'{data['first_name']}', '{data['last_name']}', '{data['company_name']}', '{data['city']}', '{data['state']}', {data['zip']}, '{data['email']}', '{data['web']}', {data['age']} )")
        return make_response({"message":"user created successfully"},201)

    def update_user_model(self,data):
        self.cur.execute(f"'UPDATE users SET first_name:'{data['first_name']}', last_name='{data['last_name']}', company_name='{data['company_name']}', city='{data['city']}', state='{data['state']}', zip={data['zip']}, email='{data['email']}', web='{data['web']}', age={data['age']} WHERE id={data['id']}'")
        if self.cur.rowcount()>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def user_getone_model(self,id):
        self.cur.execute(f"SELECT*FROM users WHERE id={id}")
        res=self.cur.fetchall()
        if(self.cur.rowcount>0):
            res=make_response({"payload":res},200)  
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return make_response({"message":"user not found"},202)
               
    
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if(self.cur.rowcount>0):
            return make_response({"message":"user deleted successfully"},200)
        else:
            return make_response({"message":"nothing to delete"},202)

    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        query=f"SELECT * FROM users LIMIT {start},{limit}"
        self.cur.execute(query)
        res=self.cur.fetchall()
        if(len(res)>0):
            res=make_response({"payload":res,"page_no.":page,"limit":limit},200)  
            res.headers['Access-Control-Allow-Origin']="*"               
            return res
        else:
            return make_response({"message":"no data"},204)
        
    def add_multiple_users_model(self, data):
        qry = "INSERT INTO users(id, first_name, last_name, company_name, city, state, zip, email, web, age) VALUES "
        for userdata in data:
            qry += f" ({userdata['id']}, '{userdata['first_name']}', '{userdata['last_name']}', '{userdata['company_name']}', '{userdata['city']}', '{userdata['state']}', {userdata['zip']}, '{userdata['email']}', '{userdata['web']}', {userdata['age']}),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)