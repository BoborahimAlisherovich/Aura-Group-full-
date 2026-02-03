from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import (
    OurTeam,
    ContactUs,
    Services,
    ServicesDetails,
    Portfolio,
    PortfolioImage,
    Career,
    CareerApplication,
)


# ============================================
# JAMOA A'ZOLARI ADMIN
# ============================================
@admin.register(OurTeam)
class OurTeamAdmin(TranslationAdmin):
    """Jamoa a'zolari admin paneli"""
    list_display = ('image_preview', 'name', 'position', 'experience_years', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position')
    list_filter = ('position',)
    ordering = ['order', 'name']

    fieldsets = (
        ('👤 Asosiy ma\'lumotlar', {
            'fields': ('name', 'image', 'position', 'experience_years', 'order')
        }),
        ('📝 Tavsif', {
            'fields': ('description', 'skills', 'story'),
            'classes': ('collapse',)
        }),
        ('🔗 Ijtimoiy tarmoqlar', {
            'fields': ('telegram', 'linkedin', 'github'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;width:50px;object-fit:cover;border-radius:50%;border:2px solid #6366f1;" />',
                obj.image.url
            )
        return format_html('<span style="color:#ccc;">{}</span>', '📷')
    image_preview.short_description = 'Rasm'


# ============================================
# ALOQA SO'ROVLARI ADMIN
# ============================================
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """Aloqa so'rovlari admin paneli"""
    list_display = ('full_name', 'phone_number', 'email', 'short_message', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('full_name', 'phone_number', 'email', 'message', 'created_at')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    def short_message(self, obj):
        if len(obj.message) > 50:
            return obj.message[:50] + '...'
        return obj.message
    short_message.short_description = 'Xabar'
    
    def has_add_permission(self, request):
        return False


# ============================================
# XIZMATLAR ADMIN
# ============================================
@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    """Xizmatlar admin paneli"""
    list_display = ('get_name_display', 'icon_preview',  'short_description', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'name')
    ordering = ['order', 'name']

    fieldsets = (
        ('🏷️ Xizmat turi', {
            'fields': ('name', 'order', 'is_active'),
            'description': '📋 Xizmat turini ro\'yxatdan tanlang. Icon avtomatik qo\'yiladi.'
        }),
        ('📝 Tavsif', {
            'fields': ('description',)
        }),
        ('⚙️ Qo\'shimcha (ixtiyoriy)', {
            'fields': ('icon',),
            'classes': ('collapse',),
            'description': 'Agar boshqa icon xohlasangiz, bu yerda o\'zgartiring.'
        }),
    )

    def icon_preview(self, obj):
        icon = obj.get_icon() if hasattr(obj, 'get_icon') else obj.icon
        if icon:
            return format_html(
                '<i class="{}" style="font-size:24px;color:#6366f1;"></i>',
                icon
            )
        return '-'
    icon_preview.short_description = 'Icon'
    
    def get_name_display(self, obj):
        return obj.get_name_display()
    get_name_display.short_description = 'Xizmat turi'
    get_name_display.admin_order_field = 'name'
    
    def short_description(self, obj):
        if len(obj.description) > 60:
            return obj.description[:60] + '...'
        return obj.description
    short_description.short_description = 'Tavsif'


# ============================================
# XIZMAT SO'ROVLARI ADMIN
# ============================================
@admin.register(ServicesDetails)
class ServicesDetailsAdmin(admin.ModelAdmin):
    """Xizmat so'rovlari admin paneli"""
    list_display = ('company_name', 'contact_name', 'service_type', 'phone_number', 'telegram', 'created_at', 'status_badge')
    search_fields = ('company_name', 'contact_name', 'phone_number', 'email', 'telegram')
    list_filter = ('service_type', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('🏢 Kompaniya ma\'lumotlari', {
            'fields': ('company_name', 'contact_name', 'service_type')
        }),
        ('📞 Aloqa', {
            'fields': ('phone_number', 'email', 'telegram')
        }),
        ('📋 Loyiha tafsilotlari', {
            'fields': ('description', 'file')
        }),
        ('📅 Vaqt', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def status_badge(self, obj):
        return format_html(
            '<span style="background:#22c55e;color:white;padding:3px 10px;border-radius:12px;font-size:11px;">{}</span>',
            'Yangi'
        )
    status_badge.short_description = 'Status'
    
    def has_add_permission(self, request):
        return False


# ============================================
# PORTFOLIO ADMIN
# ============================================
class PortfolioImageInline(admin.TabularInline):
    """Portfolio rasmlari inline"""
    model = PortfolioImage
    extra = 1
    classes = ['collapse']


@admin.register(Portfolio)
class PortfolioAdmin(TranslationAdmin):
    """Portfolio admin paneli"""
    list_display = ('image_preview', 'name', 'project_type', 'stats_display', 'created_at')
    search_fields = ('name', 'technologies')
    list_filter = ('project_type', 'created_at')
    readonly_fields = ('view_count', 'like_count', 'created_at')
    inlines = [PortfolioImageInline]
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('📁 Asosiy ma\'lumotlar', {
            'fields': ('name', 'image', 'project_type', 'project_link', 'technologies')
        }),
        ('📝 Tavsif', {
            'fields': ('description',)
        }),
        ('📊 Statistika', {
            'fields': ('view_count', 'like_count', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;width:80px;object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return format_html('<span style="color:#ccc;">{}</span>', '🖼️')
    image_preview.short_description = 'Rasm'
    
    def stats_display(self, obj):
        return format_html(
            '<span style="color:#6366f1;">👁️ {}</span> &nbsp; <span style="color:#ef4444;">❤️ {}</span>',
            obj.view_count,
            obj.like_count
        )
    stats_display.short_description = 'Statistika'


# ============================================
# VAKANSIYALAR ADMIN
# ============================================
@admin.register(Career)
class CareerAdmin(TranslationAdmin):
    """Vakansiyalar admin paneli"""
    list_display = ('position', 'location', 'salary', 'deadline', 'status_badge')
    list_editable = ()
    search_fields = ('position', 'location')
    list_filter = ('is_active', 'posted_date', 'deadline')
    readonly_fields = ('posted_date',)
    ordering = ['-posted_date']
    date_hierarchy = 'posted_date'

    fieldsets = (
        ('💼 Vakansiya ma\'lumotlari', {
            'fields': ('position', 'location', 'salary', 'experience_level')
        }),
        ('📋 Tavsif va talablar', {
            'fields': ('description', 'requirements')
        }),
        ('⚙️ Holati', {
            'fields': ('deadline', 'is_active', 'posted_date')
        }),
    )
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="background:#22c55e;color:white;padding:3px 10px;border-radius:12px;font-size:11px;">{}</span>',
                '✅ Faol'
            )
        return format_html(
            '<span style="background:#ef4444;color:white;padding:3px 10px;border-radius:12px;font-size:11px;">{}</span>',
            '❌ Yopiq'
        )
    status_badge.short_description = 'Holat'


# ============================================
# VAKANSIYA ARIZALARI ADMIN
# ============================================
@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    """Vakansiya arizalari admin paneli"""
    list_display = ('full_name', 'career', 'phone_number', 'telegram', 'created_at', 'resume_link')
    search_fields = ('full_name', 'phone_number', 'telegram')
    list_filter = ('career', 'created_at')
    readonly_fields = ('full_name', 'phone_number', 'telegram', 'career', 'message', 'file', 'created_at')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('👤 Nomzod ma\'lumotlari', {
            'fields': ('full_name', 'phone_number', 'telegram')
        }),
        ('💼 Vakansiya', {
            'fields': ('career',)
        }),
        ('📝 Xabar va Resume', {
            'fields': ('message', 'file')
        }),
        ('📅 Vaqt', {
            'fields': ('created_at',)
        }),
    )
    
    def resume_link(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank" style="color:#6366f1;text-decoration:none;">📄 Ko\'rish</a>',
                obj.file.url
            )
        return format_html('<span style="color:#ccc;">{}</span>', '—')
    resume_link.short_description = 'Resume'
    
    def has_add_permission(self, request):
        return False


# ============================================
# ADMIN PANEL SOZLAMALARI
# ============================================
admin.site.site_header = "🚀 AURA Group Boshqaruv Paneli"
admin.site.site_title = "AURA Group Admin"
admin.site.index_title = "Boshqaruv Paneliga Xush Kelibsiz!"



