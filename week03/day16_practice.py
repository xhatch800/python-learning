"""Day 16 — Key Standard Library Modules (Part 1)

Topics: os, sys, json, datetime, re
"""
import os
import sys
import re
import json
from datetime import datetime


# write two functions:
#
# get_env(key, default=None) — returns the value of an environment variable,
# or default if it's not set. Use os.environ.get().
#
# script_info() — returns a dict with two keys:
#
# "python_version" → the first 6 characters of sys.version (e.g. "3.14.0")
# "argv" → sys.argv as-is

def get_env(key, default=None):
    return os.environ.get(key, default)


def script_info():
    return {
        "python_version": re.sub(r" \(.*", "", sys.version),
        "argv": sys.argv
    }


# write two functions:
#
# serialize_user(name, age, tags) — takes a name (str), age (int),
# and tags (list of str), returns a JSON string with those three fields. Use json.dumps.
#
# parse_config(json_str) — takes a JSON string, returns the parsed dict.
# If the string is invalid JSON, catch the exception and return None.
# Hint: json.loads raises json.JSONDecodeError on bad input.

def serialize_user(name: str, age: int, tags: list[str]) -> str:
    return json.dumps({
        "name": name,
        "age": age,
        "tags": tags
    })


def parse_config(json_str: str):
    try:
        result = json.loads(json_str)
    except json.JSONDecodeError as err:
        print(f"Json Error: {err.msg}: {json_str}")
    else:
        return result


# write two functions:
#
# format_date(dt, fmt="%Y-%m-%d") — takes a datetime object,
# returns it formatted as a string using fmt.

# days_until(target_date) — takes a date object, returns the number
# of days from today until that date as an int. Negative
# if the date is in the past.
#
# Hint: subtracting two date objects gives a timedelta —
# check what attribute gives you the day count.

def format_date(dt: datetime, fmt="%Y-%m-%d"):
    return dt.strftime(fmt)


def days_until(target_date: datetime, now=None):
    now = datetime.now() if now is None else now
    diff = target_date - now
    return diff.days


# write two functions:
#
# extract_emails(text) — takes a string, returns a list of all email addresses
# found in it. A simple pattern is fine: word chars/dots/hyphens before @, domain after.
#
# mask_phone(text) — takes a string containing a US phone number in the
# format XXX-XXX-XXXX, returns the string with the number
# replaced by ***-***-XXXX (mask all but the last 4 digits).
#
# Example: "Call me at 415-555-1234 please" → "Call me at ***-***-1234 please"

def extract_emails(text: str):
    return re.findall(r"[\w.\-]+@[\w.\-]+", text)


def mask_phone(text: str):
    match = re.match(r"(.*)(\d{3})+[- ]?(\d{3})+[- ]?(\d{4})(.*)", text)
    return f"{match[1]}***-***-{match[4]}{match[5]}" if match else None
