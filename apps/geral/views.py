from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import OficinaForm, MecanicoForm
from .models import Oficina, Mecanico


@login_required
def home(request):
    template_name = 'geral/home.html'
    context = {}
    return render(request, template_name, context)


@login_required
def nova_oficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.success(request, 'Oficina cadastrada com sucesso.')
            return redirect('geral:lista_oficina')
        else:
            messagem_erro = list(form.errors.values())[0][0]
            messages.error(request, f'{messagem_erro}')
            return redirect('geral:lista_oficina')
    form = OficinaForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user) # select * from oficina where usuario = usuario_da_sessao;
    context = {
        'oficinas': oficinas,
    }
    return render(request, template_name, context)


@login_required
def excluir_oficina(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk) # SQL Equivalente: select * from oficina where id = pk;
    oficina.delete() # SQL Equivalente: delete from oficina where id = pk;
    messages.info(request, 'Oficina excluída com sucesso.')
    return redirect('geral:lista_oficina')


@login_required
def editar_oficina(request, pk):
    template_name = 'geral/nova_oficina.html'
    context = {}
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina) # SQL Equivalente: update table oficina set nome = ''...
        form.save()
        messages.success(request, 'Oficina atualizada com sucesso.')
        return redirect('geral:lista_oficina')
    form = OficinaForm(instance=oficina)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def novo_mecanico(request):
    template_name = 'geral/novo_mecanico.html'
    context = {}
    oficina = get_object_or_404(Oficina, usuario=request.user)
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            mf = form.save(commit=False)
            mf.oficina = oficina
            mf.save()
            messages.success(request, 'Mecânico cadastrado com sucesso.')
            return redirect('geral:lista_mecanico')
    form = MecanicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_mecanico(request):
    template_name = 'geral/lista_mecanico.html'
    oficina = get_object_or_404(Oficina, usuario=request.user)
    mecanicos = Mecanico.objects.filter(oficina=oficina)
    context = {
        'mecanicos': mecanicos
    }
    return render(request, template_name, context)
