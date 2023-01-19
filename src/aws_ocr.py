import boto3
import json

# textract = boto3.client('textract')
# response = textract.detect_document_text(
#    Document={
#        'S3Object': {
#            'Bucket': 'ocr-bucket-jj',
#            'Name': 'rg.png'
#        }
#     }
# )

#print(response)

path = "c:\\work\\capco\\aws-ocr\\data\\data_obito1.json"

with open(path, encoding="utf-8") as response:
    data = json.load(response, strict=False)
    

blocks = data['Blocks']
word = ""
line = ""

for block in blocks:
    if (block['BlockType'] == 'WORD'):
        word += block['Text'] + " "
    elif (block['BlockType'] == 'LINE'):
        line += block['Text'] + " "

print(word)
print("\n --------------------------------------- \n")
print(line)