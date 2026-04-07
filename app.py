from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-secret-key"

# 演示账号（生产环境请改为数据库校验）
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "123456"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == DEMO_USERNAME and password == DEMO_PASSWORD:
            return redirect(url_for("dashboard", username=username))

        flash("用户名或密码错误，请重试。")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    username = request.args.get("username", "访客")
    return render_template("dashboard.html", username=username)


if __name__ == "__main__":
    # 监听所有网卡，便于通过公网 IP 访问
    app.run(host="0.0.0.0", port=5000, debug=True)
