import pyvisa
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def connect(request):
    rm = pyvisa.ResourceManager()
    instr = rm.open_resource('USB0::0x1313::0x804F::M00295819::INSTR')
    request.session['instr'] = instr
    return JsonResponse({'status': 'success'})

def set_current(request):
    instr = request.session.get('instr')
    current = float(request.GET.get('current'))
    instr.write(f'source1:current:level:amplitude {current}')
    new_current = instr.query('source1:current:level:amplitude?')
    return JsonResponse({'new_current': new_current})
