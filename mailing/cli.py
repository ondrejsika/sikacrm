from .models import ListEmail


def add_email(list_id, email):
    ListEmail(email=email, list_id=int(list_id)).save()


def render_campaign(campaign_id):
    pass


def send_campaign(campaign_id):
    pass

