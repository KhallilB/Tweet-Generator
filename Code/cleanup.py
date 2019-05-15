import string


def cleanup(source):
    source_text = source.lower()
    source_text = source.replace('-', ' ')
    source_text = '\u0391 ' + source_text.replace('.', ' \u03a9 \u0391 ')

    translation = str.maketrans(dict.fromkeys(
        string.punctuation + '\u201c\u201d\u2018\u2019'))
    translated_text = source_text.translate(translation)

    return translated_text
