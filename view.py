from django.shortcuts import render
from .models import Video
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from .serializers import VideoSerializer,VideoPathSerializer,VideoPath
from django.db.models import Q
import json


@api_view(['OPTIONS','POST']) 
def SendVideo(request):

    try:
        if request.method == "OPTIONS": 
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            response['Access-Control-Max-Age'] = 1000
            # note that '*' is not valid for Access-Control-Allow-Headers
            response['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
            return response

        print(request.content_type) 
        if request.content_type == 'application/json' or request.content_type == "application/x-www-form-urlencoded; charset=UTF-8":
            cat = request.body.decode('utf-8')
            temp = json.loads(cat)
            video_name = temp['video_name']
            Bandwidth = float(temp['Bandwidth'])
            StartTime = temp['StartTime']
            #a = time.time()
            #test = pyspeedtest.SpeedTest('www.youtube.com')
            #Bandwidth = test.download()/10000
            #b = time.time()

            video = Video.objects.filter(name=video_name).values_list('ResolutionHigh', 'ResolutionMedium','ResolutionLow')

        else:
            d={}
            d['errors']="Please send data in json format"
            return JsonResponse(d)

        if Bandwidth >=5 :
            path = video[0][0]
            vid = {}
            vid['Resolution']=path
            vid['video_name']=video_name
            vid['StartTime'] = StartTime
            #vid['time'] = b-a
            #obj = VideoPath(vid)
            #s = VideoPathSerializer(obj)
            #res=Response(s.data)
            res =Response(vid,status=status.HTTP_201_CREATED)


        	
        elif Bandwidth<5 and Bandwidth >=3:
            path = video[0][1]
            vid = {}
            vid['Resolution']=path
            vid['video_name']=video_name
            vid['StartTime'] = StartTime
            #vid['time'] = b-a
            #obj =VideoPath(vid)
            #s = VideoPathSerializer(obj)
            #res=Response(s.data)
            res =Response(vid,status=status.HTTP_201_CREATED)

        	
        else:
            path = video[0][2]
            vid = {}
            vid['Resolution']=path
            vid['video_name']=video_name
            vid['StartTime'] = StartTime
            #vid['time'] = b-a
            #obj = VideoPath(vid)
            #s = VideoPathSerializer(obj)
            #res=Response(s.data)
            res =Response(vid,status=status.HTTP_201_CREATED)


        
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    
    if request.method == 'POST':
        
        return res
    else:
        return Response({"Only Post method is allowed"})
