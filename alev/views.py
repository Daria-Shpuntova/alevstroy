from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, FormView
from .models import CallMe, Repair, Other, Image
from .forms import CallForm
from django.urls import reverse, reverse_lazy
from alevstroy.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError



class HomePage(ListView, FormMixin):
    model = Repair
    template_name = 'alev/home.html'
    context_object_name = 'rem'
    form_class = CallForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name_form')
            self.tel = form.cleaned_data.get('tel_form')
            self.text = form.cleaned_data.get('text_form')
            try:
                send_mail(f'Запрос',f'{self.name} телефон {self.tel} self.text',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.tel = self.tel
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'
        return context


class Rem(DetailView, FormMixin):
    model = Repair
    template_name = 'alev/rem.html'
    context_object_name = 'rem'
    form_class = CallForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name_form')
            self.tel = form.cleaned_data.get('tel_form')
            self.text = form.cleaned_data.get('text_form')
            try:
                send_mail(f'Запрос',f'{self.name} телефон {self.tel}  self.text',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.tel = self.tel
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Rem, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'
        return context



class Other(FormMixin, DetailView):
    model = Other
    template_name = 'alev/other.html'
    form_class = CallForm
    context_object_name = 'other'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name_form')
            self.tel = form.cleaned_data.get('tel_form')
            self.text = form.cleaned_data.get('text_form')
            try:
                send_mail(f'Запрос',f'{self.name} телефон {self.tel} self.text',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.tel = self.tel
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Other, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'
        return context


class Image(ListView, FormMixin):
    model = Image
    template_name = 'alev/gallary.html'
    context_object_name = 'image'
    form_class = CallForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name_form')
            self.tel = form.cleaned_data.get('tel_form')
            self.text = form.cleaned_data.get('text_form')
            try:
                send_mail(f'Запрос', f'{self.name} телефон {self.tel} self.text',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.tel = self.tel
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Image, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'
        return context


class About(FormView):
    template_name = "alev/about.html"
    form_class = CallForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.name = form.cleaned_data.get('name_form')
            self.tel = form.cleaned_data.get('tel_form')
            self.text = form.cleaned_data.get('text_form')
            try:
                send_mail(f'Запрос', f'{self.name} телефон {self.tel} self.text',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.name
        self.object.tel = self.tel
        self.object.text = self.text
        self.object.save()
        return super().form_valid(form)

 #   def form_valid(self, form):
 #       self.object = form.save(commit=False)
 #       self.object.name = form.cleaned_data.get('name_form')
 #       self.object.tel = form.cleaned_data.get('tel_form')
 #       self.object.text = form.cleaned_data.get('text_form')
 #       self.object.save()
 #       return super().form_valid(form)

#def about(request):
#    print(44)
#    if request.method == "POST":
#        call_me = CallMe
#        form = CallForm(request.POST, instance=call_me)
##        print(form, 'form')
##        print(form.cleaned_data.get('name_form'), "form.cleaned_data.get('name_form')")
#
#        if form.is_valid():
#            call = form.save(commit=False)
#            call.name_form = call.cleaned_data.get('name_form')
#
#            print(call, 'call')
#            print(call.cleaned_data.get('name_form'), "call.cleaned_data.get('name_form')")
#            call.tel_form = call.cleaned_data.get('tel_form')
#            print(call.cleaned_data.get('tel_form'), "call.cleaned_data.get('tel_form')")
#            call.text_form = call.cleaned_data.get('text_form')
#            print(call.cleaned_data.get('text_form'), "call.cleaned_data.get('text_form')")
#            call.save()
#            print(call.name_form)
#            print(call)
#            return redirect('home')
#    else:
#        form = CallForm()
#    return render(request, 'alev/about.html', {'form': form})