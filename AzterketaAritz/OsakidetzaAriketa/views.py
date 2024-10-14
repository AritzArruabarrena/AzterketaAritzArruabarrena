from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def zitak_list(request):
    ZitakZerrenda=Zitak.objects.all()
    return render(request, 'firstApp/kudeatu/zitak/zitak_list.html', {'zitak':ZitakZerrenda})

def zitak_new(request):
    if request.method == 'POST':
        form=ZitakForm(request.POST)
        if form.is_valid:
            zitak = form.save()
            zitak.save()
        return redirect('zitak_list')

    else:
        form=ZitakForm()
        return render(request, 'firstApp/kudeatu/zitak/zitakform.html', {'form':form})
    
def zitak_ezabatu(request, id):
    zitak = Zitak.objects.filter(id=id) 
    
    zitak.delete()  
    return redirect('zitak_list')

def medikuak(request):
    return render(request, 'firstApp/kudeatu/medikuak/medikuak.html')


def medikuak_list(request):
    MedikuZerrenda=Medikua.objects.all()
    return render(request, 'firstApp/kudeatu/medikuak/medikuak_list.html', {'medikua':MedikuZerrenda})

def mediko_new(request):
    if request.method == 'POST':
        form=MedikoForm(request.POST)
        if form.is_valid:
            medikoa = form.save()
            medikoa.save()
        return redirect('zitak_list')

    else:
        form=MedikoForm()
        return render(request, 'firstApp/kudeatu/medikuak/medikoakform.html', {'form':form})
    

def mediko_delete(request):
    if request.method == 'POST':
        uid = request.POST.get("uid", "")
        Medikua.objects.filter(id=uid).delete()
        return redirect('zitak_list')
    
    else:
        MedikuaZerrenda=Medikua.objects.all()
        return render(request, 'firstApp/kudeatu/medikuak/delete_medikua.html',{'medikua':MedikuaZerrenda})
    
def medikua_editatu(request,medikua_id):
    medikuak = Medikua.objects.filter(id=medikua_id)
    
    medikuaEditatu = medikuak.first()
    
    if request.method == 'POST':
        form = MedikuaEditatuForm(request.POST, instance=medikuaEditatu)
        if form.is_valid():
            form.save()
            return redirect('zitak_list')  
    else:
        form = MedikuaEditatuForm(instance=medikuaEditatu)

    return render(request, 'firstApp/kudeatu/medikuak/medikoakform.html', {'form': form})

    
def pazienteak(request):
    return render(request, 'firstApp/kudeatu/pazienteak/pazienteak.html')

def pazienteak_list(request):
    PazienteZerrenda=Paziente.objects.all()
    return render(request, 'firstApp/kudeatu/pazienteak/pazienteak_list.html', {'paziente':PazienteZerrenda})

def paziente_new(request):
    if request.method == 'POST':
        form=PazienteForm(request.POST)
        if form.is_valid:
            paziente = form.save()
            paziente.save()
        return redirect('zitak_list')

    else:
        form=PazienteForm()
        return render(request, 'firstApp/kudeatu/pazienteak/pazienteakform.html', {'form':form})
    

def paziente_delete(request):
    if request.method == 'POST':
        uid = request.POST.get("uid", "")
        Paziente.objects.filter(id=uid).delete()
        return redirect('zitak_list')
    
    else:
        PazeinteZerrenda=Paziente.objects.all()
        return render(request, 'firstApp/kudeatu/pazienteak/delete_paziente.html',{'paziente':PazeinteZerrenda})
    

def pazientea_editatu(request,paziente_id):
    pazienteak = Paziente.objects.filter(id=paziente_id)
    
    pazienteaEditatu = pazienteak.first()
    

    
    if request.method == 'POST':
        form = PazienteEditatuForm(request.POST, instance=pazienteaEditatu)
        if form.is_valid():
            form.save()
            return redirect('zitak_list')  
    else:
        form = PazienteEditatuForm(instance=pazienteaEditatu)

    return render(request, 'firstApp/kudeatu/pazienteak/pazienteakform.html', {'form': form})