from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
    name='mysterybot',
    version='0.0.1',
    author='nyarmith',
    description='A discord bot for managing task-oriented communities',
    long_description=readme,
    packages=setuptools.find_packages(),
    install_requires=requirements,

    entry_points={
        'console_scripts': [
            'community_gm_bot=community_gm_bot.launcher:main',
        ],
    },

    scripts=[
    ]
)
