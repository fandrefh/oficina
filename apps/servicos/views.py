from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ServicoForm, OrdemServicoForm, RelatorioForm

from .models import Servico, OrdemServico
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


@login_required
def criar_ordem_servico(request):
    template_name = 'servicos/criar_ordem_servico.html'
    context = {}
    oficina = get_object_or_404(Oficina, usuario=request.user)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            osf = form.save(commit=False)
            osf.oficina = oficina
            osf.save()
            form.save_m2m()
            messages.success(request, 'Ordem de Serviço criada com sucesso.')
            return redirect('servicos:lista_ordem_servico')
    form = OrdemServicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_ordem_servico(request):
    template_name = 'servicos/lista_ordem_servico.html'
    oficina = get_object_or_404(Oficina, usuario=request.user)
    ordens_servicos = OrdemServico.objects.filter(oficina=oficina)
    context = {
        'ordens_servicos': ordens_servicos,
    }
    return render(request, template_name, context)


@login_required
def editar_ordem_servico(request, pk):
    template_name = 'servicos/criar_ordem_servico.html'
    context = {}
    ordem_servico = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(data=request.POST, instance=ordem_servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de Serviço alterada com sucesso.')
            return redirect('servicos:lista_ordem_servico')
    form = OrdemServicoForm(instance=ordem_servico)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def gerar_relatorio(request):
    template_name = 'servicos/gerar_relatorio.html'
    mecanico = request.GET.get('mecanico')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    # SQL Equivalente: select * from ordem_servico where data_entrada = data_inicial and data_entrega <= data_final and mecanico = mecanico
    ordens_servicos = OrdemServico.objects.filter(
        data_entrada__gte=data_inicial,
          data_entrega__lte=data_final,
            mecanico=mecanico, status=2)
    form = RelatorioForm()
    context = {
        'form': form,
        'ordens_servicos': ordens_servicos
    }
    return render(request, template_name, context)
