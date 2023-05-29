import json
from urllib import request
url = "https://opentdb.com/api.php?amount=10&type=boolean"

response = request.urlopen(url)
data = json.loads(response.read())

question_data = data['results']
