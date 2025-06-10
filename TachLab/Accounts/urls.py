from django.urls import path
from .views import (
    AboutSectionList, AboutSectionDetail, AboutFeatureList, AboutTeamMemberList, TrustLogoList,
    ServiceList, ServiceDetail, ServiceCategoryList, ServiceFeatureList,
    ProductList, ProductDetail, ProductCategoryList,
    ContactSectionList, ContactSectionDetail,
    BlogHighlightList, BlogHighlightDetail, BlogCategoryList, BlogTagList,
    TestimonialList, TestimonialDetail, TestimonialCategoryList,
    HeroSectionList, HeroSectionDetail, ProductGalleryImageList,
    HomePageAPIView
)

urlpatterns = [
    path('about-sections/', AboutSectionList.as_view()),
    path('about-sections/<int:pk>/', AboutSectionDetail.as_view()),
    path('about-features/', AboutFeatureList.as_view()),
    path('about-team-members/', AboutTeamMemberList.as_view()),
    path('trust-logos/', TrustLogoList.as_view()),

    path('services/', ServiceList.as_view()),
    path('services/<int:pk>/', ServiceDetail.as_view()),
    path('service-categories/', ServiceCategoryList.as_view()),
    path('service-features/', ServiceFeatureList.as_view()),

    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('product-categories/', ProductCategoryList.as_view()),

    path('contacts/', ContactSectionList.as_view()),
    path('contacts/<int:pk>/', ContactSectionDetail.as_view()),

    path('blogs/', BlogHighlightList.as_view()),
    path('blogs/<int:pk>/', BlogHighlightDetail.as_view()),
    path('blog-categories/', BlogCategoryList.as_view()),
    path('blog-tags/', BlogTagList.as_view()),

    path('testimonials/', TestimonialList.as_view()),
    path('testimonials/<int:pk>/', TestimonialDetail.as_view()),
    path('testimonial-categories/', TestimonialCategoryList.as_view()),

    path('hero-sections/', HeroSectionList.as_view()),
    path('hero-sections/<int:pk>/', HeroSectionDetail.as_view()),

    path('products/<int:product_id>/gallery/', ProductGalleryImageList.as_view()),
    # path('services/<int:service_id>/gallery/', ServiceGalleryImageList.as_view()),

    path('homepage/', HomePageAPIView.as_view(), name='homepage-api'),
]