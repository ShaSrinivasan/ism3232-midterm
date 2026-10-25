#businessrules.py
#Business rules for Cooper Kettle Coffee Roasters
#Organization: Cooper Kettle Coffee Roasters
#Name: Sharath Srinivasan

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """   Returns the bean cost before any discount (rule 1). """
    
    total_cost =  bags * bag_price
    return total_cost

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """   Returns the discount rate as a decimal, so 9% is 0.09 (rules 2 and 3).   """

    discount = 0.00
    if bags >=80:
        discount =.14 #14% discount for 80 or more bags
    elif bags >= 20:
        discount = 0.09 # 9% discount for 20-79 bags

    if partner and bags >= 20:
        discount += 0.04 # Additional 4% discount for partners when ordering 20 or more bags

    return discount

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """   Returns the shipment total for one shipment: the discounted cost, plus the shipping fee when it applies (rule 4). It must call your first two functions. """

    total_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    shipment_total = total_cost * (1 - discount)

    if shipment_total < 250:
        shipment_total += 35.00 # Add $35 shipping fee for orders under $250

    return shipment_total

def requires_prepayment(total: float) -> bool:
    """   Determine if prepayment is required based on the total shipment cost.  """
    
    if total >= 1500.0:
        return True
    else:
        return False

def needs_pallet(bags: int, total: float) -> bool:
    """   	Returns True when the shipment needs a freight pallet (rule 6), otherwise False.  """
    if bags >= 60 and total >= 700.0:
        return True
    else:
        return False

def total_shipped(shipments: list) -> float:
    """   Returns the sum of the shipment totals for every shipment in the list. It must use a for loop that calls calculate_shipment_total.  """
    sum = 0.0
    for shipment in shipments:
        bag_price, bags, partner = shipment
        sum += calculate_shipment_total(bag_price, bags, partner)
    return round(sum, 2)  # Round to two decimal places

def largest_shipment(shipments: list) -> str:
    """Returns the buyer of the shipment with the largest shipment total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls calculate_shipment_total."""
    largest_total = 0.0
    largest_buyer = ""
    for shipment in shipments:
        buyer, bag_price, bags, partner = shipment
        shipment_total = calculate_shipment_total(bag_price, bags, partner)

        if shipment_total > largest_total:
            largest_total = shipment_total
            largest_buyer = buyer

    return largest_buyer

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """ Returns one line of the report, such as Uptown Bakery: $175.00 | prepayment: no | pallet: no. Each True/False value is shown as yes or no, and the amount always has two decimal places. """
    prepayment_str = "yes" if prepayment else "no"
    pallet_str = "yes" if pallet else "no"
    return f"{buyer}: ${total:.2f} | prepayment: {prepayment_str} | pallet: {pallet_str}"