from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

# from .models import (
#     HeroSection, AboutSection, Service, Product,
#     BlogHighlight, Testimonial, ContactSection
# )
# from .serializers import (
#     HeroSectionSerializer, AboutSectionSerializer, ServiceSerializer,
#     ProductSerializer, BlogHighlightSerializer, TestimonialSerializer,
#     ContactSectionSerializer
# )

# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response

from .models import (
    HeroSection, AboutSection, AboutFeature, AboutGalleryImage, AboutTeamMember, TrustLogo,
    Service, ServiceCategory, ServiceFeature,
    Product, ProductCategory, ProductGalleryImage,
    ContactSection,
    BlogHighlight, BlogCategory, BlogTag,
    Testimonial, TestimonialCategory,
)

from .serializers import (
    HeroSectionSerializer, AboutSectionSerializer, AboutFeatureSerializer, ImageSerializer, AboutTeamMemberSerializer, TrustLogoSerializer,
    ServiceSerializer, ServiceCategorySerializer, ServiceFeatureSerializer,
    ProductSerializer, ProductCategorySerializer, ProductGalleryImageSerializer,
    ContactSectionSerializer,
    BlogHighlightSerializer, BlogCategorySerializer, BlogTagSerializer,
    TestimonialSerializer, TestimonialCategorySerializer,
)

class AboutSectionList(generics.ListAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class AboutSectionDetail(generics.RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class AboutFeatureList(generics.ListAPIView):
    queryset = AboutFeature.objects.all()
    serializer_class = AboutFeatureSerializer

class AboutTeamMemberList(generics.ListAPIView):
    queryset = AboutTeamMember.objects.all()
    serializer_class = AboutTeamMemberSerializer

class TrustLogoList(generics.ListAPIView):
    queryset = TrustLogo.objects.all()
    serializer_class = TrustLogoSerializer

class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceCategoryList(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceFeatureList(generics.ListAPIView):
    queryset = ServiceFeature.objects.all()
    serializer_class = ServiceFeatureSerializer

# class ServiceGalleryImageList(generics.ListAPIView):
#     queryset = ServiceGalleryImage.objects.all()
#     serializer_class = ServiceGalleryImageSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryList(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ContactSectionList(generics.ListAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer

class ContactSectionDetail(generics.RetrieveAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer

class BlogHighlightList(generics.ListAPIView):
    queryset = BlogHighlight.objects.all()
    serializer_class = BlogHighlightSerializer

class BlogHighlightDetail(generics.RetrieveAPIView):
    queryset = BlogHighlight.objects.all()
    serializer_class = BlogHighlightSerializer

class BlogCategoryList(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogTagList(generics.ListAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class TestimonialList(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialDetail(generics.RetrieveAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialCategoryList(generics.ListAPIView):
    queryset = TestimonialCategory.objects.all()
    serializer_class = TestimonialCategorySerializer

class HeroSectionList(generics.ListAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class HeroSectionDetail(generics.RetrieveAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class AboutGalleryImageList(generics.ListAPIView):
    queryset = AboutGalleryImage.objects.all()
    serializer_class = ImageSerializer

class ProductGalleryImageList(generics.ListAPIView):
    queryset = ProductGalleryImage.objects.all()
    serializer_class = ProductGalleryImageSerializer


class HomePageAPIView(APIView):
    def get(self, request, format=None):
        try:
            hero = HeroSection.objects.first()
            about = AboutSection.objects.first()
            contact = ContactSection.objects.first()

            services = Service.objects.filter(is_featured=True)
            products = Product.objects.filter(is_featured=True)
            blogs = BlogHighlight.objects.filter(is_featured=True)
            testimonials = Testimonial.objects.filter(is_featured=True)

            data = {
                "hero": HeroSectionSerializer(hero).data if hero else None,
                "about": AboutSectionSerializer(about).data if about else None,
                "services": ServiceSerializer(services, many=True).data,
                "products": ProductSerializer(products, many=True).data,
                "blog_highlights": BlogHighlightSerializer(blogs, many=True).data,
                "testimonials": TestimonialSerializer(testimonials, many=True).data,
                "contact": ContactSectionSerializer(contact).data if contact else None,
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib import messages
from django.core.exceptions import ValidationError
from.models import Subscriber

def base_view(request):
    return render(request,'base.html')

def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def services_view(request):
    return render(request,'services.html')

def products_view(request):
    return render(request,'products.html')

def blogs_view(request):
    return render(request,'blog.html')

def testimonials_view(request):
    return render(request,'testimonials.html')

def contact_view(request):
    return render(request,'contact.html')

def index_view(request):
    return render(request,'index7.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Email is required.")
            return redirect('accounts:index')
        else:
            try:
                validate_email(email)
                subscriber, created = Subscriber.objects.get_or_create(email=email)
                if created:
                    messages.success(request, "Thank you for subscribing!")
                else:
                    messages.info(request, "You are already subscribed.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
    return redirect('accounts:index')

