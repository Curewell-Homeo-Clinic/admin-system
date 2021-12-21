from patients.models import Invoice, Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from patients.views import LOGIN_URL, CACHE_TTL


def get_invoice(patient_name=None):
    if patient_name:
        patient = Patient.objects.filter(first_name__icontains=patient_name)
        invoices = Invoice.objects.filter(patient__in=patient).order_by('-id')
    else:
        invoices = Invoice.objects.all().order_by('-id')

    return invoices


@login_required(login_url=LOGIN_URL)
def invoice_list(request):
    filter_by_patient_name = request.GET.get('patient_name')
    if cache.get(f'invoice_{filter_by_patient_name}'):
        return cache.get(f'invoice_{filter_by_patient_name}')
    else:
        if filter_by_patient_name:
            invoices = get_invoice(patient_name=filter_by_patient_name)
            cache.set(f'invoice_{filter_by_patient_name}', invoices, CACHE_TTL)
        else:
            invoices = get_invoice()

    context = {'invoices': invoices, 'active': 'invoice'}
    return render(request, 'invoices/invoice_list.html', context)


@login_required(login_url=LOGIN_URL)
def invoice_detail(request, pk):
    if cache.get(f'invoice{pk}'):
        invoice = cache.get(f'invoice{pk}')
    else:
        invoice = Invoice.objects.get(pk=pk)
        cache.set(f'invoice{pk}', invoice)

    context = {
        'invoice': invoice,
        'invoice_edit': f'/admin/patients/invoice/{invoice.id}/change',
        'active': 'invoice'
    }

    return render(request, 'invoices/invoice_detail.html', context)


@login_required(login_url=LOGIN_URL)
def invoice_print(request, pk):
    if cache.get(f'invoice{pk}'):
        invoice = cache.get(f'invoice{pk}')
    else:
        invoice = Invoice.objects.get(pk=pk)
        cache.set(f'invoice{pk}', invoice)

    context = {'invoice': invoice, 'blank_row': range(6)}

    return render(request, 'invoices/print.html', context)
