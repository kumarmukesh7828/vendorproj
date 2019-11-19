from django.shortcuts import render, redirect
from .models import Vendor, VendorAddress
from .form import VendorForm, VendorAddrForm
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory


# Create your views here.
def vendor_create(request):
    form = VendorForm(request.POST or None)
    addrform = VendorAddrForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid() and addrform.is_valid():
            try:
                with transaction.atomic():
                    insured = form.save(commit=False)
                    insured.save()
                    data = addrform.save(commit=False)
                    data.vendor_id = insured
                    data.save()
            except IntegrityError:
                print("Error Encountere d",IntegrityError.__name__)
    form = VendorForm()
    addrform = VendorAddrForm()
    context = {
        'form': form,
        'addrform': addrform
    }
    return render(request, 'vendor.html', context)


def vendor_list(request):
    vendor = Vendor.objects.all()
    vaddr = VendorAddress.objects.all()
    return render(request, 'vendor_list.html', {'vendor': vendor})

def delete_view(request, id):
    vendor = Vendor.objects.get(id=id)
    vendor.delete()
    return redirect('vendor:vendor_list')


def address_view(request):
    vaddr = VendorAddress.objects.get(id=id)
    return render(request, 'vendor_address.html', {'vaddr': vaddr})
