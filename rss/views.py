from django.shortcuts import render

# Create your views here.
from django.views import View
from django.db.utils import IntegrityError
import urllib3
import bs4
from datetime import datetime

from .models import Item


class RSS(View):
    def get(self, request):

        page = urllib3.PoolManager().request("GET", "https://habr.com/rss/interesting/")
        xml = bs4.BeautifulSoup(page.data, 'xml')
        for item in xml.find_all('item'):
            try:
                title = str(item.title.string)
                link = str(item.guid.string)
                desc = str(item.description.string)
                date = str(item.pubDate.string)
                i, created = Item.objects.get_or_create(
                    header=title,
                    link=link,
                    description=desc,
                    date=datetime.strptime(date, '%a, %d %b %Y %X GMT')

                )
                if created:
                    i.save()
            except IntegrityError:
                print("Ой, ну бывает")
                print([title, link, desc, date])

        items = Item.objects.all().order_by('-date')
        s = ""
        context = {}
        for i in range(10):
            item = items[i]
            context["header" + str(i)] = str(item.header)
            context["link" + str(i)] = str(item.link)
            context["date" + str(i)] = str(item.date)
        return render(request, 'rss.html', context)

    def post(self):
        return
