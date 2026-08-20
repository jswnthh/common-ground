from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import ServiceCategory


class StaticSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return [
            ("index", 1.0),
            ("counsellors", 0.9),
            ("book", 0.6),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ServiceCategory.objects.all()

    def location(self, obj):
        return reverse("service_detail", kwargs={"slug": obj.slug})


SITEMAPS = {
    "static": StaticSitemap,
    "services": ServiceSitemap,
}
