cim_rpm = 2655                   # with 337 Watt
stage1 = 12 / 60
stage2 = 14 / 84
output = 2655 * stage1 * stage2  # should be 96 rpm for 1 m/s

print(f"The gocart rpm on the axle is {output} rpm.")
