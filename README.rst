RobotFramework AsyncLibrary
=======================

Short Description
-----------------
Generic Robot Framework library for asynchronous keyword execution originally modified by René Lehfeld.

Installation
============
Install the library from GitHub using pip:

::

    pip install "git+https://github.com/Quadrob/robotframework-async.git"

Usage
=====

#) Import into a test suite with:

.. code:: robotframework

    Library AsyncLibrary

#) To run a keyword asynchronously:

.. code:: robotframework

    ${handle}    Async Run    some keyword    first argument    second argument

#) To retrieve the return value, a blocking call to async_get is called with the handle:

.. code:: robotframework

    ${return_value}    Async Get    ${handle}
