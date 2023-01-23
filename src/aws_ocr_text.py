import boto3
import json
import unicodedata

######## access s3 and send data to textract
# textract = boto3.client('textract')
# # response = textract.analyze_document(
# response = textract.detect_document_text( 
#     Document={
#        'S3Object': {
#            'Bucket': 'ocr-bucket-jj',
#            'Name': 'cert_obt4.png'
#        }
#     }#,
#     #FeatureTypes=["FORMS"]
# )

# print(response)

# with open('json_data.json', 'w') as outfile:
#     json.dump(response, outfile)

######## read json generated by textract
path = "c:\\work\\capco\\aws-ocr\\data\\data_obito4.json"

with open(path, encoding="utf-8") as response:
    data = json.load(response, strict=False)
    
blocks = data['Blocks']
word = ""
line = ""

for block in blocks:
    if (block['BlockType'] == 'WORD'):
        word += block['Text'] + " "
    elif (block['BlockType'] == 'LINE'):
        line += block['Text'] + ' - Confidence: ' + "{:.2f}".format(block['Confidence']) + "%" + "\n"

# Normalize encode text
word = unicodedata.normalize('NFC', word)
line = unicodedata.normalize('NFC', line)

print(word)
print("\n --------------------------------------- \n")
print(line)

######## send data to aws comprehend
# create a client for comprehend
# comprehend = boto3.client('comprehend')

# # call comprehend on the text
# # response_sentiment = comprehend.detect_sentiment(
# #     Text=line,
# #     LanguageCode='pt'
# # )

# response_entities = comprehend.detect_entities(
#     Text=line,
#     LanguageCode='pt',

# )

# # print(response_sentiment)
# print("\n --------------------------------------- \n")
# print(response_entities)