from typing import Any, Dict
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = Client.objects.all()
        return queryset

class SearchResultView(ListView):
    template_name = "search_results.html" 
    context_object_name = "results"

    def get_queryset(self) :

        query = self.request.GET.get("q") or None

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

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Client.objects.all()
        return queryset

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
