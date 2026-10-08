from django.http import Http404
from django.shortcuts import render


SERVICE_TEMPLATE_MAP = {
    'contracts': 'sites/service_contracts.html',
    'planning': 'sites/service_planning.html',
    'interiors': 'sites/service_interiors.html',
    'interior-design': 'sites/service_interior_design.html',
    'exterior-designs': 'sites/service_exterior_designs.html',
    'agriculture': 'sites/service_agriculture.html',
    'visualizations': 'sites/service_visualizations.html',
}


def home(request):
    return render(request, 'sites/index.html')


def service_detail(request, slug):
    template_name = SERVICE_TEMPLATE_MAP.get(slug)
    if not template_name:
        raise Http404('Service not found')
    return render(request, template_name, {'slug': slug})
