from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse


PUBLIC_SERVICE_SLUGS = (
    'contracts',
    'planning',
    'interiors',
    'interior-design',
    'exterior-designs',
    'agriculture',
    'visualizations',
)


def robots_txt(request):
    """Tell search engines what they may crawl and where to find the sitemap."""
    sitemap_url = f'{settings.SITE_URL}{reverse("sitemap")}'
    content = '\n'.join(
        (
            'User-agent: *',
            'Allow: /',
            'Disallow: /admin/',
            f'Sitemap: {sitemap_url}',
            '',
        )
    )
    return HttpResponse(content, content_type='text/plain; charset=utf-8')


def sitemap_xml(request):
    """Return an XML sitemap containing all public, indexable pages."""
    urls = [f'{settings.SITE_URL}{reverse("home")}']
    urls.extend(
        f'{settings.SITE_URL}{reverse("service_detail", kwargs={"slug": slug})}'
        for slug in PUBLIC_SERVICE_SLUGS
    )
    url_entries = ''.join(f'<url><loc>{url}</loc></url>' for url in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'{url_entries}'
        '</urlset>'
    )
    return HttpResponse(xml, content_type='application/xml; charset=utf-8')
