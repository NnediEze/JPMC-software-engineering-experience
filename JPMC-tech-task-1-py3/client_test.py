import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2),'not equal')

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceBZero(self):
    price_a = 516.20
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b),'Stock B price is NONZERO')

  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 123.64
    self.assertEqual(getRatio(price_a, price_b), 0, 'Stock A price is NONZERO')

  def test_getRatio_greaterThan1(self):
    price_a = 346.48
    price_b = 126.59
    self.assertGreater(getRatio(price_a, price_b), 1, 'Price Ratio is LESS THAN than 1; Stock B > Stock A')

  def test_getRatio_LessThan1(self):
    price_a = 166.39
    price_b = 457.49
    self.assertLess(getRatio(price_a, price_b), 1, 'Price Ratio is GREATER THAN than 1; Stock A > Stock B')

  def test_getRatio_exactlyOne(self):
    price_a = 387.92
    price_b = 387.92
    self.assertEqual(getRatio(price_a, price_b), 1, 'Price Ratio is NOT EQUAL to 1; Stock A ≠ Stock B')

if __name__ == '__main__':
    unittest.main()
