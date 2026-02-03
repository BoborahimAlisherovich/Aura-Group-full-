from modeltranslation.translator import translator, TranslationOptions
from .models import OurTeam, Services, Portfolio, Career


class OurTeamTranslationOptions(TranslationOptions):
    """Jamoa a'zolari uchun tarjima maydonlari"""
    fields = ('name', 'position', 'skills', 'description', 'story')


class ServicesTranslationOptions(TranslationOptions):
    """Xizmatlar uchun tarjima maydonlari"""
    fields = ('description',)


class PortfolioTranslationOptions(TranslationOptions):
    """Portfolio uchun tarjima maydonlari"""
    fields = ('name', 'description', 'full_description', 'features')


class CareerTranslationOptions(TranslationOptions):
    """Vakansiyalar uchun tarjima maydonlari"""
    fields = ('position', 'location', 'description', 'requirements', 'experience_level')


# Modellarni ro'yxatdan o'tkazish
translator.register(OurTeam, OurTeamTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(Portfolio, PortfolioTranslationOptions)
translator.register(Career, CareerTranslationOptions)
