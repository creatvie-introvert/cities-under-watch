from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Collection(models.Model):
    class ReleaseStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        COMING_SOON = 'coming_soon', 'Coming Soon'
        ARCHIVED = 'archived', 'Archived'

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='collections'
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='collections/',
        blank=True,
        null=True
    )
    image_alt_text = models.CharField(max_length=255, blank=True)
    planned_product_count = models.PositiveIntegerField(
        default=0,
        help_text='Use for display counts, coming soon colections'
    )
    release_status = models.CharField(
        max_length=20,
        choices=ReleaseStatus.choices,
        default=ReleaseStatus.AVAILABLE
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ('city', 'name')

    def __str__(self):
        return self.name


class CollectionNarrativePanel(models.Model):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="narrative_panels"
    )
    panel_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    label = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="collection_narratives",
        blank=True,
        null=True
    )
    image_alt = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['panel_number']
        unique_together = ['collection', 'panel_number']
    
    def __str__(self):
        return f'{self.collection.name} - Panel {self.panel_number}'


class Product(models.Model):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='products'
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    sku = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    context_text = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=255, blank=True)
    is_primary = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"{self.product.title} image"
