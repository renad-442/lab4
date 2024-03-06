from django.shortcuts import render
from django.http import HttpResponse

rateOfTax = 15

def index(request):
    return HttpResponse("<h1>This is a site to calculate Tax</h1>")

def calculate_price_withTax(request, num):
    price = num * (1 + rateOfTax/100)
    return HttpResponse(f"<h1>Total Price after 15% tax: {price}</h1>")

def view_Tax(request):
    return render(request, "claculateTax/index.html", {'tax_rate': rateOfTax})
