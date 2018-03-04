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
    return bool(match)

def test_telephone(telephone):
    match = re.match(r'^0[1-9]([-. ]?[0-9]{2}){4}$',telephone)
    return bool(match)

