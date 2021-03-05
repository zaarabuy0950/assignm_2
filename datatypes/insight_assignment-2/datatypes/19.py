a=input("ente a number:")
asd=a.split()
for i  in range(len(asd)):
    asd[i]=int(asd[i])
print(min(asd))