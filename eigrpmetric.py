# eigrpmetric.py
# calculate eigrp metric using bandwidth and delay as inputs


least_bw = int(input("Enter the lowest bandwidth on the path in kbps: "))

total_delay = int(input("Enter the sum of the delay on the path in 10s of usec: " ))

metric = ((10**7/least_bw) + total_delay) * 256

print("The EIGRP metric for this path is :" + str(metric))
