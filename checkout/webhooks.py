from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from stripe """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.apikey = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signiture
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNITURE']
    event = None

    try:
        event = stripe.webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignitureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exeption as e:
        return HttpResponse(content=e, status=400)
    print('Success!')
    return HttpResponse(status=200)
