from django.shortcuts import render, redirect
from crypto_app.lstm_prediction import *
import yfinance as yf
from yahoo_finance import Share
from .models import Crypto
from .forms import CryptoForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def redirect_root(request):
    return redirect('/crypto_app/index')
def cryptohome(request):
	niftyD = yf.Ticker("BTC-USD")
	niftyDa = niftyD.info
	niftyData = niftyDa['regularMarketPrice']
	print(niftyDa)
	sensexD = yf.Ticker("ETH-USD")
	sensexDa = sensexD.info
	sensexData = sensexDa['regularMarketPrice']
	cryptos = ["BTC-USD","ETH-USD","USDT-USD","BNB-USD","USDC-USD","ADA-USD","SOL-USD","HEX-USD","XRP-USD","LUNA1-USD"]
	finalCryptoData = []
	for i in cryptos:
		tempD = yf.Ticker(i)
		tempDa = tempD.info
		tempName = tempDa['shortName']
		tempSymbol = tempDa['symbol']
		tempOpen = tempDa['regularMarketOpen']
		tempClose = tempDa['regularMarketPreviousClose']
		tempHigh = tempDa['dayHigh']
		tempLow = tempDa['dayLow']
		temp = []
		temp.append(tempName)
		temp.append(tempSymbol)
		temp.append(tempOpen)
		temp.append(tempClose)
		temp.append(tempHigh)
		temp.append(tempLow)
		finalCryptoData.append(temp)
	dataBTC = finalCryptoData[0]
	dataETH = finalCryptoData[1]
	dataUSDT = finalCryptoData[2]
	dataBNB = finalCryptoData[3]
	dataUSDC = finalCryptoData[4]
	dataADA = finalCryptoData[5]
	dataSOL = finalCryptoData[6]
	dataHEX = finalCryptoData[7]
	dataXRP = finalCryptoData[8]
	dataLUNA1= finalCryptoData[9]
	#print(dataReliance,dataTcs,dataHdfcbank,dataInfy,dataIcicibank,dataHindu,dataSbi,dataHdfc,dataBajaj,dataBhartiAirtel)
	#niftyData = yf.download(tickers='^NSEI', period='5d', interval='5m')
	#sensexData = yf.download(tickers='^BSESN', period='5d', interval='5m')
	return render(request,'crypto_app/cryptohome.html',{'niftydata':niftyData,'sensexdata':sensexData,'finalCryptoData':finalCryptoData})
def index(request):
	return render(request, 'crypto_app/index.html') 

def predCrypt(request):
    return render(request, 'crypto_app/prediction.html')

def contact(request):
	return render(request, 'crypto_app/contact.html')

def searchCrypt(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'crypto_app/search.html', {"predicted_result_df": predicted_result_df})

def add_crypto(request):
	import requests
	import json
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = CryptoForm(request.POST or None)
		
			if form.is_valid():
				form.save()
				messages.success(request, ("Crypto has been added to your portfolio!"))				
				return redirect('add_crypto')

		else:	
			ticker = Crypto.objects.all()
			# pass in url that calls the api
			# save ticker info from api output into python list ('output list')
			output = []
			# modify to pull multiple stock tickers at the same time
			for ticker_item in ticker:
				#api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=</your_api_key>")
				msft = str(ticker_item) + "-USD"
				msft_data = yf.Ticker(msft)
				api = msft_data.info
				try:
					output.append(api)
				except Exception as e:
					api = "Error..."
			return render(request, 'crypto_app/add_crypto.html', {'ticker': ticker, 'output':  output})
	return HttpResponseRedirect('adminlogin')
def delete(request, crypto_id):
	item = Crypto.objects.get(pk=crypto_id) # call database by primary key for id #
	item.delete()
	messages.success(request, ("Crypto Has Been Deleted From Portfolio!"))
	return redirect(add_crypto)