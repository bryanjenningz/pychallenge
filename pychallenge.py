import urllib.request
import re


def c0():
    """Find 2 to the 38th power."""
    return 2**38


def c1(message):
    """Unencrypt the message. K -> M, O -> Q, E -> G. Shift to the right 2.
    url: """
    def unencrypt(message):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for letter in message:
            if letter in alphabet:
                result += alphabet[(alphabet.index(letter) + 2) % len(alphabet)]
            else:
                result += letter
        return result
    return unencrypt(message)


def c2(url):
    """Find the secret message in the source code of the page.
    url: www.pythonchallenge.com/pc/def/ocr.html"""
    source = urllib.request.urlopen(url).read().decode('utf-8')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    source = source[source.index('%%$'):]
    for character in source:
        if character in alphabet:
            result += character
    return result


def c3(url):
    """One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    url: http://www.pythonchallenge.com/pc/def/equality.html"""
    result = ''
    pattern = r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}'
    source = urllib.request.urlopen(url).read().decode('utf-8')
    matches = re.findall(pattern, source)
    result = ''.join(matches)
    return result
    
