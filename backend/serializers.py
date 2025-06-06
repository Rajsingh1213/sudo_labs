from rest_framework import serializers
from .models import (
    # About
    AboutSection, AboutFeature, AboutGalleryImage, AboutTeamMember, TrustLogo,

    # Services
    Service, ServiceCategory, ServiceFeature,

    # Products
    Product, ProductCategory, ProductGalleryImage,

    # Contact
    ContactSection,

    # Blogs
    BlogHighlight, BlogCategory, BlogTag,

    # Testimonials
    Testimonial, TestimonialCategory,
)
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutGalleryImage  # Can be reused for other image-based models
        fields = ['id', 'image', 'caption', 'image_alt_text']


class BaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection  # Placeholder - override in child classes
        fields = '__all__'

class AboutFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFeature
        fields = '_all_'


class AboutTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeamMember
        fields = '_all_'


class TrustLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustLogo
        fields = '_all_'


class AboutGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutGalleryImage
        fields = '_all_'


class AboutSectionSerializer(serializers.ModelSerializer):
    feature_list = AboutFeatureSerializer(many=True, read_only=True)
    gallery_images = AboutGalleryImageSerializer(many=True, read_only=True)
    team_members = AboutTeamMemberSerializer(many=True, read_only=True)
    trust_logos = TrustLogoSerializer(many=True, read_only=True)

    class Meta:
        model = AboutSection
        fields = '__all__'

class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = '_all_'


# class ServiceGalleryImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceGalleryImage
#         fields = '_all_'


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '_all_'


class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    feature_list = ServiceFeatureSerializer(many=True, read_only=True)
    # gallery_images = ServiceGalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '_all_'

class ProductGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGalleryImage
        fields = '_all_'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '_all_'


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    gallery_images = ProductGalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '_all_'

class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = '_all_'

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '_all_'


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '_all_'


class BlogHighlightSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    tags = BlogTagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogHighlight
        fields = '_all_'

class TestimonialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialCategory
        fields = '_all_'


class TestimonialSerializer(serializers.ModelSerializer):
    category = TestimonialCategorySerializer(read_only=True)

    class Meta:
        model = Testimonial
        fields = '_all_'

from rest_framework import serializers
from .models import (
    HeroSection, AboutSection, Service, Product, BlogHighlight,
    Testimonial, ContactSection
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '_all_'


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '_all_'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '_all_'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'


class BlogHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogHighlight
        fields = '_all_'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '_all_'


class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = '_all_'

class HomePageSerializer(serializers.Serializer):
    hero = HeroSectionSerializer()
    about = AboutSectionSerializer()
    services = ServiceSerializer(many=True)
    products = ProductSerializer(many=True)
    blog_highlights = BlogHighlightSerializer(many=True)
    testimonials = TestimonialSerializer(many=True)
    contact = ContactSectionSerializer()

