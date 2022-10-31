import api

def main():
    print("\nThis application will tell you the next delivery date by post nord to a specific postal code.\n")
 
    postal_code = input("Please enter a postal code: ")
    lookup = api.sendoutarrival.get(postal_code)
    status_code = lookup.status_code
    json_data = lookup.json()

    if status_code != 200:
        print("The request failed")
        print(json_data)
        exit(1)

    delivery = json_data["delivery"]
    if(delivery == "N/A"):
        print("No delivery found. Please check the input.")
        exit(1)

    print("\nNext delivery to postal code", json_data["postalCode"],  "in",  json_data["city"], "will be", json_data["delivery"], "\n" ) 


if __name__ == '__main__':
    main()

