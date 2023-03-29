from django.shortcuts import render
from .models import ConversionRate
from .models import CryptoCurrency
# Create your views here.

def index(request):
    conversion_rate = ConversionRate.objects.get(from_currency='BTC', to_currency='USD')
    btc_amount = float(request.GET.get('btc_amount'))
    usd_amount = btc_amount * conversion_rate.rate
    
    return render(request, 'index.html', {'amount':usd_amount})


def crypto_converter(request):
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

    return render(request, 'crypto_converter.html', context)
