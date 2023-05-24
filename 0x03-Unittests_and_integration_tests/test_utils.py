#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, returned):
        """
        Test the access_nested_map function with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), returned)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, ret_error):
        """
        Test that a KeyError is raised when accessing a non-existent
        key in a nested map.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(ret_error, str(error.exception))


class TestGetJson(unittest.TestCase):
    """Test class for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test the get_json function by mocking the requests.get
        method and its response.
        """
        response = mock.Mock()
        response.json.return_value = payload

        with mock.patch('requests.get', return_value=response):
            request = get_json(url)
            self.assertEqual(request, payload)
            response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator"""

    def test_memoize(self):
        """
        Test the memoize decorator by mocking a method and
        checking that it is only called once.
        """

        class TestClass:
            """Test class"""

            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """Test memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            returned = test_class.a_property
            returned = test_class.a_property

            self.assertEqual(returned, 42)
            patched.assert_called_once()


if __name__ == '__main__':
    unittest.main()
