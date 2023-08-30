from urllib.parse import urlparse, urlunparse
file_path = 'urls.txt'
with open(file_path, 'r') as file:
    urls = file.read().splitlines()

def remove_path_from_url(url):
    parsed_url = urlparse(url)
    cleaned_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    return cleaned_url

cleaned_urls = [remove_path_from_url(url) for url in urls]
cleaned_file_path = 'cleaned_urls.txt'
with open(cleaned_file_path, 'w') as cleaned_file:
    cleaned_file.write('\n'.join(cleaned_urls))
