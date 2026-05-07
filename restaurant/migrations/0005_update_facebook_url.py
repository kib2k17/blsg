# Generated manually on 2026-05-07

from django.db import migrations, models


FACEBOOK_URL = "https://www.facebook.com/SMCityMallMainBranch"


def update_facebook_url(apps, schema_editor):
    SiteSettings = apps.get_model("restaurant", "SiteSettings")
    SiteSettings.objects.filter(facebook_url__in=["", "https://www.facebook.com/"]).update(
        facebook_url=FACEBOOK_URL
    )


def restore_placeholder(apps, schema_editor):
    SiteSettings = apps.get_model("restaurant", "SiteSettings")
    SiteSettings.objects.filter(facebook_url=FACEBOOK_URL).update(
        facebook_url="https://www.facebook.com/"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_full_menu_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitesettings",
            name="facebook_url",
            field=models.URLField(
                default=FACEBOOK_URL,
                help_text="Official Facebook page for the restaurant.",
                max_length=500,
                verbose_name="Facebook page URL",
            ),
        ),
        migrations.RunPython(update_facebook_url, restore_placeholder),
    ]
