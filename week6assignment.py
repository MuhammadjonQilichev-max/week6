# You are a real estate analyst comparing property listings.
#  The data is available as a list of tuples, 
# where each tuple contains a (listing_id, neighborhood, price, area_in_sqft).
#  Your objective is to create a Python script to analyze the real estate market.

def calculate_price_per_sqft(listing_tuple):
    id = listing_tuple[0]
    neighborhood = listing_tuple[1]
    price = listing_tuple[2]
    area = listing_tuple[3]
    return (price / area)

def find_best_value_listing(listings):
    best_listing  = None
    best_value = None
    for item in listings:
        id = item[0]
        price = item[2]
        area = item[3]
        value = price/area

        if best_value is None:
            best_value = value
            best_listing = id
        elif value < best_value:
                best_value = value
                best_listing = id
        elif value == best_value and id < best_listing:
             best_listing =id
    return best_listing    

def get_listings_in_neighborhood(listings, neighborhood_name):
     result = []
     for item in listings:
          id = item[0]
          neighborhood = item[1]
          if neighborhood == neighborhood_name:
               result.append(id)
     result.sort()
     return result

def get_neighborhood_value_summary(listings):
    totals = {}
    for item in listings:
         neighborhood = item[1]
         price = item[2]
         if neighborhood not in totals:
              totals[neighborhood] = 0

         totals[neighborhood] += price

    summary = []
    for name in sorted(totals):
         summary.append((name, totals[name]))
    return summary

def analyze_listings(listings):
    best_value = find_best_value_listing(listings)
    riverside_listings = get_listings_in_neighborhood(listings, "Riverside")
    neighborhood_summary = get_neighborhood_value_summary(listings)
    return (best_value, riverside_listings, neighborhood_summary)


listings = [
    ('L101', 'Downtown', 500000, 800),    # PPSF: 625.0
    ('L205', 'Riverside', 450000, 1000),   # PPSF: 450.0
    ('L102', 'Downtown', 750000, 1200),   # PPSF: 625.0
    ('L301', 'Northwood', 350000, 900),    # PPSF: 388.88
    ('L206', 'Riverside', 600000, 1250)    # PPSF: 480.0
]

print(analyze_listings(listings))
# Expected Output:
# ('L301', ['L205', 'L206'], [('Downtown', 1250000), ('Northwood', 350000), ('Riverside', 1050000)])