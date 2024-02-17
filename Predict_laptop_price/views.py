from django.shortcuts import render
import pandas as pd
from .helper import Data, predict_price

Brands, Type_name, Ram, Gpu, Cpu, Ssd, Hdd, min_w, max_w = Data()


# Create your views here.
def home(request):
    context = {
        "brands": Brands,
        "types": Type_name,
        "rams": Ram,
        "gpus": Gpu,
        "cpus": Cpu,
        "ssds": Ssd,
        "hdds": Hdd,
        "resolutions": ['1366x768','1600x900','1920x1080','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'],
        "min_weight": min_w,
        "max_weight": max_w,
    }

    if request.method=="POST":
        company = request.POST.get('company')
        type_name = request.POST.get('type')
        ram = request.POST.get('ram')
        weight = request.POST.get('weight')
        gpu = request.POST.get('gpu')
        cpu = request.POST.get('cpu')
        ssd = request.POST.get('ssd')
        hdd = request.POST.get('hdd')
        resolution = request.POST.get('resolution')
        touchscreen = 1 if request.POST.get('touchscreen')=="Yes" else 0
        ips = 1 if request.POST.get('ips')=="Yes" else 0
        screensize = float(request.POST.get('screensize'))
        weight = request.POST.get('weight')
        
        result =  predict_price(company, type_name, ram, weight, touchscreen, ips, screensize, resolution, cpu, hdd, ssd, gpu)
           

        context={
            "brand": company,
            "type": type_name,
            "ram": ram,
            "weight": weight,
            "gpu": gpu,
            "cpu": cpu,
            "ssd": ssd,
            "hdd": hdd,
            "resolution": resolution,
            "touchscreen": "Yes" if touchscreen==1 else "No",
            "ips": "Yes" if ips==1 else "No",
            "screensize": screensize,
            "weight": weight,
            "result":result
        }
           
            

        return render(request, 'Predict_laptop_price/result.html', context)
    
    return render(request, 'Predict_laptop_price/index.html', context)