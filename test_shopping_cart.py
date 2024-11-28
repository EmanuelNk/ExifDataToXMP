from shopping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    cart = ShoppingCart(3)
    cart.add("item1")
    assert cart.size() == 1
    assert cart.get_items() == ["item1"]

def test_added_items_are_in_cart():
    cart = ShoppingCart(3)
    cart.add("item1")
    cart.add("item2")
    assert cart.size() == 2
    assert cart.get_items() == ["item1", "item2"]

def test_overfill_cart():
    cart = ShoppingCart(5)
    for i in range(5):
        cart.add(f"item{i}")
    with pytest.raises(OverflowError):
        cart.add("item6")
       
    