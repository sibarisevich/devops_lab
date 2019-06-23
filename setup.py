import setuptools

setuptools.setup(
    name="monitor",
    packages=setuptools.find_packages(),
    version="1.0",
    author="Siarhei Barysevich",
    author_email="siarhei_barysevich@epam.com",
    description="app for monitoring system info",
    license="MIT",
    install_requires=['psutil==5.6.3']
)
