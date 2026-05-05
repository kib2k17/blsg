from collections import OrderedDict

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

from .forms import ContactForm
from .models import CATEGORY_CHOICES, GalleryPhoto, MenuItem, SiteSettings


@require_GET
def home(request):
    site = SiteSettings.load()
    featured = list(
        MenuItem.objects.filter(
            is_available=True,
            is_featured=True,
        ).order_by("category", "name")[:6]
    )
    if len(featured) < 6:
        extra = list(
            MenuItem.objects.filter(
                is_available=True,
                is_featured=False,
            ).order_by("-created_at")[: 6 - len(featured)]
        )
        # Avoid duplicates
        have = {i.pk for i in featured}
        for item in extra:
            if item.pk not in have:
                featured.append(item)
                have.add(item.pk)
        featured = featured[:6]

    return render(
        request,
        "restaurant/home.html",
        {
            "featured_items": featured,
            "home_lead": site.about_lead or site.tagline,
        },
    )


@require_GET
def menu(request):
    available = MenuItem.objects.filter(is_available=True).order_by("name")
    by_key = OrderedDict((key, []) for key, _ in CATEGORY_CHOICES)
    for item in available:
        by_key[item.category].append(item)
    label_map = dict(CATEGORY_CHOICES)
    sections = [
        (key, label_map[key], by_key[key])
        for key, _ in CATEGORY_CHOICES
    ]
    return render(
        request,
        "restaurant/menu.html",
        {
            "sections": sections,
        },
    )


@require_GET
def about(request):
    return render(request, "restaurant/about.html")


@require_GET
def gallery(request):
    photos = GalleryPhoto.objects.all()
    return render(
        request,
        "restaurant/gallery.html",
        {
            "photos": photos,
        },
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Message sent! We will contact you soon.",
            )
            return redirect("contact")
    else:
        form = ContactForm()
    return render(
        request,
        "restaurant/contact.html",
        {
            "form": form,
        },
    )
