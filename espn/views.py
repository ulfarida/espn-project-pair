from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Berita, Detail, Team, Match
import datetime
import pytz
import collections
# Create your views here.
def index(request):
    berita_object = Berita.objects.all().order_by('-createdat')
    nau = datetime.datetime.now(pytz.utc)
    return render(request, 'espn/index.html', {'berita_object':berita_object,'nau':nau})

def sport(request, sportstr):
    
    sportstr = sportstr.capitalize()
    sport_news = Berita.objects.filter(sport=sportstr).order_by('-createdat')
    nau = datetime.datetime.now(pytz.utc)

    return render(request, 'espn/index.html', {'berita_object':sport_news,'nau':nau})

def peritem(request, bar, foo):

    nau = datetime.datetime.now(pytz.utc)
    
    peritem_news = Berita.objects.filter(sport=bar).filter(id__lte=foo).order_by('-createdat')
    
    return render(request, 'espn/index.html', {'berita_object':peritem_news,'nau':nau})


def news(request, sportstr, new_id):
    berita_object = Berita.objects.all().order_by('-createdat')
    newdetail = Berita.objects.get(pk=new_id)
    sportstr = sportstr
    var = {'baru':newdetail, 'beritas' : berita_object, 'sportstr' : sportstr}
    return render(request, 'espn/news.html', var)

def scores(request, sportstr):
    # sportstr2 = sportstr.lower()
    matchs = Match.objects.filter(sport=sportstr).order_by('-takes_time')

    # matchs2 = Match.objects.all()
    # for j in matchs2
    replace = []
    # packed = namedtuple('packed', ['obj','hp','ap'])
    for i in matchs:
        #print(i.home_team_id)
        dict_ref = {
            'i': i,
            'h': i.home_team_id.team_image,
            'a': i.away_team_id.team_image
        }
        h_pic = i.home_team_id.team_image
        a_pic = i.away_team_id.team_image
        # p = packed(i,h_pic,a_pic)
        replace.append(dict_ref)
    var = {'matchs' : replace,'sportstr':sportstr}
    return render(request, 'espn/score.html', var)

def download(request):
    render(request, 'espn/link_download_laporan.html',{})
