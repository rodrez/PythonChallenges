def domain_name(url):
    clean_url = url.replace('https://','').replace('http://','').replace('www.','')
    dot = clean_url.index('.')
    if dot == 3:
        clean_url = clean_url[4:]
    else:
        dot = clean_url.index('.')
        clean_url = clean_url[:dot]
    return clean_url
