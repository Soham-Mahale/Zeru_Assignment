import json
import csv

def json_to_csv(file_path,sample):
    # Load the JSON (single user record)
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract only the actionData field

    attributes_dict=[]

    for i in data:
        attributes_dict.append(i['actionData'])

    attributes=list(str())

    for j in attributes_dict:
        for l in dict(j).keys():
            if l not in attributes:
                attributes.append(l)
    if sample==1:
        with open('sample.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=attributes)
            writer.writeheader()
            writer.writerows(attributes_dict)

    else:
        with open('user_wallet.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=attributes)
            writer.writeheader()
            writer.writerows(attributes_dict)

# For sample Data keep sample value True its set as default
json_to_csv(file_path="user-wallet-transactions.json",sample=True)