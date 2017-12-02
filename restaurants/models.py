from django.db import models

# Create your models here.
class Restaurant(models.Model):
    yelp_id = models.CharField(max_length=200, default='N/A')
    name = models.CharField(max_length=200, default='N/A')
    claimed = models.IntegerField(default=0)
    ratings = models.FloatField(default=0.0)
    ratings_notation = models.CharField(max_length=200,default='0')
    review = models.IntegerField(default=0)
    dollar_signs = models.CharField(max_length=200, default='')
    category = models.CharField(max_length=200, default='N/A')
    prediction = models.IntegerField(default=0)
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    between = models.CharField(max_length=200, default='')
    neighborhood= models.CharField(max_length=200, default='')
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
    def get_all_neighborhoods():
        neighborhoods_unsplit = Restaurant.objects.order_by().values_list('neighborhood').distinct()

        neighborhoods = set()
        for row in neighborhoods_unsplit:

            neighborhoods_str = row[0]

            if not neighborhoods_str:
                continue

            for neighborhood in neighborhoods_str.split(','):
                neighborhoods.add(neighborhood)

        return neighborhoods
