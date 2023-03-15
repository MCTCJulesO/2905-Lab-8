import unittest
from unittest.mock import patch, MagicMock
from bitcoin_converter import (
    get_bitcoin_amount, 
    convert_bitcoin_to_dollars, 
    display_results
)


class TestBitcoinConverter(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_get_bitcoin_amount(self, mock_input):
        # Test that the get_bitcoin_amount function returns the expected value (1.0)
        bitcoin = get_bitcoin_amount()
        self.assertEqual(bitcoin, 1.0)

    @patch('builtins.input', return_value='-1\n2')
    def test_get_bitcoin_amount_with_invalid_input(self, mock_input):
        # Test that the get_bitcoin_amount function raises a SystemExit exception when an invalid input is provided
        with self.assertRaises(SystemExit):
            get_bitcoin_amount()

    @patch('bitcoin_converter.get_bitcoin_data', return_value={
        'bpi': {
            'USD': {
                'rate_float': 50000.00
            }
        }
    })
    def test_convert_bitcoin_to_dollars(self, mock_get_bitcoin_data):
        # Test the convert_bitcoin_to_dollars function with three different amounts of bitcoin
        bitcoin = 1
        dollars = convert_bitcoin_to_dollars(bitcoin)
        self.assertEqual(dollars, 50000.00)

        bitcoin = 0.5
        dollars = convert_bitcoin_to_dollars(bitcoin)
        self.assertEqual(dollars, 25000.00)

        bitcoin = 0
        dollars = convert_bitcoin_to_dollars(bitcoin)
        self.assertEqual(dollars, 0)

    @patch('sys.stdout', new_callable=MagicMock)
    def test_display_results(self, mock_stdout):
        # Test the display_results function by checking that the correct string is printed to stdout
        bitcoin = 1
        dollars = 50000.00
        display_results(bitcoin, dollars)
        mock_stdout.assert_called_with('1 bitcoin is equal to $50000.0\n')

    @patch('sys.stdout', new_callable=MagicMock)
    @patch('builtins.input', return_value='1')
    @patch('bitcoin_converter.get_bitcoin_data', return_value={
        'bpi': {
            'USD': {
                'rate_float': 50000.00
            }
        }
    })
    def test_main(self, mock_get_bitcoin_data, mock_input, mock_stdout):
        # Test the main function by mocking the input and get_bitcoin_data functions, and checking that the correct output is printed to stdout
        main()
        mock_get_bitcoin_data.assert_called_once()
        mock_input.assert_called_once_with('Enter the number of bitcoin: ')
        mock_stdout.assert_called_with('1 bitcoin is equal to $50000.0\n')


if __name__ == '__main__':
    unittest.main()
