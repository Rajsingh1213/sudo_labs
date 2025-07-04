from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SEOFields(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True)
    schema_markup = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class BaseSection(TimeStampedModel, SEOFields):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    order = models.PositiveIntegerField(default=0)

    # Layout and style
    background_color = models.CharField(max_length=7, blank=True, null=True, help_text="e.g. #FFFFFF")
    text_color = models.CharField(max_length=7, blank=True, null=True)
    section_id = models.CharField(max_length=100, blank=True, null=True, help_text="For page anchor navigation")
    custom_css_class = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['order']


class HeroSection(BaseSection):
    headline = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True)
    rich_description = RichTextField(blank=True, null=True)

    background_image = models.ImageField(upload_to='hero/')
    background_mobile_image = models.ImageField(upload_to='hero/mobile/', blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True)

    overlay_color = models.CharField(max_length=7, default='#000000')
    overlay_opacity = models.FloatField(default=0.4)

    # Primary CTA
    button_text = models.CharField(max_length=100)
    button_link = models.URLField()
    button_icon = models.CharField(max_length=100, blank=True)

    # Secondary CTA
    second_button_text = models.CharField(max_length=100, blank=True)
    second_button_link = models.URLField(blank=True)
    second_button_icon = models.CharField(max_length=100, blank=True)

    # Optional Video
    video_url = models.URLField(blank=True, null=True)
    video_popup_enabled = models.BooleanField(default=False)


class Service(BaseSection):
    icon_class = models.CharField(max_length=100, help_text="e.g., fa fa-truck")
    short_description = models.CharField(max_length=500)
    full_description = RichTextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    # Style options
    card_background_color = models.CharField(max_length=7, blank=True, null=True)
    card_text_color = models.CharField(max_length=7, blank=True, null=True)


class Testimonial(BaseSection):
    name = models.CharField(max_length=255)
    feedback = RichTextField()
    rating = models.PositiveSmallIntegerField(default=5)
    designation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)
    show_on_slider = models.BooleanField(default=True)

class BlogHighlight(BaseSection):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    blog_link = models.URLField()
    image = models.ImageField(upload_to='blogs/')
    image_alt_text = models.CharField(max_length=255, blank=True)
    author_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    published_date = models.DateField()
    read_time_minutes = models.PositiveIntegerField(default=3)
    is_featured = models.BooleanField(default=False)
    show_date = models.BooleanField(default=True)


class ContactSection(BaseSection):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    map_embed_code = models.TextField(blank=True)
    working_hours = models.CharField(max_length=255, blank=True)
    contact_form_enabled = models.BooleanField(default=True)
    contact_form_recaptcha = models.BooleanField(default=False)

    # Social links
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    # Tracking
    google_tracking_id = models.CharField(max_length=100, blank=True, null=True)
    facebook_pixel_id = models.CharField(max_length=100, blank=True, null=True)


class AboutSection(BaseSection):
    rich_content = RichTextField(verbose_name="Main Content")
    
    # Images
    image = models.ImageField(upload_to='about/', verbose_name="Primary Image")
    image_alt_text = models.CharField(max_length=255, blank=True)
    secondary_image = models.ImageField(upload_to='about/', blank=True, null=True)
    secondary_image_alt = models.CharField(max_length=255, blank=True)
    
    # Gallery
    gallery_title = models.CharField(max_length=255, blank=True)
    gallery_images = models.ManyToManyField('AboutGalleryImage', blank=True)

    # Optional Video
    video_url = models.URLField(blank=True, null=True)
    video_caption = models.CharField(max_length=255, blank=True)

    # Core messages
    mission = RichTextField(blank=True, null=True)
    vision = RichTextField(blank=True, null=True)
    core_values = RichTextField(blank=True, null=True)

    # Bullet points or features
    show_feature_list = models.BooleanField(default=False)
    feature_list = models.ManyToManyField('AboutFeature', blank=True)

    # Counters (optional)
    show_counters = models.BooleanField(default=False)
    experience_years = models.PositiveIntegerField(default=0)
    completed_projects = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)
    team_strength = models.PositiveIntegerField(default=0)

    # CTA
    cta_text = models.CharField(max_length=100, blank=True)
    cta_link = models.URLField(blank=True)
    cta_icon = models.CharField(max_length=100, blank=True)

    # Achievements
    awards_description = RichTextField(blank=True)
    awards_image = models.ImageField(upload_to='about/awards/', blank=True, null=True)

    # Optional team member spotlight
    show_team_preview = models.BooleanField(default=False)
    team_members = models.ManyToManyField('AboutTeamMember', blank=True)

    # Client logos or trust badges
    show_trust_logos = models.BooleanField(default=False)
    trust_logos = models.ManyToManyField('TrustLogo', blank=True)

    class Meta:
        verbose_name = "About Us Section"
        verbose_name_plural = "About Us Sections"


