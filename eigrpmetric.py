# eigrpmetric.py
# calculate classic eigrp metric using bandwidth and delay as inputs
# The EIGRP classic metrtic is calculated by dividing the lowest bandwidth hop into 10^7, adding the sum of the delay along the path 
# and multiplying the result by 256.  The resulting integer is what EIGRP uses to determine the successor route.

least_bw = int(input("Enter the lowest bandwidth on the path in kbps: "))

total_delay = int(input("Enter the sum of the delay on the path in 10s of usec: " ))

metric = ((10**7/least_bw) + total_delay) * 256

print("The EIGRP metric for this path is :" + str(metric))
