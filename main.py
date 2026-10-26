# ISM 3232 Midterm main.py
# Main program for Cooper Kettle Coffee Roasters
# Organization: Cooper Kettle Coffee Roasters
# Name: Sharath Srinivasan

from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)

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

print("Copper Kettle Coffee Roasters - Shipment Report")
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
    print(
        format_shipment_line(buyer, shipment_total, prepayment_required, pallet_needed)
    )

print("Shipments:", len(shipments))
print(
    "Total shipped: ${:.2f}".format(
        total_shipped([(s["bag_price"], s["bags"], s["partner"]) for s in shipments])
    )
)
print(
    "Average shipment total: ${:.2f}".format(
        round(
            total_shipped(
                [(s["bag_price"], s["bags"], s["partner"]) for s in shipments]
            )
            / len(shipments),
            2,
        )
    )
)
print(
    "Largest shipment:",
    largest_shipment(
        [(s["buyer"], s["bag_price"], s["bags"], s["partner"]) for s in shipments]
    ),
)
print(
    "Prepayments required:",
    sum(
        1
        for s in shipments
        if requires_prepayment(
            calculate_shipment_total(s["bag_price"], s["bags"], s["partner"])
        )
    ),
)
print(
    "Pallets needed:",
    sum(
        1
        for s in shipments
        if needs_pallet(
            s["bags"], calculate_shipment_total(s["bag_price"], s["bags"], s["partner"])
        )
    ),
)
