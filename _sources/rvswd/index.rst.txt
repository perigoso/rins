RVSWD
=====

Note: there seems to exist multiple variations of the RISC-V SWD protocol, lets call them short packet and long packet, this document describes the long packet version only for now.

RVSWD is the name of the proprietary two-wire debug protocol/DTM on WCH's RISC-V MCUs.

Similar to ARM's SWD interface, RWSWD has two wires named DIO and CLK respectively, but the protocol is not compatible.

This protocol basically exposes(addr+data+op/status) the dmi (0x11) register of DTM (Debug Transport Module) in a typical JTAG implementation.

Characteristics
---------------

- CLK and DIO idle high
- Protocol is half-duplex
- Protocol uses packet formating
- DIO falling egde while CLK is idle high marks a START condition
- DIO rising edge while CLK is idle high marks a STOP condition
- DIO is updated in the CLK low phase
- Bits and bytes are sent MSB first
- Bits are sampled in the CLK rising edge
- Data polarity is standard (0 is low, 1 is high)
- Data integrity is verified via parity bits
- A transaction is always initiated by the host (the debugger)
- PThe protocol is point-to-point, there's no target addressing

Format
------

.. table::

	+-------------+-------+---------+------+-----------+--------+---------+--------+--------+--------+------+
	| Type        | START | Address | Data | Operation | Parity | Address | Data   | Status | Parity | STOP |
	+=============+=======+=========+======+===========+========+=========+========+========+========+======+
	| Source 	  | Host  | Host    | Host | Host      | Host   | Target  | Target | Target | Target | Host |
	+-------------+-------+---------+------+-----------+--------+---------+--------+--------+--------+------+
	| Length(bit) | 0 	  | 7       | 32   | 2         | 1      | 7       | 32     | 2      | 1      | 0    |
	+-------------+-------+---------+------+-----------+--------+---------+--------+--------+--------+------+

First parity (Host) is odd parity of Address, Data and Operation field.
Second parity (Target) is even parity of Address, Data and Status field.

Wakeup
------

CLK and DIO idle high the debbuger sends 100 clock strobes with DIO high, and a STOP condition(DIO low, CLK high, DIO rising edge).

.. toctree::
	:maxdepth: 2
	:hidden:
