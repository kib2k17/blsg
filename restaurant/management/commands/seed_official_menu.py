from decimal import Decimal

from django.core.management.base import BaseCommand

from restaurant.models import MenuItem

# (category, name, price) — from BL&SG print menu (Lapu-lapu "Steamed w/ soy sauce" corrected 5550 → 555)
MENU_DATA = [
    # Page 1 — Noodles, snacks, shakes, etc.
    ("noodles", "Pancit canton", Decimal("395")),
    ("noodles", "Sotanghon guisado", Decimal("395")),
    ("noodles", "Bihon guisado", Decimal("385")),
    ("snacks", "Lomi special w/ toasted bread", Decimal("315")),
    ("snacks", "Burger deluxe w/ fries", Decimal("165")),
    ("snacks", "Regular burger", Decimal("120")),
    ("snacks", "French fries", Decimal("100")),
    ("snacks", "Tuna sandwich", Decimal("195")),
    ("snacks", "BL best sandwich", Decimal("205")),
    ("shakes", "Grape shake", Decimal("125")),
    ("shakes", "Mango", Decimal("115")),
    ("shakes", "Watermelon", Decimal("115")),
    ("shakes", "Banana", Decimal("110")),
    ("shakes", "Cookies & cream", Decimal("120")),
    ("shakes", "Chocolate", Decimal("120")),
    ("shakes", "Avocado", Decimal("120")),
    ("shakes", "Banana mango shake", Decimal("135")),
    ("shakes", "Watermelon mango shake", Decimal("135")),
    ("shakes", "Chocolate cookies & cream shake", Decimal("135")),
    ("pitcher", "Ice tea (pitcher)", Decimal("185")),
    ("pitcher", "Blue lemonade", Decimal("190")),
    ("pitcher", "Lychee lemonade", Decimal("190")),
    ("pitcher", "Lemonade (pitcher)", Decimal("190")),
    ("hot_drinks", "Brewed coffee", Decimal("90")),
    ("hot_drinks", "Hot calamansi juice", Decimal("80")),
    ("hot_drinks", "Hot green tea", Decimal("75")),
    ("rice", "Plain cup rice", Decimal("63")),
    ("rice", "Plain platter rice", Decimal("160")),
    ("rice", "Shanghai rice", Decimal("205")),
    ("rice", "Garlic rice", Decimal("195")),
    ("dessert", "Halo-halo", Decimal("125")),
    ("dessert", "Banana split", Decimal("110")),
    ("dessert", "Buko pandan", Decimal("100")),
    ("dessert", "BL ice cream scoop", Decimal("105")),
    ("dessert", "Mais con yelo", Decimal("115")),
    ("appetizer", "Nachos platter", Decimal("260")),
    ("appetizer", "Fresh summer salad", Decimal("220")),
    ("appetizer", "Cucumber tuna salad", Decimal("255")),
    ("cold_drinks", "Warm / cold calamansi juice", Decimal("80")),
    ("cold_drinks", "Ice tea (glass)", Decimal("70")),
    ("cold_drinks", "Bottle water", Decimal("50")),
    ("cold_drinks", "Pineapple juice", Decimal("99")),
    ("cold_drinks", "Coke", Decimal("99")),
    ("cold_drinks", "Coke zero", Decimal("99")),
    ("cold_drinks", "Royale", Decimal("99")),
    ("cold_drinks", "Sprite", Decimal("99")),
    ("fruit_coolers", "Cucumber juice", Decimal("199")),
    ("fruit_coolers", "Watermelon juice", Decimal("199")),
    # Page 2 — Mains
    ("pork", "Lechon", Decimal("575")),
    ("pork", "Pritson", Decimal("620")),
    ("pork", "Lechon paksiw", Decimal("625")),
    ("pork", "Lechon kawali", Decimal("405")),
    ("pork", "Lumpia shanghai", Decimal("318")),
    ("pork", "Crispy pata", Decimal("750")),
    ("pork", "Sweet & sour pork", Decimal("365")),
    ("pork", "Grilled liempo", Decimal("405")),
    ("pork", "Pork tinola", Decimal("420")),
    ("pork", "Pork sinigang", Decimal("420")),
    ("pork", "Sizzling sisig", Decimal("340")),
    ("goat_meat", "Kalderetang kambing", Decimal("670")),
    ("goat_meat", "Kilawin (goat)", Decimal("335")),
    ("chicken", "Garlic chicken", Decimal("410")),
    ("chicken", "Crispy fried chicken", Decimal("405")),
    ("chicken", "Buttered chicken", Decimal("399")),
    ("chicken", "Cordon bleu", Decimal("405")),
    ("value_meal", "Pecho (value meal)", Decimal("189")),
    ("value_meal", "Paa (value meal)", Decimal("179")),
    ("value_meal", "Pritson (value meal)", Decimal("225")),
    ("value_meal", "Lechon paksiw (value meal)", Decimal("215")),
    ("squid", "Calamares", Decimal("470")),
    ("squid", "Adobo squid w/ atta", Decimal("465")),
    ("squid", "Adobo squid w/o atta", Decimal("465")),
    ("squid", "Sizzling squid", Decimal("480")),
    ("squid", "Grilled squid", Decimal("435")),
    ("beef", "Beef w/ broccoli", Decimal("495")),
    ("beef", "Beef w/ ampalaya", Decimal("430")),
    ("beef", "Beef w/ oyster sauce", Decimal("470")),
    ("beef", "Beef w/ mushroom", Decimal("445")),
    ("fish_tuna", "Sweet & sour fillet", Decimal("405")),
    ("fish_tuna", "Fish tausi", Decimal("405")),
    ("fish_tuna", "Grilled (tuna)", Decimal("395")),
    ("fish_tuna", "Kinilaw", Decimal("399")),
    ("fish_tuna", "Sinuglaw", Decimal("450")),
    ("fish_tuna", "Tinola (tuna)", Decimal("390")),
    ("fish_tuna", "Sinigang (tuna)", Decimal("390")),
    ("shrimp", "Sizzling gambas", Decimal("399")),
    ("shrimp", "Fried w/ garlic shrimp", Decimal("379")),
    ("shrimp", "Tempura (shrimp)", Decimal("395")),
    ("shrimp", "Shrimp tinola", Decimal("400")),
    ("shrimp", "Shrimp sinigang", Decimal("435")),
    ("lapu_lapu", "Sweet & sour (lapu-lapu)", Decimal("545")),
    ("lapu_lapu", "Steamed w/ soy sauce (lapu-lapu)", Decimal("555")),  # print shows 5550; corrected
    ("lapu_lapu", "Steamed w/ white sauce (lapu-lapu)", Decimal("555")),
    ("lapu_lapu", "Tinola (lapu-lapu)", Decimal("505")),
    ("lapu_lapu", "Sinigang (lapu-lapu)", Decimal("505")),
    ("vegetables", "Four season", Decimal("405")),
    ("vegetables", "Chopsuey", Decimal("325")),
    ("vegetables", "Pinakbet", Decimal("350")),
]

# Shown on home when no manual picks; distinct (category, name) keys
DEFAULT_FEATURED = {
    ("pork", "Lechon"),
    ("pork", "Crispy pata"),
    ("chicken", "Garlic chicken"),
    ("dessert", "Halo-halo"),
    ("pork", "Sizzling sisig"),
    ("fish_tuna", "Sinigang (tuna)"),
}


class Command(BaseCommand):
    help = "Load or update the full BL&SG print menu (idempotent: matches category + name)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all menu items first, then insert.",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            n = MenuItem.objects.all().count()
            MenuItem.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Removed {n} existing menu item(s)."))

        created, updated, skipped = 0, 0, 0
        for category, name, price in MENU_DATA:
            is_featured = (category, name) in DEFAULT_FEATURED
            obj, was_created = MenuItem.objects.update_or_create(
                category=category,
                name=name,
                defaults={
                    "price": price,
                    "is_featured": is_featured,
                    "is_available": True,
                    "description": "",
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Menu sync done: {created} created, {updated} updated (idempotent re-run = all updated)."
            )
        )
