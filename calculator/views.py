from django.shortcuts import render

from calculator.calculator import calculator


# Create your views here.
def calculate_savings(request):
    consumption = [1518, 1071, 968]
    distributor_tax = 0.95871974
    tax_type = "Industrial"

    savings = calculator(consumption, distributor_tax, tax_type)

    context = {
        "annual_savings": savings[0],
        "monthly_savings": savings[1],
        "applied_discount": savings[2],
        "coverage": savings[3],
    }

    return render(request, "index.html", context)
