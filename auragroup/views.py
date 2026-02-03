from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import (
    OurTeam, ContactUs, Services, ServicesDetails,
    Portfolio, Career, CareerApplication
)
from .forms import ContactForm, ServicesDetailsForm, CareerApplicationForm
from .bot import send_message, send_service_request, send_vocation


class IndexView(TemplateView):
    """Bosh sahifa"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = OurTeam.objects.all()[:4]
        context['services'] = Services.objects.all()[:6]
        context['portfolios'] = Portfolio.objects.all()[:6]
        context['page_title'] = _("Bosh sahifa")
        return context


class ServicesView(ListView):
    """Xizmatlar sahifasi"""
    model = Services
    template_name = 'services.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _("Xizmatlar")
        return context


class PortfolioView(ListView):
    """Portfolio sahifasi"""
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Services.objects.all()
        context['page_title'] = _("Portfolio")
        return context


class PortfolioDetailsView(DetailView):
    """Portfolio tafsilotlari sahifasi"""
    model = Portfolio
    template_name = 'portfolio_detail.html'
    context_object_name = 'portfolio'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save(update_fields=['view_count'])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.name
        return context


class AboutView(ListView):
    """Biz haqimizda sahifasi"""
    model = OurTeam
    template_name = 'about.html'
    context_object_name = 'team_members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _("Biz haqimizda")
        return context


class CareerView(ListView):
    """Karyera sahifasi"""
    model = Career
    template_name = 'career.html'
    context_object_name = 'careers'
    paginate_by = 6

    def get_queryset(self):
        return Career.objects.filter(is_active=True).order_by('-posted_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _("Karyera")
        return context


def contact_view(request):
    """Aloqa sahifasi"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            
            # Telegram'ga xabar yuborish
            send_message(
                name=instance.full_name,
                email=instance.email,
                phone_number=instance.phone_number,
                description=instance.message
            )
            
            messages.success(request, _("Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."))
            return redirect('contact')
        else:
            messages.error(request, _("Iltimos, formani to'g'ri to'ldiring."))
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': _("Bog'lanish"),
    }
    return render(request, 'contact.html', context)


def service_request_view(request, pk):
    """Xizmat so'rovi sahifasi"""
    service = get_object_or_404(Services, pk=pk)

    if request.method == "POST":
        form = ServicesDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.service_type = service
            instance.save()
            
            # Fayl yo'lini olish
            file_path = None
            if instance.file:
                file_path = instance.file.path
            
            # Telegram'ga xabar va fayl yuborish
            send_service_request(
                company=instance.company_name,
                phone=str(instance.phone_number),
                service=service.name,
                contact_name=instance.contact_name,
                description=instance.description,
                telegram=instance.telegram or "",
                email=instance.email or "",
                file_path=file_path
            )
            
            messages.success(request, _("So'rovingiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."))
            return redirect('index')
        else:
            messages.error(request, _("Iltimos, formani to'g'ri to'ldiring."))
    else:
        form = ServicesDetailsForm()

    context = {
        'form': form,
        'service': service,
        'page_title': _("Xizmat so'rovi"),
    }
    return render(request, 'service_request.html', context)


def career_detail_view(request, pk):
    """Vakansiya tafsilotlari va ariza topshirish sahifasi"""
    career = get_object_or_404(Career, pk=pk)

    if request.method == "POST":
        form = CareerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.career = career
            instance.save()
            
            # Resume fayl yo'lini olish
            resume_path = None
            if instance.file:
                resume_path = instance.file.path
            
            # Telegram'ga xabar va resume yuborish
            send_vocation(
                {
                    'Vakansiya': career.position,
                    'Ism': instance.full_name,
                    'Telefon': instance.phone_number,
                    'Telegram': instance.telegram,
                    'Xabar': instance.message,
                },
                resume_path=resume_path
            )
            
            messages.success(request, _("Arizangiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."))
            return redirect('career')
        else:
            messages.error(request, _("Iltimos, formani to'g'ri to'ldiring."))
    else:
        form = CareerApplicationForm()

    context = {
        'form': form,
        'career': career,
        'page_title': career.position,
    }
    return render(request, 'career_detail.html', context)


def like_project_view(request, pk):
    """Portfolio loyihasini yoqtirish"""
    project = get_object_or_404(Portfolio, pk=pk)
    session_key = f'liked_project_{pk}'

    liked = request.session.get(session_key, False)

    if not liked:
        project.like_count += 1
        request.session[session_key] = True
        liked = True
        message = _("Loyihaga yoqdi deb belgiladingiz!")
    else:
        project.like_count = max(0, project.like_count - 1)
        request.session[session_key] = False
        liked = False
        message = _("Yoqdi belgisini olib tashladingiz!")

    project.save(update_fields=['like_count'])

    return JsonResponse({
        'like_count': project.like_count,
        'liked': liked,
        'message': str(message)
    })

