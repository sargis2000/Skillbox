import requests
import re
x = requests.get('http://www.columbia.edu/~fdc/sample.html').text.split('\n')

x = [i for i in x if i.startswith('<h3') and i.endswith('h3>')]
x = [re.search(r'>(.*?)<', i).group()[1:-1] for i in x]
print(x)
