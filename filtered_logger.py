#!/usr/bin/env python3
"""Filtering log"""
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields, redaction, message, separator):
    """The filter_datum function returns the log message obfuscated.
    Obfuscation is the process of disguising confidential or sensitive data."""
    a = r"(" + '|'.join(fields) + r")=([^" + separator + "]*)"
    return re.sub(a, r"\1=" + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ The format method uses filter_datum to obfuscate the message and
        returns the result"""
        r = record.getMessage()
        s = self.fields
        record.msg = filter_datum(s, self.REDACTION, r, self.SEPARATOR)
        return super().format(record)

def get_logger() -> logging.Logger:
    
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)

    log.propagate = False

    handler.setFormatter(RedactingFormatter(Fields=PII_FIELDS))
    log.addHandler(log.StreamHandler())
    return log
