from django.shortcuts import render

# Create your views here.
def index(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    price = 0
    if thing in product_price.keys():
        price = product_price[thing] * cnt
    context = {
        'thing':thing,
        'cnt':cnt,
        'price':price,
    }
    return render(request, 'prices/index.html', context)