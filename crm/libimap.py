import imaplib
import email


class IMAP(object):
    def __init__(self, server, port, user, password, tls):
        if tls:
            self._imap = imaplib.IMAP4_SSL(server)
        else:
            self._imap = imaplib.IMAP4(server)

        self._imap.login(user, password)

    def select(self, folder):
        self._imap.select(folder)

    def get_email_ids(self):
        result, data = self._imap.search(None, "ALL")
        ids = data[0]
        return map(int, ids.split())

    def get_raw_email(self, email_id):
        result, data = self._imap.fetch(str(email_id), "(RFC822)")
        return data[0][1]

    def get_email(self, email_id):
        return self.parse_email(self.get_raw_email(email_id))

    @staticmethod
    def parse_email(raw_email):
        return email.message_from_string(raw_email)

    @staticmethod
    def get_first_text_block(email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()
