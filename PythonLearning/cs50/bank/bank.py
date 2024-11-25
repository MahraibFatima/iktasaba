greeting = input("Greeting: ").strip()
greeting_lower = greeting.lower()

if greeting_lower == "hello" or greeting_lower == "hello, newman":
    print("$0")
elif greeting_lower == "how you doing?":
    print("$20")
elif greeting_lower == "what's happening?" or greeting_lower == "what's up?":
    print("$100")
