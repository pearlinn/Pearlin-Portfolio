from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_folder='static')

app.config["DEBUG"] = True

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("forum.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)