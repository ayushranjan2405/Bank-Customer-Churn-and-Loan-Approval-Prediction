from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    return render(request,'index.html')

def getPrediction(CreditScore, age, tenure, balance, products, salary, active, creditcard, germany, spain, gender1):
    model = pickle.load(open('churn_pred','rb'))

    prediction = int(model.predict([[CreditScore, age, tenure, balance, products, salary, active, creditcard, germany, spain, gender1]]))

    if prediction == 0:
        return 'no'
    else:
        return 'yes'

def result(request):
    CreditScore = int(request.POST['CreditScore'])
    age = int(request.POST['age'])
    tenure = int(request.POST['tenure'])
    balance = float(request.POST['balance'])
    products = int(request.POST['products'])
    salary = float(request.POST['salary'])
    active = int(request.POST['active'])
    creditcard = int(request.POST['creditcard'])
    location1 = request.POST['location1']
    if(location1 == 'Germany'):
        germany = 1
        spain = 0
        france = 0
    elif(location1 == 'Spain'):
        germany = 0
        spain = 1
        france = 0
    else:
        germany = 0
        spain = 0
        france = 1
    gender1 = int(request.POST['gender1'])

    result = getPrediction(CreditScore, age, tenure, balance, products, salary, active, creditcard, germany, spain, gender1)
    return render(request, 'result1.html', {'result': result})