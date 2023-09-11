from django.shortcuts import render
from djstripe.models import Product

from django.views.generic.base import TemplateView


from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe
stripe.api_key = "sk_test_51NokjjGwYrEQlYDwvdocD89ZgapAOYtQ75n7qRlc6u9W4PzJe7kJERQvf0Ti025BV8mOI0pyAGRr7fQDqxfwurK200Rp7uZVjv"
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'payment/home.html'


def pricing_page(request):
    # if ludicrous_mode_enabled(user):
    #     do_ludicrous_stuff()
    return render(request, 'payment/pricing_page.html', {'products': Product.objects.all()})




@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY }
        return JsonResponse(stripe_config, safe=False)
    


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000'
        # success_url = domain_url + 'success?session_id={CHECKOUT_SESSION_ID}', 
        # cancel_url = domain_url + 'cancelled/',
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param

            checkout_session = stripe.checkout.Session.create(
                success_url = domain_url + 'success?session_id={CHECKOUT_SESSION_ID}', 
                
                cancel_url = domain_url + 'cancelled/',
                payment_method_types = ['card'],
                mode = 'payment',
                line_items = [
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '20000'
                    }
                ],
            )
        
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})