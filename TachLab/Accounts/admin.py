from django.contrib import admin
from .models import (
    # About
    AboutSection, AboutFeature, AboutGalleryImage, AboutTeamMember, Subscriber, TrustLogo,

    # Services
    Service, ServiceCategory, ServiceFeature,

    # Products
    Product, ProductCategory, ProductGalleryImage,

    # Contact
    ContactSection, ContactUs,

    # Blogs
    BlogHighlight, BlogCategory, BlogTag,

    # Testimonials
    Testimonial, TestimonialCategory,
)

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_feature_list', 'show_team_preview', 'show_trust_logos']
    filter_horizontal = ['feature_list', 'gallery_images', 'team_members', 'trust_logos']


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class']
    search_fields = ['title']


@admin.register(AboutGalleryImage)
class AboutGalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image_alt_text']
    search_fields = ['caption']


@admin.register(AboutTeamMember)
class AboutTeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
    search_fields = ['name', 'role']


@admin.register(TrustLogo)
class TrustLogoAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'link']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'show_in_slider']
    list_filter = ['category', 'is_featured']
    search_fields = ['title']
    # filter_horizontal = ['feature_list', 'gallery_images']


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class']
    search_fields = ['title']


# @admin.register(ServiceGalleryImage)
# class ServiceGalleryImageAdmin(admin.ModelAdmin):
#     list_display = ['caption', 'image_alt_text']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_price', 'in_stock', 'is_featured']
    list_filter = ['category', 'is_featured']
    search_fields = ['name', 'sku']
    filter_horizontal = ['gallery_images']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']


@admin.register(ProductGalleryImage)
class ProductGalleryImageAdmin(admin.ModelAdmin):
    list_display = ['alt_text']

@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone', 'contact_form_enabled']
    search_fields = ['title', 'email', 'phone']

@admin.register(BlogHighlight)
class BlogHighlightAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'category', 'published_date', 'views_count', 'is_featured']
    list_filter = ['category', 'is_featured']
    search_fields = ['title', 'author_name']
    # filter_horizontal = ['tags']


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'rating', 'location', 'is_featured']
    list_filter = ['category', 'is_featured']
    search_fields = ['name', 'company']


@admin.register(TestimonialCategory)
class TestimonialCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Subscriber)
admin.site.register(ContactUs)