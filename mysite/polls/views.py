import asyncio

from django.http import HttpResponse
from django.views import View


def index(request):
    name = request.GET.get('name', 'world')
    return HttpResponse(f"Hello, {name}. You're at the polls")


class IndexView(View):
    async def get(self, request):
        name = request.GET.get('name', 'world')
        await asyncio.sleep(1)
        return HttpResponse(f"Hello, {name}. You're at the class-based polls")
