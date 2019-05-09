module accumulate (
  input clk,
  input rst,
  input en,
  input [31:0] i_in,
  output reg [31:0] o_out
);

wire [31:0] sum;

adder adder_inst(
  .clk(clk),
  .A (i_in),
  .B (o_out),
  .o_adder(sum)
);

always @ (posedge clk) begin
  if (rst == 1'b1) begin
    o_out <= 32'b0;
  end
  else if (en == 1'b1) begin
    o_out <= sum;
  end
end

endmodule
