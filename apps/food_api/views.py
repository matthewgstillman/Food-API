from django.shortcuts import render, redirect
from api_keys import api_keys
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("Making A POST Request")
        food_name = request.POST['food_name']
        request.session['food_name'] = food_name
        session_food =  request.session['food_name']
        print("Session Food: {}".format(session_food))
        print("Food Name: {}".format(food_name))
        context = {
            'food_name': food_name,
            'session_food': session_food,
        }
        return redirect('/result', context)
    if request.method == 'GET':
        # url_root = "https://www.themealdb.com/api/json/v1/"
        # api_key = api_keys['api_key']
        # print(api_key)
        # url_tail = "/random.php"
        # url = str(url_root) + str(api_key) + str(url_tail)
        # response = requests.get(url)
        # random_food = response.json()
        # print(random_food)
        print("Making a GET Request")
        return render(request, 'food_api/index.html')

def result(request):
    food_name = request.session['food_name']
    print("Food Name: {}".format(food_name))
    context = {
        'food_name': food_name,
    }
    return render(request, 'food_api/result.html', context)

def categories(request):
    url = 'https://www.themealdb.com/api/json/v1/1/categories.php'
    response = requests.get(url)
    categories = response.json()
    print("Categories: {}".format(categories))
    context = {
        'categories': categories,
    }
    return render(request, 'food_api/categories.html', context)
