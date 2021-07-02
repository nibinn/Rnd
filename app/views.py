from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import *
from .models import *
from django.http import HttpResponseRedirect

import pandas as pd
import joblib
reloadModel=joblib.load('./models/xgbostModel.pkl')

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
# @login_required(login_url="/login/")
def add_customer(request):
    # form = CustomerForm()
    if request.method=='POST':
        form = CustomerForm(request.POST)
        print("form:",form)
        print(form.errors)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            phone=form.cleaned_data['phone']
            print("name",name)
            customer=Customer(name=name,email=email,address=address,phone_number=phone)
            customer.save()
            return HttpResponseRedirect('/add_customer/')

        else:
            print("not valid")
    else:
        form=CustomerForm()
    return render(request, 'add-customer.html', {'form': form})
def show_customer(request):
    cus_list=Customer.objects.all()
    print("cus_list:",cus_list)
    return render(request,'customer_list.html',{'cus_list':cus_list})
    

def foc_calculation(request):
    context= {'form':FOCPredictionForm}
    return render(request,'Foc_form.html',context)

def foc_prediction(request):
    print(request)
    temp={}
    if request.method == 'POST':
        print(type(float(request.POST["draft"])))
        temp['Draft(m)'] = float(request.POST["draft"])
        temp['Age']=float(request.POST["age"])
        temp['STW_kn']=float(request.POST["stw_kn"])
        temp['Model_Sea_State_D']=float(request.POST["model_sea_state_d"])
        temp['Number_of_Months_after_Dry_Dock']=float(request.POST["no_of_months_after_dry_dock"])
        temp['DWT(T)']=float(request.POST["dwt"])
    testData=pd.DataFrame({'x':temp}).transpose()
    clist=['STW_kn','Model_Sea_State_D','Draft(m)','Age','DWT(T)','Number_of_Months_after_Dry_Dock']
    testData = testData[clist]
    print(testData)
    scoreval=reloadModel.predict(testData)[0]
    context= {'scoreval':scoreval}
    return render(request,'customer_list.html',context)
    
    