# coding: utf8

import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_tz


def _decode(text, charset):
    return text.decode(charset) if charset else text


def _decode_header(header):
    return ' '.join(_decode(data, charset) for data, charset in decode_header(header))


class Email(object):
    def __init__(self, raw_message):
        self._raw_message = raw_message

        self._message = email.message_from_string(self._raw_message)

    def get_from(self):
        return _decode_header(self._message['from'])

    def get_to(self):
        return _decode_header(self._message['to'])

    def get_subject(self):
        return _decode_header(self._message['subject'])

    def get_message_id(self):
        return _decode_header(self._message['message-id'])

    def get_references(self):
        if not self._message['references']:
            return []
        return self._message['references'].replace('\r\n', '').split()

    def get_date(self):
        return parsedate_tz(_decode_header(self._message['date']))

    def get_body(self):
        if self._message.is_multipart():
            for part in self._message.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # skip any text/plain (txt) attachments
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = _decode(part.get_payload(decode=True), part.get_content_charset())  # decode
                    break
        # not multipart - i.e. plain text, no attachments, keeping fingers crossed
        else:
            body = _decode(self._message.get_payload(decode=True), self._message.get_content_charset())
        return body


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
        return Email(self.get_raw_email(email_id))
