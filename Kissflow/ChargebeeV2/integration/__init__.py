import os

import chargebee


def configure():
    api_key = os.getenv("API_KEY", "test_wNf487LcucBdOJIwCCML0GI8s8ZfuF69H")
    site = os.getenv("SITE", "orangscape-test")

    chargebee.configure(api_key, site)
