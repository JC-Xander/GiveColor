from setuptools import setup, find_packages

setup(
    name='GiveColor',
    version='0.1.0',
    author='JC-Xander',
    author_email='j.xanderoficial@gmail.com',
    description='Un paquete para imprimir texto de colores en la terminal de Windows',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JC-Xander/GiveColor',
    download_url='https://github.com/JC-Xander/GiveColor/archive/refs/tags/0.1.0.zip',
    keywords=['Color', 'Terminal', 'font'],
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    python_requires='>=3.6',
)
