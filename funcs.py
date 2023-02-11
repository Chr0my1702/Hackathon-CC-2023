def auto_format(text, max_length=45, separator=' '):
    words = text.split(separator)
    new_text = ''
    line_length = 0
    for word in words:
        if line_length + len(word) > max_length:
            new_text += '\n'
            line_length = 0
        new_text += word + separator
        line_length += len(word) + 1
    return new_text
