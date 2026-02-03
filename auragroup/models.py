from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class OurTeam(models.Model):
    """Bizning jamoa a'zolari"""
    name = models.CharField(_("Ism"), max_length=100)
    image = models.ImageField(_("Rasm"), upload_to='images/team/')
    position = models.CharField(_("Lavozim"), max_length=100)
    experience_years = models.PositiveIntegerField(_("Tajriba (yil)"), default=1)
    skills = models.CharField(_("Ko'nikmalar"), max_length=300, blank=True, help_text="Vergul bilan ajrating")
    description = models.TextField(_("Tavsif"))
    story = models.TextField(_("Hikoya"), blank=True, null=True)
    telegram = models.CharField(_("Telegram"), max_length=50, blank=True, null=True)
    linkedin = models.URLField(_("LinkedIn"), blank=True, null=True)
    github = models.URLField(_("GitHub"), blank=True, null=True)
    order = models.PositiveIntegerField(_("Tartib"), default=0)

    class Meta:
        verbose_name = _("Jamoa a'zosi")
        verbose_name_plural = _("Jamoa a'zolari")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
    
    def get_skills_list(self):
        """Ko'nikmalarni ro'yxat sifatida qaytaradi"""
        if self.skills:
            return [s.strip() for s in self.skills.split(',')]
        return []


class ContactUs(models.Model):
    """Aloqa so'rovlari"""
    full_name = models.CharField(_("To'liq ism"), max_length=100)
    phone_number = models.CharField(_("Telefon raqam"), max_length=20)
    email = models.EmailField(_("Email"))
    message = models.TextField(_("Xabar"))
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)

    class Meta:
        verbose_name = _("Aloqa so'rovi")
        verbose_name_plural = _("Aloqa so'rovlari")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%d.%m.%Y')}"


class Services(models.Model):
    """Xizmatlar"""
    
    SERVICE_CHOICES = [
        ('web', _("Web sayt")),
        ('mobile', _("Mobil ilova")),
        ('telegram', _("Telegram bot")),
        ('ai', _("AI / Sun'iy intellekt")),
        ('crm', _("CRM tizimi")),
        ('ecommerce', _("E-commerce")),
        ('desktop', _("Desktop dastur")),
        ('cloud', _("Cloud xizmatlari")),
        ('security', _("Kiberxavfsizlik")),
        ('analytics', _("Ma'lumotlar tahlili")),
        ('blockchain', _("Blockchain")),
        ('iot', _("IoT")),
        ('design', _("UX/UI Dizayn")),
        ('devops', _("DevOps")),
        ('api', _("API integratsiya")),
    ]
    
    # Har bir xizmat turi uchun default iconlar
    SERVICE_ICONS = {
        'web': 'fas fa-globe',
        'mobile': 'fas fa-mobile-alt',
        'telegram': 'fab fa-telegram',
        'ai': 'fas fa-brain',
        'crm': 'fas fa-users-cog',
        'ecommerce': 'fas fa-shopping-cart',
        'desktop': 'fas fa-desktop',
        'cloud': 'fas fa-cloud',
        'security': 'fas fa-shield-alt',
        'analytics': 'fas fa-chart-line',
        'blockchain': 'fas fa-link',
        'iot': 'fas fa-microchip',
        'design': 'fas fa-palette',
        'devops': 'fas fa-server',
        'api': 'fas fa-plug',
    }
    
    name = models.CharField(_("Xizmat turi"), max_length=50, choices=SERVICE_CHOICES, unique=True)
    image = models.ImageField(_("Rasm"), upload_to='images/services/', blank=True, null=True)
    description = models.TextField(_("Tavsif"))
    icon = models.CharField(_("Ikon klassi"), max_length=100, blank=True, help_text="Bo'sh qoldirsangiz avtomatik tanlanadi")
    order = models.PositiveIntegerField(_("Tartib"), default=0)
    is_active = models.BooleanField(_("Faol"), default=True)

    class Meta:
        verbose_name = _("Xizmat")
        verbose_name_plural = _("Xizmatlar")
        ordering = ['order', 'name']

    def __str__(self):
        return self.get_name_display()
    
    def save(self, *args, **kwargs):
        # Agar icon bo'sh bo'lsa, avtomatik icon qo'yish
        if not self.icon:
            self.icon = self.SERVICE_ICONS.get(self.name, 'fas fa-cogs')
        super().save(*args, **kwargs)
    
    def get_icon(self):
        """Xizmat iconini qaytaradi"""
        return self.icon or self.SERVICE_ICONS.get(self.name, 'fas fa-cogs')


