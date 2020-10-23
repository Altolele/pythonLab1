import re
from itertools import groupby

pattern = r"\@[a-zA-Z0-9_-]+?\.[a-zA-Z]{2,6}"

inputFile = open('emails.txt', 'r')
result = inputFile.read()
result = re.findall(pattern, result)
result.sort()
result = [el for el, _ in groupby(result)]
resultFile = open('result.txt', 'w')
for line in result:
    print(line)
    resultFile.write(line)
    resultFile.write('\n')

inputFile.close()
resultFile.close()
