``0x0d`` System
===============

System commands

``0x01`` - Get Version
----------------------

Returns the version of the probe.

.. table:: Table 1 - Get Version cmd

	+-------------+-------+
	| Byte        | 0     |
	+=============+=======+
	| Description | 0x01  |
	+-------------+-------+

.. table:: Table 2 - Get Version response

	+-------------+-------+-------+----+
	| Byte        | 0     | 1     | 2  |
	+=============+=======+=======+====+
	| Description | major | minor | id |
	+-------------+-------+-------+----+

Major/Minor
~~~~~~~~~~~

Major and minor version of the probe, ``major.minor``.

ID
~~

Probe ID code

Extracted strings from official toolchain:

- ``0x01``: WCH-Link-CH549 (RV)

- ``0x02``: WCH-LinkE-CH32V307 (RV)

- ``0x03``: WCH-LinkS-CH32V203 (RV)

- ``0x04``: WCH-LinkB (RV)

``0x02`` - Connect
------------------

.. table:: Table 3 - Connect cmd

	+-------------+-------+
	| Byte        | 0     |
	+=============+=======+
	| Description | 0x02  |
	+-------------+-------+

.. table:: Table 4 - Connect response

	+-------------+---------+
	| Byte        | 0 .. 3  |
	+=============+=========+
	| Description | CHIP ID |
	+-------------+---------+

On error the response is of group  ``0x55`` `Error`_ with still unknown format

CHIP ID
~~~~~~~

The chip ID of the connected chip. MSB first.


``0x03`` - Unknown
------------------

no clue.

``0x04`` - Get Memory Info
--------------------------

RAM size, flash size, addr.

``0xff`` - Close
----------------

Terminate connection (unsure what this does)

.. toctree::
	:maxdepth: 2
	:hidden:

.. _Error: error.html
