from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Demo credentials (replace with DB validation in production)
DEMO_USER = "admin"
DEMO_PASSWORD = "123456"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == DEMO_USER and password == DEMO_PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))

        flash("用户名或密码错误，请重试。", "error")

    return render_template("login.html", public_ip="101.201.59.152")


@app.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    # 使用公网访问时建议绑定 0.0.0.0
    app.run(host="0.0.0.0", port=5000, debug=True)
