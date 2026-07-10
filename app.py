from flask import Flask, render_template, redirect, request, url_for, session, flash
app = Flask(__name__)   
import os

app.secret_key = os.environ.get("SECRET_KEY", "my-secret-key")


USERS={
    "priyamrathod05@gmail.com" : "culture123"
}


@app.route("/")
def home():
    if "user" in session:
         return render_template("CULTURE-CIRCLE-MAIN.html")
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if email in USERS and USERS[email] == password:
            session["user"] = email
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password.")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/contact")
def contact():
    return render_template("Contact us.html")

if __name__ == "__main__":
    app.run(debug=True)

   