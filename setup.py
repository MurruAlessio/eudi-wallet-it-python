import re

from glob import glob
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

_pkg_name = 'eudi_wallet_python'

with open(f'{_pkg_name}/__init__.py', 'r') as fd:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name=_pkg_name,
    version=VERSION,
    description="Python toolchain for building an OpenID4VP RP with a SATOSA backend compliant to the Italian Wallet Solution.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    url='https://github.com/italia/eudi-wallet-it-python',
    author='Giuseppe De Marco',
    author_email='demarcog83@gmail.com',
    license='License :: OSI Approved :: Apache Software License',
    # scripts=[f'{_pkg_name}/bin/{_pkg_name}'],
    packages=[f"{_pkg_name}"],
    package_dir={f"{_pkg_name}": f"{_pkg_name}"},
    package_data={f"{_pkg_name}": [
            i.replace(f'{_pkg_name}/', '')
            for i in glob(f'{_pkg_name}/**', recursive=True)
        ]
    },
    install_requires=[
        "cryptojwt>=1.8.2",
    ],
)
