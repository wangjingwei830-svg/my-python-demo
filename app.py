from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-secret-key"

# 演示账号（生产环境请改为数据库持久化）
users = {
    "admin": "123456"
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if users.get(username) == password:
            return redirect(url_for("dashboard", username=username))

        flash("用户名或密码错误，请重试。")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not password:
            flash("用户名和密码不能为空。")
            return render_template("register.html")

        if username in users:
            flash("该用户名已存在，请更换用户名。")
            return render_template("register.html")

        if password != confirm_password:
            flash("两次输入的密码不一致。")
            return render_template("register.html")

        users[username] = password
        flash("注册成功，请使用新账号登录。")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    username = request.args.get("username", "访客")
    return render_template("dashboard.html", username=username)


if __name__ == "__main__":
    # 监听所有网卡，便于通过公网 IP 访问
    app.run(host="0.0.0.0", port=5000, debug=True)
