from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

CATEGORY_CHOICES = [
    ("appetizer", "Appetizer"),
    ("pork", "Pork"),
    ("goat_meat", "Goat meat"),
    ("chicken", "Chicken"),
    ("value_meal", "Value meal"),
    ("beef", "Beef"),
    ("fish_tuna", "Fish & tuna"),
    ("shrimp", "Shrimp"),
    ("squid", "Squid"),
    ("lapu_lapu", "Lapu-lapu"),
    ("vegetables", "Vegetables"),
    ("noodles", "Noodles"),
    ("snacks", "Snacks"),
    ("rice", "Rice"),
    ("dessert", "Dessert"),
    ("shakes", "Shakes"),
    ("pitcher", "Pitcher"),
    ("hot_drinks", "Hot drinks"),
    ("cold_drinks", "Cold drinks"),
    ("fruit_coolers", "Fresh fruit coolers"),
]


class SiteSettings(models.Model):
    tagline = models.CharField(max_length=255, default="The pleasure of variety on your plate")
    about_lead = models.TextField(
        blank=True,
        default=(
            "Family-style Filipino favorites—crispy lechon, fresh seafood, and grill classics—"
            "served at SM City Mall, Butuan City."
        ),
        help_text="Short intro for home/about snippet (supports line breaks).",
    )
    about_text = models.TextField(
        blank=True,
        default=(
            "Butuan Lechon & Seafoods Grill brings together the best of Mindanao hospitality and "
            "beloved Filipino flavors. From whole lechon celebrations to everyday seafood plates, "
            "our kitchen focuses on consistent quality, generous portions, and a warm dining "
            "experience for families and friends on the 2nd floor of SM City Butuan."
        ),
        help_text="Longer story for the About page.",
    )
    phone = models.CharField(max_length=32, default="09516811367")
    email = models.EmailField(default="butuanlechon2022@gmail.com")
    address = models.CharField(
        max_length=255,
        default="SM City Mall, 2nd Floor, J.C. Aquino Ave., Butuan City",
    )
    facebook_url = models.URLField(
        "Facebook page URL",
        max_length=500,
        default="https://www.facebook.com/SMCityMallMainBranch",
        help_text="Official Facebook page for the restaurant.",
    )
    maps_query = models.CharField(
        "Google Maps place query",
        max_length=200,
        default="SM City Butuan",
        help_text="Used in the map embed; adjust if the pin is off.",
    )

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return "Butuan Lechon — site settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0"))],
    )
    image = models.ImageField(upload_to="menu/", blank=True, null=True)
    is_featured = models.BooleanField(
        default=False,
        help_text="Show on the home page featured grid (up to 6, plus backfill by newest).",
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.caption or f"Photo {self.pk}"


class ContactInquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=32, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark when handled in admin.")

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Contact inquiry"
        verbose_name_plural = "Contact inquiries"

    def __str__(self):
        return f"{self.name} — {self.submitted_at:%Y-%m-%d %H:%M}"
