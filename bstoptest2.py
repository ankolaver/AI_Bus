
with open('busstopall.txt','r') as bs:
    for element in bs:
        element = str(element)
element = element.replace(")(","),(")
print(element)
