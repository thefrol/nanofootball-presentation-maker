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

file_name='VERSION'

versions:list[str]=open(file_name,'r').read().split('.')
root,major,minor=(int(item) for item in versions)
minor=minor+1

updated_version_string=f'{root}.{major}.{minor}'

open(file_name,'w').write(updated_version_string)