from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)


class HomePage(TemplateView):
    template_name = 'index.html'
