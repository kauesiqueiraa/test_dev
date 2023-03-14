def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage

    """

    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    # your code here #
    tariff_dict = {
        "Residencial": {
            "min": 0,
            "max": 150,
            "discount": 0.10,
            "coverage": 0.9,
        },
        "Comercial": {
            "min": 150,
            "max": 500,
            "discount": 0.16,
            "coverage": 0.9,
        },
        "Industrial": {
            "min": 500,
            "max": float("inf"),
            "discount": 0.20,
            "coverage": 0.9,
        }
    }

    # Calc consumo Medio
    avg_consumption = sum(consumption) / len(consumption)

    # Tarifa baseada no tipo
    tariff = None
    for key in tariff_dict:
        if key == tax_type:
            tariff = tariff_dict[key]

    # calcular desconto com base no consumo e tarifa
    discount = 0
    if avg_consumption >= tariff["min"]:
        if avg_consumption <= tariff["max"] or tariff["max"] == float("inf"):
            discount = tariff["discount"]

    # Calcular economia Anual
    annual_savings = sum(consumption) * distributor_tax * discount * tariff["coverage"] * 12

    # Calcular Economia Mensal
    monthly_savings = annual_savings / 12

    # return
    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        discount,
        tariff["coverage"],
    )

if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
