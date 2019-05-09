// Adder DUT
module adder (
    input             clk,
    input      [31:0] A,
    input      [31:0] B,
    output reg [31:0] o_adder
);

  assign o_adder = 0;
  // assign o_adder = A + B;

endmodule
