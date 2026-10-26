# Test for business rules for Cooper Kettle Coffee Roasters
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


def test_calculate_bean_cost():
    assert calculate_bean_cost(10.0, 5) == 50.0
    assert calculate_bean_cost(12.5, 3) == 37.5
    assert calculate_bean_cost(15.0, 0) == 0.0


def test_get_bulk_discount_zero_discount():
    assert get_bulk_discount(19) == 0.0


def test_get_bulk_discount_nine_percent_discount():
    assert get_bulk_discount(20) == 0.09


def test_get_bulk_discount_fourteen_percent_discount():
    assert get_bulk_discount(80) == 0.14


def test_get_bulk_discount_partner_discount():
    assert get_bulk_discount(25, partner=True) == 0.13
    assert get_bulk_discount(100, partner=True) == 0.18


def test_get_bulk_discount_partner_no_discount():
    assert get_bulk_discount(19, partner=True) == 0.0


def test_calculate_shipment_total_with_shipping_fee():
    assert calculate_shipment_total(83, 3) == 284  # 249 + 35 shipping


def test_calculate_shipment_total_without_shipping_fee():
    assert calculate_shipment_total(25.0, 10) == 250.0  # 250 and no shipping


def test_calculate_shipment_total_with_discount():
    assert calculate_shipment_total(15.0, 20) == 273.0  # 300 - 9% discount
    assert calculate_shipment_total(15.0, 80) == 1032.0  # 1200 - 14% discount


def test_calculate_shipment_total_with_discount_and_partner():
    assert (
        calculate_shipment_total(15.0, 25, partner=True) == 326.25
    )  # (375 - (375 * (0.09 + 0.04)))


def test_calculate_shipment_total_with_discount_and_not_partner_matters():
    assert (
        calculate_shipment_total(12.0, 20, partner=False) == 253.4
    )  # (260 - (260 * 0.09)) with no shipping fee


def test_calculate_shipment_total_with_discount_and_shipping_fee_partner_matters():
    assert (
        calculate_shipment_total(13.0, 20, partner=True) == 261.2
    )  # (260 - (260 * (0.09 + 0.04))) + shipping


def test_requires_prepayment_almost_threshold():
    assert requires_prepayment(1499.99) == False


def test_requires_prepayment_at_threshold():
    assert requires_prepayment(1500.00) == True


def test_requires_prepayment_above_threshold():
    assert requires_prepayment(2000.00) == True


def test_needs_pallet():
    assert needs_pallet(50, 600.0) == False  # 50 < 60


def test_needs_pallet_bags_yes_total_no():
    assert needs_pallet(60, 699.0) == False  # 699.0 < 700.0


def test_needs_pallet_bags_no_total_yes():
    assert needs_pallet(59, 700.0) == False  # 59 < 60


def test_needs_pallet_bags_yes_total_yes():
    assert needs_pallet(60, 700.0) == True  # 60 >= 60 and 700.0 >= 700.0


def test_total_shipped():
    shipments = [(10.0, 5, False), (12.5, 3, False), (15.0, 20, False)]
    assert total_shipped(shipments) == 430.5


def test_largest_shipment():
    shipments = [
        ("Buyer A", 15.0, 20, False),
        ("Buyer B", 12.5, 3, False),
        ("Buyer C", 15.0, 10, False),
    ]
    assert largest_shipment(shipments) == "Buyer A"


def test_largest_shipment_tie():
    shipments = [
        ("Buyer A", 15.0, 20, False),
        ("Buyer B", 12.5, 3, False),
        ("Buyer C", 15.0, 20, False),
    ]
    assert largest_shipment(shipments) == "Buyer A"


def test_format_shipment_line_prepayment_yes_pallet_no():
    assert (
        format_shipment_line("Buyer A", 100.0, True, False)
        == "Buyer A: $100.00 | prepayment: yes | pallet: no"
    )


def test_format_shipment_line_prepayment_no_pallet_yes():
    assert (
        format_shipment_line("Buyer B", 200.0, False, True)
        == "Buyer B: $200.00 | prepayment: no | pallet: yes"
    )


def test_format_shipment_line_prepayment_yes_pallet_yes():
    assert (
        format_shipment_line("Buyer C", 300.0, True, True)
        == "Buyer C: $300.00 | prepayment: yes | pallet: yes"
    )


def test_format_shipment_line_prepayment_no_pallet_no():
    assert (
        format_shipment_line("Buyer D", 400.0, False, False)
        == "Buyer D: $400.00 | prepayment: no | pallet: no"
    )
