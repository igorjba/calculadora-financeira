from flask import Flask, render_template, request
from typing import Tuple

app = Flask(__name__)

def calculate_required_time(principal: float, interest_rate: float, monthly_contribution: float, desired_amount: float) -> Tuple[int, float]:

    interest_rate_decimal = interest_rate / 100.0
    months = 0
    while principal < desired_amount:
        principal = (principal + monthly_contribution) * (1 + interest_rate_decimal)
        months += 1
    return months, principal

@app.route('/')
def index():
    return render_template('index_investment_calculation.html')

@app.route('/calculate_time', methods=['POST'])
def calculate_time():

    principal = float(request.form.get('aporteInicial', 0))
    interest_rate = float(request.form.get('taxaJuros', 0))
    monthly_contribution = float(request.form.get('aporteMensal', 0))
    desired_amount = float(request.form.get('montanteDesejado', 0))
    
    months_needed, final_amount = calculate_required_time(principal, interest_rate, monthly_contribution, desired_amount)
    
    return render_template('result_investment_calculation.html', time=months_needed, final_amount=final_amount)

if __name__ == '__main__':
    app.run(debug=True)
