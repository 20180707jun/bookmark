from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.list import ListView

from . models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')