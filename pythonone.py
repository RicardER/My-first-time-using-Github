#THIS CODE TO THE PUT BACKWARD A PHRASE
my_message = "Bonjour à tous mes amis, et au revoir"
my_space = ""
b = len(my_message)
for i in range(b):
    my_space += my_message[(b-1)-i]
    print(my_space)