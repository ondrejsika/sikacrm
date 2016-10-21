import mailing.cli as mailing_cli


FUNCTIONS = {
    'mailing_add_email': mailing_cli.add_email,
    'mailing_render_campaign': mailing_cli.render_campaign,
    'mailing_send_campaign': mailing_cli.send_campaign,
}


def run(*args, **options):
    func = args[0]
    args = args[1:]

    FUNCTIONS[func](*args)
