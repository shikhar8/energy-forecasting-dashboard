from django.shortcuts import render
from json import dumps
import csv
import os


def home_page(request):
    return render(request, 'blog/testingHome.html', {})


def cost(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\costDataToday.csv"))
    input_file2= csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\costDataPredicted.csv"))
    arr1=[]
    arr2=[]
    arr3=[]
    data_dictionary={}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
    for row in input_file2:
        arr3.append(row['Y_Value'])
    data_dictionary['X_Value']=arr1
    data_dictionary['Z_Value']=arr2
    data_dictionary['Y_Value']=arr3
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingCost.html', {'data':data_json})


def consumer_demand_map(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\loadData.csv"))
    input_file2 = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\Eload.csv"))
    data_dictionary = {}
    for row in input_file2:
        data_dictionary['ELoad']=row['Eload']
    arr1=[]
    arr2=[]
    mn=100000000
    mx=0
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
        mn=min(mn, float(row['Y_Value']))
        mx=max(mx, float(row['Y_Value']))
    data_dictionary['X_Value']=arr1
    data_dictionary['Y_Value']=arr2
    data_dictionary['Max']=mx
    data_dictionary['Min']=mn
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingConsumerDemandMap.html', {'data':data_json})

def prosumer_supply(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\Pgreen_f.csv"))
    arr1=[]
    arr2=[]
    arr3=[]
    data_dictionary = {}
    input_file2 = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__)) + "\\Egreen.csv"))
    for row in input_file2:
        data_dictionary['EPv']=row['Pv']
        data_dictionary['EWind'] = row['Wind']
        data_dictionary['EGreen'] = row['Green']
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y1_Value'])
        arr3.append(row['Y2_Value'])
    data_dictionary['X_Value']=arr1
    data_dictionary['Y_Value']=arr2
    data_dictionary['Z_Value']=arr3
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingProsumerSupply.html', {'data':data_json})

def conventional_energy_generated(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\Pgrid.csv"))
    arr1=[]
    arr2=[]
    data_dictionary={}
    input_file2 = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__)) + "\\EConventional.csv"))
    for row in input_file2:
        data_dictionary['EGrid']=row['Grid']
        data_dictionary['EEss']=row['Ess']
        data_dictionary['EGreen']=row['Green']
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
    data_dictionary['X_Value']=arr1
    data_dictionary['Y_Value']=arr2
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingConventionalEnergyGenerated.html', {'data':data_json})

def accuracy_of_forecasting_models(request):
    return render(request, 'blog/testingAccuracyOfForcastingModels.html', {})

def scheduling_decision_report(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\schedule_report.csv"))
    arr1=[]
    arr2=[]
    arr3=[]
    arr4=[]
    arr5=[]
    data_dictionary={}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y1_Value'])
        arr3.append(row['Y2_Value'])
        arr4.append(row['Y3_Value'])
        arr5.append(row['Y4_Value'])
    data_dictionary['X_Value']=arr1
    data_dictionary['Y1_Value']=arr2
    data_dictionary['Y2_Value'] = arr3
    data_dictionary['Y3_Value'] = arr4
    data_dictionary['Y4_Value'] = arr5
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingSchedulingDecisionReport.html', {'data':data_json})


def contact_us(request):
    return render(request, 'blog/testingContactUs.html', {})

def load_power_accuracy(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__)) + "\\loadrealData.csv"))
    arr1 = []
    arr2 = []
    arr3 = []
    data_dictionary = {}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
        arr3.append(row['Z_Value'])
    data_dictionary['X_Value'] = arr1
    data_dictionary['Y_Value'] = arr2
    data_dictionary['Z_Value'] = arr3
    data_json = dumps(data_dictionary)
    return render(request, 'blog/testingLoadPowerAccuracy.html', {'data':data_json})

def solar_power_accuracy(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__)) + "\\Ppv_realf.csv"))
    arr1 = []
    arr2 = []
    arr3 = []
    data_dictionary = {}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
        arr3.append(row['Z_Value'])
    data_dictionary['X_Value'] = arr1
    data_dictionary['Y_Value'] = arr2
    data_dictionary['Z_Value'] = arr3
    data_json = dumps(data_dictionary)
    return render(request, 'blog/testingSolarPowerAccuracy.html', {'data':data_json})

def wind_power_accuracy(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__)) + "\\Pwind_realf.csv"))
    arr1 = []
    arr2 = []
    arr3=[]
    data_dictionary = {}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
        arr3.append(row['Z_Value'])
    data_dictionary['X_Value'] = arr1
    data_dictionary['Y_Value'] = arr2
    data_dictionary['Z_Value'] = arr3
    data_json = dumps(data_dictionary)
    return render(request, 'blog/testingWindPowerAccuracy.html', {'data':data_json})

def cost_accuracy(request):
    input_file = csv.DictReader(open(os.path.dirname(os.path.realpath(__file__))+"\\costrealData.csv"))
    arr1=[]
    arr2=[]
    arr3=[]
    data_dictionary={}
    for row in input_file:
        arr1.append(row['X_Value'])
        arr2.append(row['Y_Value'])
        arr3.append(row['Z_Value'])
    data_dictionary['X_Value']=arr1
    data_dictionary['Y_Value']=arr2
    data_dictionary['Z_Value']=arr3
    data_json=dumps(data_dictionary)
    return render(request, 'blog/testingCostAccuracy.html', {'data':data_json})
