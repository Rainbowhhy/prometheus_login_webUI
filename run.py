from flask import Flask, request, render_template, redirect, url_for
from werkzeug.security import check_password_hash
import json
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"
app.secret_key = '123456'

# 存放用户名和密码的json文件
PROFILE_PATH = os.path.dirname(os.path.abspath(__file__))
PROFILE_FILE = os.path.join(PROFILE_PATH, "profiles.json")


# 用户名密码加密认证
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.get_password_hash()

    def get_password_hash(self):
        # 从文件中获取密码
        try:
            with open(PROFILE_FILE) as f:
                user_profiles = json.load(f)
                user_info = user_profiles.get(self.username, None)
                if user_info is not None:
                    return user_info[0]
        except:
            print("get password error!")

    def verify_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)


@app.route("/auth", methods=["GET", "POST"])
def auth():
    url = request.cookies.get('ORIGINURL')
    token = request.cookies.get('token')
    if token == "ABCDE":
        return ("success", 200)
    else:
        return ("go to login", 401)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User(username, password)
        if user.verify_password(password):
            token = "ABCDE"
            return (token, 200)
        else:
            error = "用户名或密码错误..."
            return (error, 403)
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host="localhost", port=5000)
