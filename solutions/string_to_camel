def to_camel_case(text):
    for x in text:
        if x == '-' or x == '_':
            y = text.index(x)
            text = text[:y] + text[y+1:]
            text = text[:y] +text[y].upper()+ text[y+1:]
    return text
