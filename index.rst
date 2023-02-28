RINS WCH DTMs RE Project
========================

What is RINS
-------------

RINS is the WCH custom DTMs (Debug Transport Module) documentation and RE project.

What does this provide
----------------------

This project provides the documentation on the RVSWD DTM protocol used by WCH Risc-V microcontrollers.
It documents the physical and logic layers of the protocol with the intention of providing a clean source of documentation for 3rd party implementations.

The goal is to allow for a full Open-Source implementation of program and debug tooling for these chips thereby eliminating the need/reliance on out of tree and proprietary vendor tools for FOSS projects.

What does RINS stand for
------------------------

- R VSWD
- I s
- N ot
- S WD

Because it is not SWD.

It also means Kidneys in Portuguese, because having to deal with these protocols feels like getting punched in the kidneys.

.. toctree::
	:hidden:
	:caption: Contents:
	:maxdepth: 2

	wch-link/index
	rvswd/index
	sdi/index

.. toctree::
	:hidden:
	:maxdepth: 2
	:caption: Meta:

	license
	contributors