class AboutFeature(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class AboutGalleryImage(models.Model):
    image = models.ImageField(upload_to='about/gallery/')
    caption = models.CharField(max_length=255, blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Gallery Image"
    

class AboutTeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='about/team/')
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class TrustLogo(models.Model):
    logo = models.ImageField(upload_to='about/trust_logos/')
    alt_text = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.alt_text or "Logo"
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/categories/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel, SEOFields):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    short_description = models.CharField(max_length=500, blank=True)

    image = models.ImageField(upload_to='products/main/')
    gallery_images = models.ManyToManyField('ProductGalleryImage', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)

    # Optional
    tags = models.CharField(max_length=255, blank=True)
    sku = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    

class ProductGalleryImage(models.Model):
    image = models.ImageField(upload_to='products/gallery/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.alt_text or "Product Image"
    

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/categories/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Service(BaseSection):
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True)
    icon_class = models.CharField(max_length=100, help_text="e.g., fa fa-cog")
    short_description = models.CharField(max_length=500)
    full_description = RichTextField(blank=True)

    image = models.ImageField(upload_to='services/main/', blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)
    # gallery_images = models.ManyToManyField('ServiceGalleryImage', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, help_text="e.g. 2 weeks, 3 days")

    is_featured = models.BooleanField(default=False)
    show_in_slider = models.BooleanField(default=False)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.URLField(blank=True)

    # feature_list = models.ManyToManyField('ServiceFeature', blank=True)

    def __str__(self):
        return self.title
    

class ServiceFeature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, blank=True)

class ContactSection(BaseSection):
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    email = models.EmailField()
    alternate_email = models.EmailField(blank=True, null=True)

    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)

    working_hours = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=100, blank=True)

    contact_person = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

    # Map
    map_embed_code = models.TextField(blank=True)

    # Social Media
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    # Form Flags
    contact_form_enabled = models.BooleanField(default=True)
    contact_form_recaptcha = models.BooleanField(default=False)
    thank_you_message = models.CharField(max_length=255, blank=True)

    # Analytics
    google_tracking_id = models.CharField(max_length=100, blank=True, null=True)
    facebook_pixel_id = models.CharField(max_length=100, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Contact: {self.title}"
    

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogHighlight(BaseSection):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    # tags = models.ManyToManyField(BlogTag, blank=True)
    
    author_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='blogs/authors/', blank=True)
    author_bio = models.TextField(blank=True)

    summary = models.TextField()
    content = RichTextField()
    blog_link = models.URLField(blank=True)

    image = models.ImageField(upload_to='blogs/')
    image_alt_text = models.CharField(max_length=255, blank=True)
    
    published_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)
    read_time_minutes = models.PositiveIntegerField(default=3)
    views_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)


class TestimonialCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Testimonial(BaseSection):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='testimonials/', blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)
    
    designation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=255, blank=True)
    company_logo = models.ImageField(upload_to='testimonials/logos/', blank=True)

    location = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(TestimonialCategory, on_delete=models.SET_NULL, null=True, blank=True)

    rating = models.PositiveSmallIntegerField(default=5)
    feedback = RichTextField()

    video_review_url = models.URLField(blank=True, null=True)
    show_on_slider = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} – {self.company}"
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ContactUs(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"