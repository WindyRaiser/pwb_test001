
# def avg(data, start = 0, end = None):
#     print("the value end is ",end)
#     if not end: 
#         end = len(data)
#     # return sum(data[start:end]) / float(end-start)
#     print(sum(data[start:end]) / float(end-start))
#     return sum(data[start:end]) / float(end-start)

# d = (3,5,7,9,11)

# print("avg(d,1,4) is ",avg(d,1,4))
# print("avg(d,2) is ",avg(d,2))
# print("avg(d) is ",avg(d))
# print("avg(d,2,0) is ",avg(d,2,0))
# print("avg(d,0,None) is ",avg(d,0,None))

# new_var = print("avg(d,1,4) is ",avg(d,1,4))
# new_var

def avg(data, start = 0, end = None):
    if not end:   # (not None) == True,  
        end = len(data)
    return sum(data[start:end]) / float(end-start)

d = (3,4,5,6,7,8)


print(avg(d,1,4))   # 답 5

print(avg(d,2))     # 답  26/4 = 6.5

print(avg(d))       # 답  5.5

print(d[0:2])         # 답 (3,4)
print(d[1:4])         # 답 (4,5,6)
print(d[2:4])         # 답 (5,6)
print(d[3:5])         # 답 (6,7)

