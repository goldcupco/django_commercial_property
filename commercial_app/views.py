# commercial_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .models import CommercialProperty
from .forms import CommercialPropertyForm

class PropertyListView(View):
    template_name = 'commercial_app/property_list.html'

    def get(self, request):
        properties = CommercialProperty.objects.all()
        return render(request, self.template_name, {'properties': properties})

class PropertyDetailView(View):
    template_name = 'commercial_app/property_detail.html'

    def get(self, request, pk):
        property = get_object_or_404(CommercialProperty, pk=pk)
        return render(request, self.template_name, {'property': property})

class PropertyCreateView(View):
    template_name = 'commercial_app/property_form.html'

    def get(self, request):
        form = CommercialPropertyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CommercialPropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property-list')
        return render(request, self.template_name, {'form': form})

class PropertyUpdateView(View):
    template_name = 'commercial_app/property_form.html'

    def get(self, request, pk):
        property = get_object_or_404(CommercialProperty, pk=pk)
        form = CommercialPropertyForm(instance=property)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        property = get_object_or_404(CommercialProperty, pk=pk)
        form = CommercialPropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property-list')
        return render(request, self.template_name, {'form': form})

class PropertyDeleteView(View):
    template_name = 'commercial_app/property_confirm_delete.html'

    def get(self, request, pk):
        property = get_object_or_404(CommercialProperty, pk=pk)
        return render(request, self.template_name, {'property': property})

    def post(self, request, pk):
        property = get_object_or_404(CommercialProperty, pk=pk)
        property.delete()
        return redirect('property-list')
