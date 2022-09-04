#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parses args & kwargs to instance fields (attributes).

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


from getopt import gnu_getopt


def args2fields(instance: object, fields: dict, *args, defaults={}, **kwargs):
    """Parses `args` and `kwargs` to `instance` `fields`.

    `args` should be used for passing command-line arguments, while
    `kwargs` for passing API parameters. Should both be used, the latter
    overrides the former.

    Parameters:
        instance (object): An instance of a class.
        fields (dict):
            names (str): Field name.
            types (obj): Type field should be.
        defaults (dict):
            names (str): Field name.
            value (obj): Default value for field.
        *args (tuple): Command-line argument(s).
        **kwargs (dict): Keyword argument(s) denoting field-value pairs.
    """
    names = []
    values = []

    # Parses `args`.
    if args:
        longopts = []
        for name in fields.keys():
            longopts.append(f'{name.replace("_", "-")}=')

        opts = gnu_getopt(args, '', longopts)[0]

        for name, value in opts:
            names.append(name.replace('--', '').replace('-', '_'))
            values.append(value)

    # Sets `instance` `name` field to `value` of `type_` type.
    for name, value in list(zip(names, values)):
        type_ = fields[name]
        if type_ is bool:
            value = str2bool(value)
        elif type_ is list:
            value = value.split()
        else:
            value = type_(value)
        setattr(instance, name, value)

    # Parses `kwargs`, potentially overriding args.
    for name, value in kwargs.items():
        setattr(instance, name, value)

    # Sets instance field to default value if needed.
    for name, value in defaults.items():
        if not hasattr(instance, name):
            setattr(instance, name, value)


def str2bool(string):
    """Casts `string` as `bool` the way you'd expect."""
    if string.strip().lower() in ['0', 'false']:
        return False
    else:
        return bool(string)


if __name__ == '__main__':
    pass
