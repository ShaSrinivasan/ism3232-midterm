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

