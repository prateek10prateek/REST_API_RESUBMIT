from app import app
from model.user_model import user_model
from flask import request

obj=user_model()

@app.route("/api/users/getall")
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/api/users/add", methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/api/users/update", methods=["PUT"])
def update_user():
    return obj.update_user_model(request.form)

@app.route("/api/users/get/<id>", methods=["GET"])
def user_getone_controller(id):
    return obj.user_getone_model(id)


@app.route("/api/users/delete/<id>", methods=["DELETE"])
def delete_user(id):
    return obj.user_delete_model(id)


@app.route("/api/users/getall/limit/<limit>/page/<page>", methods=["GET"])
def getall_limit_controller(limit,page):
    return obj.user_pagination_model(limit,page)


@app.route("/api/addmultiple", methods=["POST"])
def add_multiple_users():
    return obj.add_multiple_users_model(request.json)

