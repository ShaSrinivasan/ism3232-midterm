#businessrules.py
#Business rules for Cooper Kettle Coffee Roasters
def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """   Calculate the total cost of coffee beans based on the price per bag and the number of bags purchased.  """

    total_cost = bag_price * bags
    return total_cost

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """   Calculate the bulk discount based on the number of bags purchased and whether the customer is a partner.  """

    discount = 0.00
    if bags >=80:
        discount =.14 #14% discount for 80 or more bags
    elif bags >= 20:
        discount = 0.09 # 9% discount for 20-79 bags

    if partner and bags >= 20:
        discount += 0.04 # Additional 4% discount for partners when ordering 20 or more bags

    return discount

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """   Calculate the total shipment cost after applying bulk discounts.  """

    total_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    shipment_total = total_cost * (1 - discount)

    if shipment_total < 250:
        shipment_total += 35.00 # Add $35 shipping fee for orders under $250

    return shipment_total

def requires_prepayment(shipment_total: float) -> bool:
    """   Determine if prepayment is required based on the total shipment cost.  """
    
    if shipment_total < 1500:
        return True
    else:
        return False