from django.shortcuts import render

import pickle

def index(request):
    return render(request, 'index.html')

def kcancer(request):
    return render(request, 'kidneycancer.html')

def bmi(request):
    return render(request, 'bmi.html')

def bcancer(request):
    return render(request, 'breastcancer.html')

def hcancer(request):
    return render(request, 'heartcancer.html')

def lcancer(request):
    return render(request, 'lungcancer.html')

def bform(request):
    return render(request, 'breastform.html')

def hform(request):
    return render(request, 'heartform.html')

def lform(request):
    return render(request, 'lungform.html')

def kform(request):
    return render(request, 'kidneyform.html')


def main(request):
    with open('breast_model', 'rb') as file:
        model = pickle.load(file)

    a1 = float(request.GET['b1'])
    a2 = float(request.GET['b2'])
    a3 = float(request.GET['b3'])
    a4 = float(request.GET['b4'])
    a5 = float(request.GET['b5'])
    a6 = float(request.GET['b6'])
    a7 = float(request.GET['b7'])
    a8 = float(request.GET['b8'])
    a9 = float(request.GET['b9'])
    a10 = float(request.GET['b10'])
    a11 = float(request.GET['b11'])
    a12 = float(request.GET['b12'])
    a13 = float(request.GET['b13'])
    a14 = float(request.GET['b14'])
    a15 = float(request.GET['b15'])

    breastpred = model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15]])

    result1 = ''

    if breastpred == [0]:
        result1= "This patient does not have breast cancer"
    else:
        result1= 'This patient has been diagnosed with breast cancer '

    return render (request, 'breastform.html', {"breastresult": result1 })



def heart(request):
    with open('heart_model', 'rb') as file:
        model = pickle.load(file)

    c1 = int(request.GET['h1'])
    c2 = int(request.GET['h2'])
    c3 = int(request.GET['h3'])
    c4 = int(request.GET['h4'])
    c5 = int(request.GET['h5'])
    c6 = int(request.GET['h6'])
    c7 = int(request.GET['h7'])
    c8 = int(request.GET['h8'])
    c9 = int(request.GET['h9'])

    heartpred = model.predict([[c1,c2,c3,c4,c5,c6,c7,c8,c9]])

    result2 = ''

    if heartpred == [0]:
        result2= "This patient does not have heart cancer"
    else:
        result2= 'This patient has been diagnosed with heart cancer '

    return render (request, 'heartform.html', {"heartresult": result2 })


def kidney(request):
    with open('kidney_model', 'rb') as file:
        model = pickle.load(file)

    d1 = float(request.GET['k1'])
    d2 = float(request.GET['k2'])
    d3 = float(request.GET['k3'])
    d4 = float(request.GET['k4'])
    d5 = float(request.GET['k5'])
    d6 = float(request.GET['k6'])
    d7 = float(request.GET['k7'])
    d8 = float(request.GET['k8'])
    d9 = float(request.GET['k9'])
    d10 = float(request.GET['k10'])
    d11 = float(request.GET['k11'])
    d12 = float(request.GET['k12'])
    d13 = float(request.GET['k13'])
    d14 = float(request.GET['k14'])
    d15 = float(request.GET['k15'])

    kidneypred = model.predict([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]])

    result3 = ''

    if kidneypred == [0]:
        result3= "This patient has been diagnosed with kidney cancer "
    else:
        result3= 'This patient does not have kidney cancer'

    return render (request, 'kidneyform.html', {"kidneyresult": result3 })


def lung(request):
    with open('lung_model', 'rb') as file:
        model = pickle.load(file)

    f1 = float(request.GET['l1'])
    f2 = float(request.GET['l2'])
    f3 = float(request.GET['l3'])
    f4 = float(request.GET['l4'])
    f5 = float(request.GET['l5'])
    f6 = float(request.GET['l6'])
    f7 = float(request.GET['l7'])
    f8 = float(request.GET['l8'])
    f9 = float(request.GET['l9'])
    f10 = float(request.GET['l10'])
    f11 = float(request.GET['l11'])
    f12 = float(request.GET['l12'])

    lungpred = model.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]])

    result4 = ''

    if lungpred == [1]:
        result4= "This patient has been diagnosed with lung cancer "
    else:
        result4= 'This patient does not have lung cancer'

    return render (request, 'lungform.html', {"lungresult": result4 })