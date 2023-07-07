from django.shortcuts import render
from app1.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def displaytopic(request):
    TO=Topic.objects.all()
    TO=Topic.objects.filter(topic_name='volleyboll')
    d={'T':TO}
    return render(request,'displaytopic.html',d)
def displaywebpage(request):
    WO=Webpage.objects.all()[0:3:]
    WO=Webpage.objects.all()
    WO=Webpage.objects.filter(topic_name='volleyboll')
    WO=Webpage.objects.all()
    WO=Webpage.objects.all().order_by('name')
    #WO=Webpage.objects.all().order_by('_name')
    WO=Webpage.objects.all().order_by(Length('name'))
    WO=Webpage.objects.all().order_by(Length('name').desc())
    WO=Webpage.objects.filter(url__startswith='abc.in')
    WO=Webpage.objects.filter(url__endswith='com')
    WO=Webpage.objects.filter(url__contains='abc.in')
    WO=Webpage.objects.filter(name__contains='D')
    wo=Webpage.objects.filter(name__in=['dhoni','ronaldo'])
    wo= Webpage.objects.filter(name__regex='p\w+')
    wo=Webpage.objects.filter(Q(name='d')|Q(url__startswith='dhoni.com'))
    WO=Webpage.objects.all()
    wo=Webpage.objects.filter(Q(name='abc') | Q(url__startswith='dhoni.com'))
    wo=Webpage.objects.filter(Q(name='d')&Q(url__startswith='dhoni.com'))
    wo=Webpage.objects.filter(name='dhoni').update(url='DHONI.COM')
    wo=Webpage.objects.filter(topic_name='cricket').update(name='DHONI')
    wo=Webpage.objects.filter(topic_name='football').update(url='ASD.COM')
    WO=Webpage.objects.all()
    CTO=Topic.objects.get(topic_name='cricket')
    wo=Webpage.objects.update_or_create(name='virat',defaults={'topic_name':CTO, 'name':virat,'url' :virat.COM})
    

    d={'W':WO}
    return render(request,'displaywebpage.html',d)
def displayaccessrecord(request):
    AR=AccessRecord.objects.all()
    AR=AccessRecord.objects.filter(date='2023-02-08')
    AR=AccessRecord.objects.filter(date__gt='2022-04-06')
    AR=AccessRecord.objects.filter(date__lt='2022-04-06')
    AR=AccessRecord.objects.filter(date__gte='2022-04-06')
    AR=AccessRecord.objects.filter(date__lte='2022-04-06')
    AR=AccessRecord.objects.filter(date__year='2022')
    AR=AccessRecord.objects.filter(date__month='04')
    AR=AccessRecord.objects.filter(date__day='08')
    AR=AccessRecord.objects.filter(date__year__gt='2022')
    AR=AccessRecord.objects.filter(date__year__lt='2023')
    AR=AccessRecord.objects.filter(date__day__gt='06')
    d={'AR':AR}
    return render(request,'displayar.html',d)

def deletewebpage(request):
    WO=Webpage.objects.filter(name='DHONI').delete()
    d={'W':WO}
    return render(request,'displaywebpage.html',d)