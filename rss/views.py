from django.shortcuts import render

# Create your views here.
from django.views import View
from django.db.models.functions import Coalesce
import bs4
from datetime import datetime

from .models import Item

class RSS(View):
    def get(self, request):
        xml = bs4.BeautifulSoup(open("rss/habr.xml", encoding="utf-8").read(), 'xml')
        for item in xml.find_all('item'):
            #from rss.models import Item
            title = str(item.title.string)
            link = str(item.guid.string)
            desc = str(item.description.string)
            date = str(item.pubDate.string)
            #print("1)", title)
            #print("2)", link)
            #print("3)", desc)
            #print("4)", datetime.strptime(date, '%a, %d %b %Y %X GMT'))
            #print("\n\n\n")

            #i = Item.create(title, link, desc, datetime.strptime(date, '%a, %d %b %Y %X GMT'))
            #i.save();
        items = Item.objects.all().order_by('-date')
        for item in items:
            print(item.date)
        print(len(items))

        return render(request, 'rss.html')

    def post(self):
        return
