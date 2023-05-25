from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView
)
from client_relationship_manager.forms import CreateClientForm

from client_relationship_manager.models import Client
# Create your views here.
class HomeView(ListView):
    template_name = "index.html"

class SearchResultView(ListView):
    template_name = "search_results.html" 

    def get_queryset(self) :

        query = self.request.GET.get("q")

        if query:
            results = Client.objects.filter(
                Q(name__icontains=query)
                | Q(pk__icontains=query)
                | Q(phone__icontains=query)
                | Q(address__icontains=query)
                | Q(email__icontains=query)
            )

        return results

class CreateClientView(CreateView):
    template_name ="create_client.html" 
    form_class = CreateClientForm

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Created")
        return reverse_lazy("")

class DetailClientView(DetailView):
    template_name = "detail_client.html"

class UpdateClientView(UpdateView):
    template_name = "update_client.html"
    form_class = "UpdatClientForm" 

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Updated")
        return reverse_lazy("crm:detail_client")


class DeleteClientView(DeleteView):
    template_name = "delete_client.html" 

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Deleted.")
        return reverse_lazy("crm:index")