def main():
    user_input = input()
    translated_input = translate_emoticons(user_input)
    print(translated_input)

def translate_emoticons(text):
    emoticon_mapping = {
        ":)": "\U0001F642",
        ":(": "\U0001F641"
    }
    for emoticon, emoji in emoticon_mapping.items():
        text = text.replace(emoticon, emoji)
    return text

if __name__ == "__main__":
    main()
