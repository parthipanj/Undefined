import os

import chargebee


def configure():
    api_key = os.getenv("API_KEY", "")
    site = os.getenv("SITE", "")

    chargebee.configure(api_key, site)
