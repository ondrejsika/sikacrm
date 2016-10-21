import mailing.cli as mailing_cli
import libimap

from models import EmailAccount, Email

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
                if id and id < folder.last_id:
                    continue

                m = imap.get_email(id)
                Email(
                    email_account=email_account,
                    email_from=m['from'],
                    email_to=m['to'],
                    folder='inbox' if m['to'] == email_account.email else 'outbox',
                    subject=m['subject'],
                    body=imap.get_first_text_block(m),
                ).save()
            folder.last_id = id
            folder.save()


FUNCTIONS = {
    'mailing_add_email': mailing_cli.add_email,
    'mailing_render_campaign': mailing_cli.render_campaign,
    'mailing_send_campaign': mailing_cli.send_campaign,

    'crm_load_emails': crm_load_emails,
}


def run(*args, **options):
    func = args[0]
    args = args[1:]

    FUNCTIONS[func](*args)
