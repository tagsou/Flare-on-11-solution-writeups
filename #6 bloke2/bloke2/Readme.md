
For this challenge we given a verilog project that supposed to involve a reimplemeting of the BLAKE2 hash function. 
verilog is a hardware langauge which is something im not familar with at all but the readme included in the folder and chatgpt lol helped alot in understanding how to approach the challange.

**Note** with this challenge it was very confusing at first to me and
There was alot of messing around. the solution turned out to be a very simple, it was a single line of code change to reveal the flag.

while messying around I was looking in the **data_mgr.v** file and found something that stuck out to me.

```localparam TEST_VAL = 512'h3c9cf0addf2e45ef548b011f736cc99144bdfee0d69df4090c8a39c520e18ec3bdc1277aad1706f756affca41178dac066e4beb8ab7dd2d1402c4d624aaabe40;```

this is a 512 bit hex value which I thought must contain the flag! this value gets used later in what seems to be a loop.

```
	always @(posedge clk) begin
		if (rst) begin 
			out_cnt <= 0;
		end else begin
			//$display("%t dmgr dout oc %h", $time, out_cnt);
			if (h_rdy) begin
				//$display("%t dmgr dout h %h t %b", $time, h_in, tst);
				out_cnt <= W;
				h <= h_in ^ (TEST_VAL & {(W*16){tst}});
			end else if(out_cnt != 0) begin
				//$display("%t dmgr dout d %h dv %b de %b oc %h", $time, data_out, dv_out, data_end, out_cnt);
				out_cnt <= out_cnt - 1;
				h <= {8'b0, h[W*8-1:8]};
```


Let’s break down the code. The value TEST_VAL is combined with a modified variable tst using a bitwise AND. From the definition, tst is a reg tst, so it’s a single-bit value by default. This setup means:

```
If tst is 0, the line simplifies to h <= h_in.
   If tst is 1, it changes to h <= h_in ^ TEST_VAL.
```
The challenge description suggests that the solution involves the “testbenches,” which likely means tst should be 1. we can now just modify the code so that it always executes as ```h <= h_in ^ TEST_VAL```.

running the makefile after the change....gets the flag!

