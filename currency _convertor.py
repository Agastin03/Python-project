def currency_convertor(amount,currency):
    rates={
            "usd_to_eur":0.85,
            "eur_to_usd":1.18,
            "usd_to_gbp":0.75,
            "gbp_to_usd":1.33
            }
    rate=rates.get(currency,None)
    if rate:
        return amount*rate
    else:
        return"invalid currency pair"
print(currency_convertor(100,"usd_to_eur"))
print(currency_convertor(100,"eur_to_usd"))
print(currency_convertor(100,"usd_to_inr"))
