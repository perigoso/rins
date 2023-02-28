WCH-Link
========

WCH-Link is USB debbuger tool by WCH for flashing and debugging WCH RISC-V and ARM microcontrollers.

The WCH-Link has two modes of operation, DAPLink and RV (i.e. RISC-V).

This documentation refers to the RV mode of operation only, changing the mode of operation is also out of scope.

Device Descriptors
------------------

.. table:: Table 1 - Device Descriptors

	+--------------+--------------+---------------------------------+
	| Vendor ID    | 0x1a86       | QinHeng Electronics             |
	+--------------+--------------+---------------------------------+
	| Product ID   | 0x8010       |                                 |
	+--------------+--------------+---------------------------------+
	| Manufacturer | wch.cn       |                                 |
	+--------------+--------------+---------------------------------+
	| Product      | WCH-Link     |                                 |
	+--------------+--------------+---------------------------------+
	| Serial       | 0001A0000000 | Same serial accross all devices |
	+--------------+--------------+---------------------------------+

.. include:: usb_descriptors
	:literal:

Endpoints
~~~~~~~~~

The WCH-Link exposes 4 endpoints through a Vendor interface:

- 0x82:  EP 2 IN
- 0x02:  EP 2 OUT
- 0x81:  EP 1 IN
- 0x01:  EP 1 OUT

EP 2 IN/OUT is used for most of the communication, EP 1 IN/OUT is used for some flash related operations.

Protocol
--------

.. table:: Table 2 - Command packet format

	+-------------+--------+--------------+--------------+----------+
	| Byte        | 0      | 1            | 2            | 3 .. End |
	+=============+========+==============+==============+==========+
	| Description | Header | Command Page | Command Size | Command  |
	+-------------+--------+--------------+--------------+----------+

Header
~~~~~~

Fixed header byte:
- 0x81 for host command packets
- 0x82 for device response packets

Command Page
~~~~~~~~~~~~

Command page/group, used to identify how the command data will be interpreted.

Command Size
~~~~~~~~~~~~

Length in bytes of the remaining command data.

Command
~~~~~~~

Command data, interpreted according to the command page.

Command Pages
-------------

- ``0x02`` `Flash`_
- ``0x06`` `Flash protection`_
- ``0x08`` `DMI`_
- ``0x0d`` `System`_
- ``0x0e`` `Debug`_
- ``0x55`` `Error`_

.. _Flash: protocol/flash.html
.. _Flash protection: protocol/flash_prot.html
.. _DMI: protocol/dmi.html
.. _System: protocol/system.html
.. _Debug: protocol/debug.html
.. _Error: protocol/error.html

.. toctree::
	:maxdepth: 2
	:hidden:

	protocol/index
