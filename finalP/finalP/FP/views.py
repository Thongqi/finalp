from rest_framework import serializers as serializers
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Places, States

import json

# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

def index(request):
    if request.method == 'POST':
        destination = request.POST
        
        return redirect(qa)
    



    else:
        places = Places.objects.all()
        return render(request, "FP/index.html", {
            
        })
    

# autocomplete search box API
def places(request):
    places = list(States.objects.values("states"))
    # places = serializers.serialize("json", places)
    return JsonResponse({"places":places}, safe=False)


def qa(request):
    if request.method == 'POST':
        tag = request.POST.getlist('chk[]')
        days = request.POST.get('select_days')
        budget = request.POST.get('budget')

        places = list(Places.objects.values("name"))
  
        # DAY 1-2
        if 'Outdoor' in tag or 'Nature' in tag:
            day_1_2 = 'Telaga 7 Waterfall'
        else:
            day_1_2 = 'Crocodile Adventure Land'

        if 'History' in tag or 'Culture' in tag:
            day_2_2 = 'Kota Mahsuri'
        else:
            day_2_2 = 'Underwater World Langkawi'

        if days == '3D2N':
            if day_1_2 != 'Crocodile Adventure Land':
                day_3_2 =  'Temurun Waterfall'
            elif 'Animal' in tag:
                day_3_2 =  'Crocodile Adventure Land'
            
            day_3_1 = None
            day_4_2 = None
        else:
            if day_1_2 != 'Crocodile Adventure Land':
                day_4_2 = 'Temurun Waterfall'
                day_3_2 = None
            elif 'Animal' in tag:
                day_3_2 =  'Crocodile Adventure Land'
            else:
                day_3_2 = None
                day_4_2 = None
            if 'Animal' in tag:
                day_3_1 = 'Langkawi Wildlifre Park'
            else:
                day_3_1 = 'Kilim Geoforest Park'

        return render(request, "FP/itinerary.html", {
            "tag":tag,
            "days": days,
            "budget": budget,
            "places": places,
            "day_1_2": day_1_2,
            "day_2_2":day_2_2,
            "day_3_2":day_3_2,
            "day_3_1": day_3_1,
            "day_4_2": day_4_2,
        })
    else:
        tags = [c[0] for c in Places.OPTIONS]
        return render(request, "FP/qa.html", {
            "tags":tags,
        })
# calculate distance from place to place
# data = request.body
#         data = data.decode('utf-8')

#         data = json.loads(data)
#         start = data.get("from", "")
#         end = data.get("to", "")
       
#         start_coor= Places.objects.get(name = start).location
#         end_coor = Places.objects.get(name = end).location
        
#         return JsonResponse({"start":start_coor, "end":end_coor}, safe=False)
#         return render(request, "FP/index.html", {
#             "start": start,
#         })

def itinerary (request):
    
    return render(request, "FP/itinerary.html")