class ServicesDetails(models.Model):
    """Xizmat so'rovlari"""
    company_name = models.CharField(_("Kompaniya nomi"), max_length=100)
    phone_number = PhoneNumberField(_("Telefon raqam"))
    service_type = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name=_("Xizmat turi"))
    contact_name = models.CharField(_("Aloqa uchun ism"), max_length=100)
    description = models.TextField(_("Loyiha tavsifi"))
    email = models.EmailField(_("Email"), blank=True, null=True)
    telegram = models.CharField(_("Telegram"), max_length=50, blank=True, null=True)
    file = models.FileField(_("Fayl"), upload_to='service_requests/', blank=True, null=True)
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)

    class Meta:
        verbose_name = _("Xizmat so'rovi")
        verbose_name_plural = _("Xizmat so'rovlari")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.service_type}"


class Portfolio(models.Model):
    """Portfolio loyihalar"""
    name = models.CharField(_("Loyiha nomi"), max_length=100)
    image = models.ImageField(_("Asosiy rasm"), upload_to='images/portfolio/', blank=True, null=True)
    description = models.TextField(_("Tavsif"), blank=True)
    full_description = models.TextField(_("To'liq tavsif"), blank=True, help_text="Loyiha haqida batafsil ma'lumot")
    project_type = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name=_("Loyiha turi"))
    project_link = models.URLField(_("Loyiha havolasi"), blank=True, null=True)
    client_name = models.CharField(_("Mijoz nomi"), max_length=100, blank=True)
    completion_date = models.DateField(_("Tugatilgan sana"), blank=True, null=True)
    technologies = models.CharField(_("Texnologiyalar"), max_length=200, blank=True)
    features = models.TextField(_("Xususiyatlar"), blank=True, help_text="Har bir xususiyatni yangi qatordan yozing")
    view_count = models.PositiveIntegerField(_("Ko'rishlar soni"), default=0)
    like_count = models.PositiveIntegerField(_("Yoqtirishlar soni"), default=0)
    is_featured = models.BooleanField(_("Tanlangan"), default=False, help_text="Bosh sahifada ko'rsatish")
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfoliolar")
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.name
    
    def get_technologies_list(self):
        """Texnologiyalarni ro'yxat sifatida qaytaradi"""
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',')]
        return []
    
    def get_features_list(self):
        """Xususiyatlarni ro'yxat sifatida qaytaradi"""
        if self.features:
            return [f.strip() for f in self.features.split('\n') if f.strip()]
        return []


class PortfolioImage(models.Model):
    """Portfolio rasmlari"""
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images', verbose_name=_("Portfolio"))
    image = models.ImageField(_("Rasm"), upload_to='images/portfolio/')

    class Meta:
        verbose_name = _("Portfolio rasmi")
        verbose_name_plural = _("Portfolio rasmlari")

    def __str__(self):
        return f"{self.portfolio.name} - rasm"


class Career(models.Model):
    """Vakansiyalar"""
    position = models.CharField(_("Lavozim"), max_length=100)
    location = models.CharField(_("Joylashuv"), max_length=100)
    description = models.TextField(_("Tavsif"))
    requirements = models.TextField(_("Talablar"), blank=True)
    posted_date = models.DateField(_("E'lon qilingan sana"), auto_now_add=True)
    experience_level = models.CharField(_("Tajriba darajasi"), max_length=50)
    deadline = models.DateField(_("Oxirgi muddat"))
    salary = models.CharField(_("Ish haqi"), max_length=50)
    is_active = models.BooleanField(_("Faol"), default=True)

    class Meta:
        verbose_name = _("Vakansiya")
        verbose_name_plural = _("Vakansiyalar")
        ordering = ['-posted_date']

    def __str__(self):
        return self.position


class CareerApplication(models.Model):
    """Vakansiya arizalari"""
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="applications", verbose_name=_("Vakansiya"))
    full_name = models.CharField(_("To'liq ism"), max_length=100)
    message = models.TextField(_("Xabar"))
    file = models.FileField(_("Rezyume"), upload_to='files/career/', blank=True, null=True)
    telegram = models.CharField(_("Telegram"), max_length=50)
    phone_number = models.CharField(_("Telefon raqam"), max_length=20)
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)

    class Meta:
        verbose_name = _("Vakansiya arizasi")
        verbose_name_plural = _("Vakansiya arizalari")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.career.position}"

