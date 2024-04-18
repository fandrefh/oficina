from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ServicoForm

from .models import Servico
from geral.models import Oficina


@login_required
def lista_servicos(request):
    template_name = 'servicos/lista_servicos.html'
    oficina = get_object_or_404(Oficina, usuario=request.user)
    servicos = Servico.objects.filter(oficina=oficina)
    context = {
        'servicos': servicos,
    }
    return render(request, template_name, context)



@login_required
def novo_servico(request):
    template_name = 'servicos/novo_servico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        oficina = get_object_or_404(Oficina, usuario=request.user)
        if form.is_valid():
            sf = form.save(commit=False)
            sf.oficina = oficina
            sf.save()
            messages.success(request, 'Serviço adicionado com sucesso.')
            return redirect('servicos:lista_servicos')
    form = ServicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def atualizar_servico(request, pk):
    template_name = 'servicos/novo_servico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(data=request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso.')
            return redirect('servicos:lista_servicos')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)
