from django.http import HttpResponse


def index(request):
    name = request.GET.get('name', 'world')
    return HttpResponse(f"Hello, {name}. You're at the polls")
