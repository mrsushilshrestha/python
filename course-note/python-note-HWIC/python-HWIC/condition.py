light=input("Enter the Current light Status:")
if light=="red":
    print("stop")
elif light=="yellow":
    print("look")
elif light=="green":
    print("go")
else:
    print("Light is broken")