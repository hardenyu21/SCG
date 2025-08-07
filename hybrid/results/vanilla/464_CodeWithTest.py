import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    def custom_encoder(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    return json.dumps(my_obj, default=custom_encoder)

# Example usage:
# print(task_func({'name': 'Alice', 'age': 30}))
# print(task_func({'name': 'Alice', 'age': 30, 'balance': Decimal('100.50'), 'timestamp': datetime.now()}))
import unittest
from datetime import datetime
from decimal import Decimal
import pytz  # Assuming pytz is used for timezone information in datetime objects
class TestCases(unittest.TestCase):
    def test_datetime_serialization(self):
        """Ensure datetime objects are serialized to an ISO 8601 string."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc)}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)
    def test_decimal_serialization(self):
        """Verify Decimal objects are serialized to their string representation."""
        obj = {'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('99.99', result)
    def test_combined_serialization(self):
        """Test serialization of a complex object containing both datetime and Decimal."""
        obj = {'time': datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc), 'price': Decimal('99.99')}
        result = task_func(obj)
        self.assertIn('2023-01-01T12:00:00+00:00', result)
        self.assertIn('99.99', result)
    def test_simple_object_serialization(self):
        """Check serialization of simple key-value pairs."""
        obj = {'name': 'Alice', 'age': 30}
        result = task_func(obj)
        self.assertEqual(result, '{"name": "Alice", "age": 30}')
    def test_null_serialization(self):
        """Ensure that `None` is correctly serialized as `null`."""
        obj = {'value': None}
        result = task_func(obj)
        self.assertEqual(result, '{"value": null}')
    def test_list_serialization(self):
        """Test serialization of a list containing mixed data types."""
        obj = {'list': [datetime(2023, 1, 1, 12, 0, tzinfo=pytz.utc), Decimal('99.99'), None]}
        result = task_func(obj)
        self.assertIn('"2023-01-01T12:00:00+00:00"', result)
        self.assertIn('99.99', result)
        self.assertIn('null', result)
    def test_unsupported_type(self):
        """Test that attempting to serialize an unsupported type raises an error."""
        class CustomObject:
            pass
        obj = {'custom': CustomObject()}
        with self.assertRaises(TypeError):
            task_func(obj)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)