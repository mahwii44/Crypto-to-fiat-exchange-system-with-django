from django.shortcuts import render
from .models import ConversionRate

# Create your views here.

def index(request):
    conversion_rate = ConversionRate.objects.get(from_currency='BTC', to_currency='USD')
    btc_amount = float(request.GET.get('btc_amount'))
    usd_amount = btc_amount * conversion_rate.rate
    
    return render(request, 'index.html', {'amount':usd_amount})