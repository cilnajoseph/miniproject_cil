from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Customers
import bs4 as bs
import urllib.request
import tweepy
from tweepy.auth import OAuthHandler
from textblob import TextBlob
# Create your views here.

def home(request):
    customers=Customers.objects.all()
    return render(request,'home.html',{'customers':customers})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect(request,'register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def googlelogin(request):
    return render(request,'google.html')

def cust_det(request,id):
    customers=Customers.objects.all()
    cust=Customers.objects.get(id=id)
    scrap_url=cust.links
    if cust.desc == "":
        source=urllib.request.urlopen(scrap_url).read()
        soup=bs.BeautifulSoup(source,'lxml')
        txt=""
        for paragraph in soup.find_all('p'):
            block=str(paragraph.text)
            if block==None:
                pass
            else:
                txt += (str(paragraph.text))
        cust.desc = txt
        cust.save()
    
    return render(request,'cust_detail.html',{'customers':customers,'cust':cust})

def help(request):
    customers=Customers.objects.all()
    return render(request,'help.html',{'customers':customers})


def sentimental(request):
    subjectivity=0
    polarity=0
    customers=Customers.objects.all()
    for customer in customers:
        print("inside loop")
        consumer_key = 'I5uJYivxN2sZRuz7JbyqIU0dg'
        consumer_secret = 'tO8kCyFHb0HwPZeq8Vvz2z9eEUc4xSXD56QhmzqrWiDSRbuahz'
        access_token = '1249729070671130624-xme25T1yhnLWHwQM9ECuJIN9u7fJss'
        access_token_secret = 'J67rF7bVEGvBdLEwGBs20Jgl0Nb59JNAakobSiocrTmAP'
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.search(customer.name)
        print("after search operation")
        for tweet in public_tweets:
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            polarity = polarity + analysis.polarity
            subjectivity = subjectivity + analysis.subjectivity
            print(analysis.sentiment)
            print("analysis is printed above")
        customer.polarity = polarity
        customer.subjectivity = subjectivity
        customer.save()
        print("after save")
    return render(request,'tweet.html',{'customers':customers})


    