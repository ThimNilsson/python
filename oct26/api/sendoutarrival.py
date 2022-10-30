import requests

def get(postal_code):
    api_uri = "https://portal.postnord.com/api/sendoutarrival/closest?postalCode="
    return requests.get(f"{api_uri}{postal_code}")
