#Test for business rules for Cooper Kettle Coffee Roasters
#Organization: Cooper Kettle Coffee Roasters
#Name: Sharath Srinivasan

from business_rules import calculate_bean_cost, get_bulk_discount, calculate_shipment_total, requires_prepayment, needs_pallet, total_shipped, largest_shipment, format_shipment_line

def test_calculate_bean_cost():
    assert calculate_bean_cost(10.0, 5) == 50.0
    assert calculate_bean_cost(12.5, 3) == 37.5
    assert calculate_bean_cost(15.0, 0) == 0.0

def test_get_bulk_discount():
    assert get_bulk_discount(19) == 0.0
    assert get_bulk_discount(20) == 0.09
    assert get_bulk_discount(80) == 0.14
    assert get_bulk_discount(25, partner=True) == 0.13
    assert get_bulk_discount(100, partner=True) == 0.18

def test_calculate_shipment_total():
    assert calculate_shipment_total(83,3) == 284  # 249 + 35 shipping
    assert calculate_shipment_total(25.0,10) == 250.0  # 250 and no shipping
    assert calculate_shipment_total(12.5, 3) == 72.5  # 37.5 + 35 shipping
    assert calculate_shipment_total(15.0, 20) == 273.0  # 300 - 9% discount
    assert calculate_shipment_total(15.0, 80) == 1032.0  # 1200 - 14% discount
    assert calculate_shipment_total(12.4,20) == 260.68 # 248 - 9% discount + 35 shipping
    assert calculate_shipment_total(12.4, 20, partner=True) == 250.76 # 248 - (248 * (0.09 + 0.04)) with no shipping fee
    assert calculate_shipment_total(15.0, 25, partner=True) == 326.25  # (375 - (375 * (0.09 + 0.04))) + shipping

def test_requires_prepayment():
    assert requires_prepayment(1499.99) == False
    assert requires_prepayment(1500.00) == True
    assert requires_prepayment(2000.00) == True

def test_needs_pallet():
    assert needs_pallet(50, 600.0) == False # 50 < 60
    assert needs_pallet(60, 699.0) == False # 699.0 < 700.0
    assert needs_pallet(59, 700.0) == False # 59 < 60
    assert needs_pallet(60, 700.0) == True # 60 >= 60 and 700.0 >= 700.0

def test_total_shipped():
    shipments = [(10.0, 5, False), (12.5, 3, False), (15.0, 20, False)]
    assert total_shipped(shipments) == 430.5

def test_largest_shipment():
    shipments = [("Buyer A", 15.0,20, False), ("Buyer B", 12.5, 3, False), ("Buyer C", 15.0, 20, False)]
    assert largest_shipment(shipments) == "Buyer A"

def test_format_shipment_line(): 
    assert format_shipment_line("Buyer A", 100.0, True, False) == "Buyer A: $100.00 | prepayment: yes | pallet: no"
    assert format_shipment_line("Buyer B", 200.0, False, True) == "Buyer B: $200.00 | prepayment: no | pallet: yes"
    assert format_shipment_line("Buyer C", 300.0, True, True) == "Buyer C: $300.00 | prepayment: yes | pallet: yes"
    assert format_shipment_line("Buyer D", 400.0, False, False) == "Buyer D: $400.00 | prepayment: no | pallet: no"
