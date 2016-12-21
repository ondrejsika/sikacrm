import datetime
import time

import mailing.cli as mailing_cli
import libimap

from email.utils import mktime_tz
from models import EmailAccount, Email, EmailConversationReference, EmailConversation


def crm_load_emails():
    for email_account in EmailAccount.objects.all():
        if not email_account.imap_host:
            continue

        imap = libimap.IMAP(email_account.imap_host,
                            None,  #email_account.port,
                            email_account.imap_user,
                            email_account.imap_password,
                            True,)  #email_account.tls)

        for folder in email_account.folder_set.all():
            imap.select(folder.folder)

            for id in imap.get_email_ids():
                if id and id <= folder.last_id:
                    continue


                message = imap.get_email(id)

                if message.get_references():
                    references = EmailConversationReference.objects.filter(reference__in=message.get_references())
                    if references:
                        email_conversation = references.first().email_conversation
                    else:
                        email_conversation = EmailConversation(email_account=email_account)
                        email_conversation.save()
                else:
                    email_conversation = EmailConversation(email_account=email_account)
                    email_conversation.save()
                    email_conversation_reference, _ = EmailConversationReference.objects.get_or_create(
                        reference=message.get_message_id(),
                        email_conversation=email_conversation,
                    )
                    email_conversation_reference.save()

                for ref in message.get_references():
                    email_conversation_reference, _ = EmailConversationReference.objects.get_or_create(
                        reference=ref,
                        email_conversation=email_conversation,
                    )
                    email_conversation_reference.save()

                Email(
                    email_conversation=email_conversation,
                    email_account=email_account,
                    message_id=message.get_message_id(),
                    date=datetime.datetime.fromtimestamp(mktime_tz(message.get_date())),
                    email_from=message.get_from(),
                    email_to=message.get_to(),
                    folder='inbox' if message._message['to'] == email_account.email else 'outbox',
                    subject=message.get_subject(),
                    body=message.get_body(),
                ).save()
            folder.last_id = id
            folder.save()


FUNCTIONS = {
    'mailing_add_email': mailing_cli.add_email,
    'mailing_render_campaign': mailing_cli.render_campaign,
    'mailing_send_campaign': mailing_cli.send_campaign,

    'crm_load_emails': crm_load_emails,
}


def run(*args):
    func = args[0]
    args = args[1:]

    FUNCTIONS[func](*args)
