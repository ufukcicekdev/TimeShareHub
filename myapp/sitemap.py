from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

startdate = datetime.today()
enddate = startdate + relativedelta(years=10)

class MainLinkSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        # Sadece ana URL'yi ekleyin
        return ['timesharehub.online']