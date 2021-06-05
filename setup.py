from distutils.core import setup

setup(
    name='pyloki',
    packages=['pyloki'],
    version='0.2.0',
    license='MIT',
    description='A scalable logging module and client for Grafana Loki',
    author='Ashish Shekar',
    author_email='ashishshekar15@gmail.com',
    url='https://github.com/codekidX/pyloki',
    download_url='https://github.com/codekidX/pyloki/archive/v_01.tar.gz',
    keywords=['python', 'loki', 'grafana', 'logging', 'metrics'],
    install_requires=[
        'requests',
        'pytz',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
