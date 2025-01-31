import unittest
from norm_cpu_power import parse_power_data

class TestPowerDataParsing(unittest.TestCase):
    def test_valid_power_value(self):
        lines = [
            "c298: #Avg.LastHour=390 W | 1331 Btu/hr\n",
            "c298: Cap.Watts=430 W\n"
        ]
        df = parse_power_data(lines)
        self.assertEqual(len(df), 2)
        self.assertIn("390 W", df["Value"].values)
        self.assertIn("430 W", df["Value"].values)

    def test_invalid_power_value(self):
        lines = [
            "c298: Cap.Enable=Disabled\n",
            "c298: #Cap.ActivePolicy.BtuHr=N/A\n"
        ]
        df = parse_power_data(lines)
        self.assertEqual(len(df), 0)

    def test_embedded_unit(self):
        lines = [
            "c298: Cap.BtuHr=1468 btu/hr\n"
        ]
        df = parse_power_data(lines)
        self.assertEqual(len(df), 0)

    def test_malformed_input(self):
        lines = [
            "c298: InvalidFormat\n",
            "\n",  # Empty line
            "c298: #Avg.LastHour=InvalidValue\n"
        ]
        df = parse_power_data(lines)
        self.assertEqual(len(df), 0)

    def test_edge_cases(self):
        lines = [
            "c298: #Avg.LastHour=390\n",  # No W
            "c298: Cap.Watts=430 W\n"
        ]
        df = parse_power_data(lines)
        self.assertEqual(len(df), 1)
        self.assertIn("430 W", df["Value"].values)

if __name__ == "__main__":
    unittest.main()
