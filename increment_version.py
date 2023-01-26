"""increments a minor version number for setup.py
loads and stores it in VERSION file

use:
    on building module
    python setup.py bdist_wheel
    python -m increment_version

    in setup.py
    setup(
        ...
        version=open('VERSION').read()
    )

"""

from packaging.version import parse, Version

FILE_NAME = 'VERSION'

with open(FILE_NAME, 'r', encoding='utf8') as f:
    raw_string = f.read()

version = parse(raw_string)
initial_version = version
if version.is_devrelease:
    print('this is a dev-release. incrementing only revisions')
    dev_rev = version.dev+1
    result_version = Version(version.base_version+'dev'+str(dev_rev))
if not version.is_prerelease:
    print('this is a release. incrementing only micro')
    micro = version.micro+1
    result_version = Version(f'{version.major}.{version.minor}.{micro}')

print(f'{initial_version}->{result_version}')

with open(FILE_NAME, 'w', encoding='utf8') as f:
    raw_string = f.write(str(result_version))

    