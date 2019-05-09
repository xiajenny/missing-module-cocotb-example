import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import ReturnValue

@cocotb.coroutine
def do_clock(dut):
    dut.clk = 0
    yield Timer(500)
    dut.clk = 1
    yield Timer(500)

@cocotb.coroutine
def do_reset(dut):
    dut.rst = 1
    yield do_clock(dut)
    dut.rst = 0

@cocotb.coroutine
def get_signal(clk, signal):
    yield RisingEdge(clk)
    raise ReturnValue(signal.value)

@cocotb.coroutine
def adder_sim(dut):
  print("Inside adder simulation coroutine")
  while True:
    i_add = yield get_signal(dut.clk, dut.i_in)
    o_add = yield get_signal(dut.clk, dut.o_out)
    print("Adder input:", i_add, "Reg out:", o_add)
    sum = i_add + o_add
    dut.adder_inst.o_adder <= sum
    print("Sum:", sum)
    yield Timer(1500)
    print("Adder out:", dut.adder_inst.o_adder.value)

@cocotb.test()
def missing_adder_test(dut):
    """Missing adder test"""
    yield do_reset(dut)
    dut.en = 1
    dut.i_in = 1
    yield Timer(1500)
    print("init in:", dut.i_in.value)
    print("init out:", dut.o_out.value)

    dut._log.info("Running test!")
    
    cocotb.fork(Clock(dut.clk, 1000).start())
    cocotb.fork(adder_sim(dut))

    yield Timer(15000)

    dut._log.info("Done running test!")