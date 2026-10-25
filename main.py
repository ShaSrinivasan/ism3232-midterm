#ISM 3232 Midterm main.py
#Main program for Cooper Kettle Coffee Roasters
from business_rules import calculate_bean_cost, get_bulk_discount, calculate_shipment_total, requires_prepayment, needs_pallet, total_shipped, largest_shipment, format_shipment_line


shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]

print('Copper Kettle Coffee Roasters - Shipment Report')
for shipment in shipments:
    buyer = shipment["buyer"]
    bag_price = shipment["bag_price"]
    bags = shipment["bags"]
    partner = shipment["partner"]

    total_cost = calculate_bean_cost(bag_price, bags)
    discount_rate = get_bulk_discount(bags, partner)
    shipment_total = calculate_shipment_total(bag_price, bags, partner)
    prepayment_required = requires_prepayment(shipment_total)
    pallet_needed = needs_pallet(bags, shipment_total)
    print(format_shipment_line(buyer, shipment_total, prepayment_required, pallet_needed))

