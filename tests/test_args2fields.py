#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests args2fields module.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import unittest

from args2fields import args2fields


class TestCase1(unittest.TestCase):
    def setUp(self):
        self.fields = {
            'name': str,
            'age': int,
            'weight': float,
            'employed': bool,
            'colors': list,
        }

    def test_args_parse(self):
        argv = (
            '--name', 'hank',
            '--age', '32',
            '--weight', '220.5',
            '--employed', '0',
            '--colors', 'red blue'
        )

        args2fields(self, self.fields, *argv)

        expected = ['hank', 32, 220.5, False, ['red', 'blue']]
        results = [self.name, self.age, self.weight, self.employed,
                   self.colors]

        print('--- test_args_parse ---')
        print(f'Expected = {expected}')
        print(f'Results = {results}')
        print()

        self.assertEqual(results, expected)

    def test_types(self):
        argv = (
            '--name', 'hank',
            '--age', '32',
            '--weight', '220.5',
            '--employed', '0',
            '--colors', 'red blue'
        )

        args2fields(self, self.fields, *argv)

        expected = list(self.fields.values())
        fields = [self.name, self.age, self.weight, self.employed, self.colors]
        results = [type(field) for field in fields]

        print('--- test_types ---')
        print(f'Expected = {expected}')
        print(f'Results = {results}')
        print()

        self.assertEqual(results, expected)

    def test_kwargs_parse_1(self):
        kwargs = {
            'name': 'hank',
            'age': 32,
            'weight': 220.5,
            'employed': False,
            'colors': ['red', 'blue']
        }

        args2fields(self, self.fields, **kwargs)

        expected = ['hank', 32, 220.5, False, ['red', 'blue']]
        results = [self.name, self.age, self.weight, self.employed,
                   self.colors]

        print('--- test_kwargs_parse_1 ---')
        print(f'Expected = {expected}')
        print(f'Results = {results}')
        print()

        self.assertEqual(results, expected)

    def test_kwargs_parse_2(self):
        args2fields(self, self.fields, name='hank', age=32, weight=220.5,
                    employed=False, colors=['red', 'blue'])

        expected = ['hank', 32, 220.5, False, ['red', 'blue']]
        results = [self.name, self.age, self.weight, self.employed,
                   self.colors]

        print('--- test_kwargs_parse_2 ---')
        print(f'Expected = {expected}')
        print(f'Results = {results}')
        print()

        self.assertEqual(results, expected)

    def test_parse_kwargs_w_defaults (self):
        kwargs = {
            'name': 'hank',
            'weight': 220.5,
            'colors': ['red', 'blue']
        }

        defaults = {
            'name': '',
            'age': 0,
            'weight': 0.0,
            'employed': False,
            'colors': []
        }

        args2fields(self, self.fields, defaults=defaults, **kwargs)

        expected = ['hank', 0, 220.5, False, ['red', 'blue']]
        results = [self.name, self.age, self.weight, self.employed,
                   self.colors]

        print('--- test_parse_kwargs_w_defaults ---')
        print(f'Expected = {expected}')
        print(f'Results = {results}')
        print()

        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
