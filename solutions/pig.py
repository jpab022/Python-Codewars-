def pig_it(text):
    seperated = text.split(" ")
    text = ""
    for i in seperated:
        if i not in "!@#$%^&*()-_+=?":
            first = i[0]
            i = i.replace(first,"",1)
            i+=first
            i+="ay"
        text+=i
        text+=" "
    text = text.rstrip()
    return text
