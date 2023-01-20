import boto3
import json

# response= textract.analyze_id(
#     DocumentPages=[
#         {
#             "S3Object":{
#                 "Bucket": "ocr-bucket-jj",
#                 "Name": "cnh_jj.png"
#             }
#         }
#     ]
# )

# print(response)

path = "c:\\work\\capco\\aws-ocr\\data\\data_cnh_jj.json"

with open(path, encoding="utf-8") as response:
    data = json.load(response, strict=False)
    
blocks = data['IdentityDocuments'][0]['Blocks']
word = ""
line = ""

for block in blocks:
    if (block['BlockType'] == 'WORD'):
        word += block['Text'] + " Confidence: " + str(block['Confidence']) + "\n"
    elif (block['BlockType'] == 'LINE'):
        line += block['Text'] + " Confidence: " + str(block['Confidence']) + "\n"

print(word)
print("\n --------------------------------------- \n")
print(line)

# create a client for comprehend
# comprehend = boto3.client('comprehend')

# # call comprehend on the text
# response_sentiment = comprehend.detect_sentiment(
#     Text=line,
#     LanguageCode='pt'
# )

# response_entities = comprehend.detect_entities(
#     Text=line,
#     LanguageCode='pt'
# )

# print(response_sentiment)
# print("\n --------------------------------------- \n")
# print(response_entities)