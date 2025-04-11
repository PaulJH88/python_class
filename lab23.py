import sys
import math, random

responses = []
for line in sys.stdin:
    response = line.rstrip()
    if "done" == response:
        break
    else:
        responses.append(response)


r_num = random.randint(1, len(responses[0]))

sqrt_r_num = math.sqrt(r_num)
r_num_pwr = math.pow(r_num, len(responses[1]))
r_num_close = math.remainder(100, r_num)

print(sqrt_r_num)
print(r_num_pwr)
print(r_num_close)






# response = ""
#     while response != "done":
#         response = line.rstrip()
#         responses.append(len(response))
#     else:
#         break

# 