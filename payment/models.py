from django.db import models

# Create your models here.



#whooa-fervid-hot-humane
#glad-wow-brisk-glee

class MyStripeModel(models.Model):
    name = models.CharField(max_length=100)
    stripe_subscription_id = models.CharField(max_length=100)


class StripeSubscription(models.Model):
    start_date = models.DateTimeField(help_text="The start date of the subscription")
    status = models.CharField(max_length=20, help_text="The status of this subscription")

