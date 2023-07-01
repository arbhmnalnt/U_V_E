from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.utils import timezone

class rentOrderCreatView(LoginRequiredMixin, CreateView):
    models          = Order
    template_name   = 'play/rent_order_create.html'
    form_class      = OrderForm

    def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)
            
    def get_success_url(self):
        rent = self.object.rent
        return reverse_lazy('play:rent_order_list', kwargs={'pk': rent.id})

class rentOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'play/rent_order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Order.objects.filter(rent__pk=pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        rentId = self.kwargs.get('pk')
        device = Rent.objects.get(pk=rentId).device
        context['device'] = device
        orders = Order.objects.filter(rent__pk=rentId)
        total_price = sum(order.price for order in orders)
        context['total_price'] = total_price
        return context
    

class rentUpdateView(LoginRequiredMixin, UpdateView):
    model           = Rent
    form_class      = RentForm
    success_url     = reverse_lazy('play:rent_list')
    template_name   =  'play/rent_create_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class rentCreateView(LoginRequiredMixin, CreateView):
    model = Rent
    form_class = RentForm
    success_url = reverse_lazy('play:rent_list')
    template_name = 'play/rent_create_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class rentListView(LoginRequiredMixin, ListView):   
    model = Rent
    template_name = 'play/rent_list.html'
    context_object_name = 'rents'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False).order_by(F('created_at').desc())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        devices = Device.objects.all()
        context['devices'] = devices
        current_time = timezone.now()
        context['current_time'] = current_time
        return context

