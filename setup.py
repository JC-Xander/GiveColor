from setuptools import setup, find_packages

setup(
    name='colore',
    version='0.1.0',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Un paquete para imprimir texto en colores en la terminal',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/tu_proyecto',  # Cambia esto a tu repositorio
    packages=find_packages(),
    install_requires=[],  # Agrega dependencias si es necesario
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
