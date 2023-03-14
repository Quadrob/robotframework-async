from setuptools import setup

setup(
    name = "robotframework-async",
    version = "1.0.6",
    description = "Generic Robot Framework library for asynchronous keyword execution originally modified by René Lehfeld.",
    author = "René Lehfeld",
    author_email = "54720674+rlehfeld@users.noreply.github.com",
    license = "MIT",
    url = "https://github.com/Quadrob/robotframework-async",
    download_url = "https://github.com/Quadrob/robotframework-async",
    keywords = ["async", "robotframework"],
    install_requires = ["robotframework >= 5.0.1"],
    packages = ["AsyncLibrary"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
