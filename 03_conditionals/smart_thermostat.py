device_status = "active"
temperature = 20

if device_status == "active":
    if temperature >35:
        print("HIgh temperature alrert")
    else:
        print("Temperature is normal")
else:
    print("Device is inactive")   