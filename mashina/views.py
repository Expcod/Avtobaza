from django.http import JsonResponse
from django.views import View
from .models import Haydovchi
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Haydovchi
import re


class HomePage(View):
    def get(self, request):
        pattern = r"^[A-Za-z]+ [A-Za-z]+ \(\d+\)$"
        query = self.request.GET.get("query")
            
        if query:
            context = {
                'query' : query
            }
            if bool(re.match(pattern, query)):
                ism, familya, jsh = query.split()
                haydovchi = Haydovchi.objects.get(jshshir=jsh[1:-1])
                context['haydovchi'] = haydovchi
            else:
                haydovchilar = Haydovchi.objects.filter(
                Q(ism__icontains=query) |
                Q(familiya__icontains=query) |
                Q(jshshir__icontains=query))
                context["haydovchilar"] = haydovchilar
            return render(request, 'index.html', context)
        return render(request, 'index.html')



def haydovchi_qidirish(request):
    query = request.GET.get('q')
    if not query:
        return JsonResponse({'error': 'Qidiruv so\'rovi kiritilmadi'}, status=400)
    ism, familya, jshshir = query.split()
    haydovchi = Haydovchi.objects.filter(
        Q(ism__icontains=ism) |
        Q(familiya__icontains=familya) |
        Q(jshshir__icontains=jshshir[1:-1])
    ).first()

    if not haydovchi:
        return JsonResponse({'error': 'Haydovchi topilmadi'}, status=404)

    mashinalar = haydovchi.mashinalar.all()
    mashina_data = [
        {
            'raqam': mashina.raqam,
            'nomi': mashina.nomi,
            'rangi': mashina.rangi,
            'ishlab_chiqarilgan_yili': mashina.ishlab_chiqarilgan_yili,
        } for mashina in mashinalar
    ]

    # Keyingi URLga o'tish va ro'yxatlarni yuborish
    # 'result_page' URL nomini mos ravishda o'zgartiring
    return redirect(reverse('result_page', kwargs={'haydovchi_id': haydovchi.id}))

def get_suggestions(request):
    query = request.GET.get('q', '')  # Get the search query
    if not query:
        return JsonResponse([], safe=False)  # Return an empty list if no query

    # Search drivers based on the query
    suggestions = Haydovchi.objects.filter(
        Q(ism__icontains=query) | Q(familiya__icontains=query)
    ).values_list('ism', 'familiya', 'jshshir')[:10]  # Limit to 10 suggestions

    suggestion_list = [f"{ism} {familiya} ({jshshir})" for ism, familiya, jshshir in suggestions]

    return JsonResponse(suggestion_list, safe=False)

def result_page(request, haydovchi_id):
    haydovchi = get_object_or_404(Haydovchi, id=haydovchi_id)
    mashinalar = haydovchi.mashinalar.all()
    mashina_data = [
        {
            'raqam': mashina.raqam,
            'nomi': mashina.nomi,
            'rangi': mashina.rangi,
            'ishlab_chiqarilgan_yili': mashina.ishlab_chiqarilgan_yili,
        } for mashina in mashinalar
    ]
    return render(request, 'result_page.html', {'haydovchi': haydovchi, 'mashinalar': mashina_data})
