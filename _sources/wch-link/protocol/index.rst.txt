Protocol
========

All commands noted include the header commnad page and command size bytes already, this highlights the data payload only.

The protocol seems to work with MSB first, so the first byte is the most significant byte.

.. toctree::
	:maxdepth: 2

	0x02 - Flash <flash>
	0x06 - Flash protection <flash_prot>
	0x08 - DMI <dmi>
	0x0d - System <system>
	0x0e - Debug <debug>
	0x55 - Error <error>
