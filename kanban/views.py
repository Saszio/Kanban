from django.shortcuts import render
from .models import Dane
from django.http import HttpResponse


def send(request):
    todos = Dane.objects.all().filter(status = 1)
    doings = Dane.objects.all().filter(status = 2)
    testings = Dane.objects.all().filter(status = 3)
    dones = Dane.objects.all().filter(status = 4)
    #Funkcja render, generuje z pliku stronę i pokazuję ją na przeglądarce, dalej tworzymy słwonik by odnosić się do elementów z bazy danych na stronie 
    rend = render(request, 'index.html', {'todos': todos,'doings':doings,'testings':testings,'dones':dones})
    return rend

#Funkcja robiąca update statusu w bazie danych kiedy przesuwamy zadanie między kolumnami
def sort(request):
    if request.method == "POST":
        send_id = request.POST.get('send_id')
        end = request.POST.get('end')
        Dane.objects.filter(nazwa = send_id). update(
            status = int(end)
        )
    #Funkcje działają poprawie, ale by jednak przeglądarka nie pokazywała błędu musi posiadać jakikolwiek 'return', w tym przypadku jest on pusty
    return HttpResponse('')

#Funkcja dodawająca dane z okienka do bazy danych
def add(request):
    if request.method == 'POST':
        nazwa = request.POST['nazwa']
        opis = request.POST['opis']
        status = request.POST['status']
        Dane.objects.create(
            nazwa = nazwa,
            opis = opis,
            status = status,
        )
    return HttpResponse('')

#Funkcja usuwająca z bazy element
def delete(request):
    if request.method == 'POST':
        elem_id = request.POST.get('elem_id')
        Dane.objects.filter(nazwa = elem_id).delete()
    return HttpResponse('')  
    