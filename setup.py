from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-pep8>=1',
]

setup(
    name='WindWhisper',
    version='0.0.1',
    extras_require={
        'test': test_deps,
    },
    install_requires=[
        "longling>=1.3.1"
    ],  # And any other dependencies foo needs
    entry_points={
    },
)