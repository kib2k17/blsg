from .models import SiteSettings


def site_settings(_request):
    """Expose `site` (SiteSettings singleton) in all templates."""
    return {"site": SiteSettings.load()}
