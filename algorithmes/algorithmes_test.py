import re

def test_code_postal(code_postal):
    if len(code_postal) == 5:
        return True
    else:
        return False

def test_mail(mail):
    match = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail)
    return bool(match)

def test_url(url):
    match = re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',url)
    return (match)

