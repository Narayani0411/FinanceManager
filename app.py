from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///finance.db"
db = SQLAlchemy(app)

class Finance(db.Model):
    sr = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    expense = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.sr} - {self.amount}"
    
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def finance():
    if request.method == 'POST':
        category = request.form["category"]
        expense = request.form["expense"]
        amount = request.form["amount"]
        finance = Finance(category=category, expense=expense, amount=int(amount))
        db.session.add(finance)
        db.session.commit()
    allfin = Finance.query.all()
    return render_template('index.html', allfin=allfin)

@app.route('/dashboard')
def dash():
    result = db.session.query(
        Finance.expense,
        func.sum(Finance.amount)
    ).group_by(Finance.expense).all()

    labels = [row[0] for row in result]
    values = [row[1] for row in result]

    total_income = db.session.query(
        func.sum(Finance.amount)
    ).filter(Finance.expense == "Income").scalar()
    total_income = total_income or 0

    total_expense = db.session.query(
        func.sum(Finance.amount)
    ).filter(Finance.expense == "Expense").scalar()
    total_expense = total_expense or 0
    total_saving = total_income - total_expense
    return render_template("dashboard.html", labels=labels, values=values, total_saving=total_saving)

@app.route('/delete/<int:sr>')
def delete(sr):
    finance = Finance.query.filter_by(sr=sr).first()
    db.session.delete(finance)
    db.session.commit()
    return redirect("/")

    

if __name__ == "__main__":
    app.run(debug=False)

