# python-args2fields

Parses args & kwargs to instance fields (attributes)

## Table of Contents

- [Setup](#setup)
- [Examples](#examples)
- [License](#license)

## Setup

```bash
# assumption: you're working on project with pipenv
pipenv shell
pipenv install -e git+https://github.com/hankadler/python-args2fields#egg=args2fields
```

## Examples

```python
import sys
import pandas as pd
from args2fields import args2fields


class Dummy:
    def __init__(self):
        pass


def main(*args):
    fields = pd.DataFrame(
        index=['name', 'age', 'occupation'],
        data={'types': [str, int, str]}
    )

    instance = Dummy()

    argv = ('--name', 'hank', '--age', '32', '--occupation', 'entrepreneur')
    args2fields(instance, fields, *argv)

    for k,v in instance.__dict__.items():
        print(f'{k}: {v} [{type(v)}]')


if __name__ == '__main__':
    main(*sys.argv[1:])
```

## License

[MIT](LICENSE)
