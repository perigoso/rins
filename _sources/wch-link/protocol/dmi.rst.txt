``0x08`` DMI
============

DMI access commands

DMI access
----------

.. table:: Table 1 - DMI access cmd

	+-------------+---------+--------+-----------+
	| Byte        | 0       | 1 .. 4 | 5         |
	+=============+=========+========+===========+
	| Description | address | data   | operation |
	+-------------+---------+--------+-----------+

.. table:: Table 2 - DMI access response

	+-------------+---------+--------+--------+
	| Byte        | 0       | 1 .. 4 | 5      |
	+=============+=========+========+========+
	| Description | address | data   | status |
	+-------------+---------+--------+--------+

The logic follows the standard DMI access protocol

Address
~~~~~~~

Address of the DMI register to access.

Data
~~~~

Data to write to the DMI register.

Operation
~~~~~~~~~

Desired operation:

- NOP: ``0x00``
- READ: ``0x01``
- WRITE: ``0x02``

Status
~~~~~~

Result of the operation:

- SUCCESS: ``0``
- FAILURE: ``2``
- TOO_SOON: ``3``


.. toctree::
	:maxdepth: 2
	:hidden:
