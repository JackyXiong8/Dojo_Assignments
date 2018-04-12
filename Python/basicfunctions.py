

days = {"Monday":["Sucks","fire"],
        "Tuesday":"Bit less",
        "Wednesday":"Okay-ish",
        "Thursday":"Almost there",
        "Friday":"Its Friday!"}


month = {"weeks":[{"numbers":1,"text":"Hello there, how are you"},
                {"numbers":2,"text":"Hello, welcome"},
                {"numbers":3,"text":"Hi there"}]}

for key, data in month.items():
    for information in data:
        print ("hello", information["numbers"], information["text"])

        
        