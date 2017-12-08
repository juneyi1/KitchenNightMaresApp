from django.db import models


class Restaurant(models.Model):
    yelp_id = models.CharField(max_length=200, default='N/A')
    name = models.CharField(max_length=200, default='N/A')
    claimed = models.IntegerField(default=0)
    ratings = models.FloatField(default=0.0)
    ratings_notation = models.CharField(max_length=200, default='0')
    review = models.IntegerField(default=0)
    dollar_signs = models.CharField(max_length=200, default='')
    category = models.CharField(max_length=200, default='N/A')
    prediction = models.IntegerField(default=0)
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    between = models.CharField(max_length=200, default='')
    neighborhood = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=200, default='')
    mon = models.CharField(max_length=200, default='N/A')
    tue = models.CharField(max_length=200, default='N/A')
    wed = models.CharField(max_length=200, default='N/A')
    thu = models.CharField(max_length=200, default='N/A')
    fri = models.CharField(max_length=200, default='N/A')
    sat = models.CharField(max_length=200, default='N/A')
    sun = models.CharField(max_length=200, default='N/A')
    mon1 = models.CharField(max_length=200, default='N/A')
    tue1 = models.CharField(max_length=200, default='N/A')
    wed1 = models.CharField(max_length=200, default='N/A')
    thu1 = models.CharField(max_length=200, default='N/A')
    fri1 = models.CharField(max_length=200, default='N/A')
    sat1 = models.CharField(max_length=200, default='N/A')
    sun1 = models.CharField(max_length=200, default='N/A')
    takes_reservations = models.CharField(max_length=200, default='N/A')
    delivery = models.CharField(max_length=200, default='N/A')
    take_out = models.CharField(max_length=200, default='N/A')
    accepts_credit_cards = models.CharField(max_length=200, default='N/A')
    parking = models.CharField(max_length=200, default='N/A')
    good_for_kids = models.CharField(max_length=200, default='N/A')
    good_for_groups = models.CharField(max_length=200, default='N/A')
    attire = models.CharField(max_length=200, default='N/A')
    noise_level = models.CharField(max_length=200, default='N/A')
    alcohol = models.CharField(max_length=200, default='N/A')
    outdoor_seating = models.CharField(max_length=200, default='N/A')
    wifi = models.CharField(max_length=200, default='N/A')
    hastv = models.CharField(max_length=200, default='N/A')
    first_review_date = models.DateTimeField('date first reviewed')
    last_review_date = models.DateTimeField('date last reviewed')
    permanently_closed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_prices_ranges():
        dls = Restaurant.objects.order_by().values_list('dollar_signs').distinct()
        dollar_signs = []
        for row in dls:
            dl = row[0]
            if not dl:
                continue
            if dl not in dollar_signs:
                dollar_signs.append(dl)
        dollar_signs.sort()
        return dollar_signs

    @staticmethod
    def get_all_categories():
        categories_unsplit = Restaurant.objects.order_by().values_list('category').distinct()
        categories = []
        for row in categories_unsplit:
            categories_str = row[0]
            if not categories_str:
                continue
            for category in categories_str.split(','):
                c = category.strip()
                if c not in categories:
                    categories.append(c)
        categories.sort()
        return categories

    @staticmethod
    def get_all_neighborhoods():
        neighborhoods_unsplit = Restaurant.objects.order_by().values_list('neighborhood').distinct()

        neighborhoods = []
        for row in neighborhoods_unsplit:
            neighborhoods_str = row[0]
            if not neighborhoods_str:
                continue
            for neighborhood in neighborhoods_str.split(','):
                n = neighborhood.strip()
                if n not in neighborhoods:
                    neighborhoods.append(n)
        neighborhoods.sort()
        return neighborhoods

    @staticmethod
    def get_from_search(neighborhood, price_range, category):
        filter_options = {}

        if neighborhood:
            filter_options['neighborhood__contains'] = neighborhood

        if price_range:
            filter_options['price_range'] = price_range

        if category:
            filter_options['category__contains'] = category

        result = Restaurant.objects.filter(**filter_options)

        return [i for i in result]

    @staticmethod
    def get_neighborhood_choices():
        choices = Restaurant.get_all_neighborhoods()
        return [("", "neighborhood")] + Restaurant._format_for_choices(choices)

    @staticmethod
    def get_category_choices():
        choices = Restaurant.get_all_categories()
        return [("", "category")] + Restaurant._format_for_choices(choices)

    @staticmethod
    def get_price_range_choices():
        choices = Restaurant.get_all_prices_ranges()
        return [("", "price range")] + Restaurant._format_for_choices(choices)

    @staticmethod
    def _format_for_choices(items):
        return [(i, i) for i in items]
