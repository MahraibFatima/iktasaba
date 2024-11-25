thought = input("what is Answer to the Great Question Of Life, the Universe and Everything? ")
thought = thought.strip()
thought = thought.lower()

if(thought == '42' or thought == 'forty-two' or thought == 'forty two'):
    print("Yes")
else:
    print("No")
