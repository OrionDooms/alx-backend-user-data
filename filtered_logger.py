#!/usr/bin/env python3
"""Filtering log"""
import re


def filter_datum(fields, redaction, message, separator):
    """The filter_datum function returns the log message obfuscated.
    Obfuscation is the process of disguising confidential or sensitive data."""
    a = r"(" + '|'.join(fields) + r")=([^" + separator + "]*)"
    return re.sub(a, r"\1=" + redaction, message)
