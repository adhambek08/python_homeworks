def invest(amount, rate, years):
    for year in range(1, years +1):
        amount = amount * (1 + rate)
        print(f'year {year}: ${round(amount,2):.2f}')

amount = float(input('Enter initial amount:'))
rate = float(input('Enter annual rate (e.g. 0.05 for 5%)'))
years = int(input('Enter the number of years:'))

invest(amount, rate, years)