# Initialize dependencies with `git submodule update --init --recursive`
# Run install.py to install

from setuptools import setup

setup(
    name='awsmfunc',
    version='0.1.0',
    url='https://git.concertos.live/AHD/awsmfunc',
    author='AHD',
    package_dir={
        'awsmfunc': 'awsmfunc',
        'adjust': 'dependencies/adjust',
        'adptvgrnMod': 'dependencies/adptvgrnMod',
        'edi_rpow2': 'dependencies/edi_rpow2',
        'fvsfunc': 'dependencies/fvsfunc',
        'havsfunc': 'dependencies/havsfunc',
        'kagefunc': 'dependencies/kagefunc',
        'muvsfunc': 'dependencies/muvsfunc',
        'mvsfunc': 'dependencies/mvsfunc',
        'nnedi3_resample': 'dependencies/nnedi3_resample',
        'nnedi3_rpow2': 'dependencies/nnedi3_rpow2',
        'rekt': 'dependencies/rekt/rekt',
        'vsTAAmbk': 'dependencies/vsTAAmbk',
        'vsutil': 'dependencies/vsutil',
    },
    packages=[
        'awsmfunc',
        'adjust',
        'adptvgrnMod',
        'edi_rpow2',
        'fvsfunc',
        'havsfunc',
        'kagefunc',
        'muvsfunc',
        'mvsfunc',
        'nnedi3_resample',
        'nnedi3_rpow2',
        'rekt',
        'vsTAAmbk',
        'vsutil',
    ],
)
