from flask import Flask, render_template

app = Flask(__name__)

PAYMENT_LINK = "https://merch.tochka.com/order/?uuid=724dcac7-2302-4816-98f4-d2569284f20c"
DOCUMENT_LINK = "https://disk.yandex.ru/i/Q7wrZ0pvg2XmXA"

documents = [
    {
        "category": "Внутренний контроль качества и безопасности медицинской деятельности",
        "title": "Приказ «Об утверждении Положения о порядке организации и проведения внутреннего контроля качества и безопасности медицинской деятельности», назначение ответственных",
        "price": "300 ₽",
    },
    {
        "category": "Внутренний контроль качества и безопасности медицинской деятельности",
        "title": "Положение о порядке организации и проведения внутреннего контроля качества и безопасности медицинской деятельности",
        "price": "300 ₽",
    },
    {
        "category": "Внутренний контроль качества и безопасности медицинской деятельности",
        "title": "Должностные инструкции (уполномоченный и врач)",
        "price": "300 ₽",
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        documents=documents,
        payment_link=PAYMENT_LINK
    )

@app.route("/success")
def success():
    return render_template(
        "success.html",
        document_link=DOCUMENT_LINK
    )

app.run()