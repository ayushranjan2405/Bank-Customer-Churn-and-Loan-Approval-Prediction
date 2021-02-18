from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    return render(request,'index.html')

def getPrediction(gender2, married2, dependents, graduate2, se2,  applicantIncome, CoapplicantIncome, loanAmount, LoanAmountTerm, creditHistory, propertyArea):
    model = pickle.load(open('Loan_pred','rb'))

    prediction = int(model.predict([[gender2, married2,  dependents, graduate2, se2, applicantIncome, CoapplicantIncome, loanAmount, LoanAmountTerm, creditHistory, propertyArea]]))

    if prediction == 0:
        return 'no'
    else:
        return 'yes'

def result(request):
    gender2 = int(request.POST['gender2'])
    married2 = int(request.POST['married2'])
    graduate2 = int(request.POST['graduate2'])
    se2 = int(request.POST['se2'])
    dependents = int(request.POST['dependents'])
    applicantIncome = float(request.POST['applicantIncome'])
    CoapplicantIncome = float(request.POST['CoapplicantIncome'])
    loanAmount = float(request.POST['loanAmount'])
    LoanAmountTerm = int(request.POST['LoanAmountTerm'])
    creditHistory = float(request.POST['creditHistory'])
    propertyArea = request.POST['propertyArea']
    if(propertyArea == 'Urban'):
        propertyArea = 2
    elif(propertyArea == 'Rural'):
        propertyArea = 0
    else:
        propertyArea = 1
    result = getPrediction(gender2, married2, dependents, graduate2, se2, applicantIncome, CoapplicantIncome, loanAmount, LoanAmountTerm, creditHistory, propertyArea)
    return render(request,'result2.html',{'result': result})