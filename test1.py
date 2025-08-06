import time
f1=open("a1.txt","w")
L1=["1001\n","mobile_1\n","23000\n","samsung\n"]
L2=["1002\n","mobile_2\n","24000\n","samsung\n"]
L3=["1003\n","mobile_3\n","25000\n","samsung\n"]
L4=["1004\n","mobile_4\n","26000\n","samsung\n"]
f1.writelines(L1)
f1.writelines(L2)
f1.writelines(L3)
f1.writelines(L4)
print("A file is created sucessfully:")
print()
f1.close()
print()
time.sleep(2)
print("end of an application")