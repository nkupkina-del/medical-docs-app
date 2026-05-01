from flask import Flask, render_template

app = Flask(__name__)

# Главная страница (каталог)
@app.route("/")
def index():
    return render_template("index.html")


# Страница после "оплаты" (пока вручную)
@app.route("/success")
def success():
    return render_template("success.html")


# 👇 ВАЖНО ДЛЯ RENDER
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))