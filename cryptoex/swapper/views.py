from django.shortcuts import render
from urllib import response
##from .models import ConversionRate
from .models import CryptoCurrency
import requests
# Create your views here.

#def index(request):
 #   conversion_rate = ConversionRate.objects.get(from_currency='BTC', to_currency='USD')
  #  btc_amount = float(request.GET.get('btc_amount'))
  #  usd_amount = btc_amount * conversion_rate.rate
    
  #  return render(request, 'index.html', {'amount':usd_amount})


def index(request):
    # Get all available cryptocurrencies from the database
    cryptocurrencies = CryptoCurrency.objects.all()

    if request.method == 'POST':
        # Get the selected cryptocurrency and the amount to convert from the submitted form
        selected_crypto = request.POST.get('crypto')
        amount = float(request.POST.get('amount'))

        # TODO: Convert the amount to fiat USD using the selected cryptocurrency's exchange rate

        context = {
            'cryptocurrencies': cryptocurrencies,
            'selected_crypto': selected_crypto,
            'amount': amount,
            # TODO: Add the converted amount to the context
        }
    else:
        context = {
            'cryptocurrencies': cryptocurrencies,
        }

    return render(request, 'index.html', context)

# Function to get cryptocurrency data from the CoinMarketCap API
def get_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your_api_key_here'
}
    parameters = {
    'symbol': 'BTC',
    'convert': 'USD'
}

    response = requests.get(url, headers=headers, params=parameters)

if response.status_code == 200:
    data = response.json()
    price = data['data']['BTC']['quote']['USD']['price']
    print(f"Latest BTC-USD price: {price:.2f}")
else:
    print(f"Error {response.status_code}: {response.reason}")

# Function to convert the selected cryptocurrency amount to USD
def convert_to_usd(crypto, amount):
    data = get_crypto_data()
    for item in data:
        if item['symbol'] == crypto:
            price = float(item['price_usd'])
            converted_amount = round(price * float(amount), 2)
            return converted_amount
    return None
