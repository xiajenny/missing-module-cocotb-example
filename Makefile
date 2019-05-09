TOPLEVEL_LANG ?= verilog


PWD=$(shell pwd)
COCOTB=/Users/jennyxia/Documents/cocotb
VERILOG_SOURCES = $(PWD)/*.v
TOPLEVEL=accumulate  # the module name in your Verilog or VHDL file
MODULE=missing_adder_test  # the name of the Python test file


include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim