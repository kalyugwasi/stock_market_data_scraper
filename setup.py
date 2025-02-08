from setuptools import setup, find_packages

setup(
    name='stock_market_data_scraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'run_nse_bse_scraper=stock_market_data_scraper.data_acquisition.scrapers.nse_bse_scraper:main', # Example entry point - we can define a main function later if needed
        ],
    },
)