import unittest
from datetime import datetime
from datetime import date

symbol = "GOOGL"
charttype = "1"
time_series = "2"
date_format = date_format = "%Y-%m-%d"
start_date = "2002-01-01"
end_date = "2002-01-01"

class symbolTest(unittest.TestCase):
    def test_capitalized(self):
        self.assertTrue(symbol.isupper())
    def test_num(self):
        self.assertTrue(len(symbol) <= 7 and len(symbol) >=1)
    def test_alpha(self):
        self.assertTrue(symbol.isalpha())
class chartTest(unittest.TestCase):
    def test_numeric(self):
        self.assertTrue(charttype.isnumeric() and len(charttype) == 1)
    def test_oneortwo(self):
        self.assertTrue(charttype == "1" or charttype == "2") 
class timeseries(unittest.TestCase):
    def test_numeric(self):
        self.assertTrue(time_series.isnumeric() and len(time_series) == 1)
    def test_onethroughfour(self):
         self.assertTrue(time_series == "1" or time_series == "2" or time_series == "3" or time_series == "4")
class startdate(unittest.TestCase):
    def test_datetype(self):
        self.assertTrue(datetime.strptime(start_date, date_format))
class enddate(unittest.TestCase):
    def test_datetype(self):
        self.assertTrue(datetime.strptime(end_date, date_format))

if __name__ == "__main__":
    unittest.main()