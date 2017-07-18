import json
import urllib.request
import urllib
import csv


def ballJSON(json_str):
    data = json.loads(json_str)
    json_data = []
    for m in data:
        json_temp = m[2]
        json_data.append(json_temp)

    with open('ball.csv', 'w') as f:
        csvwriter = csv.writer(f, dialect=("excel"))

        for m in data:
            temp_data = []

            temp_data1 = []
            temp_data1.append(m[0])

            temp_data2 = []
            temp_data2.append(m[1])

            temp_data = temp_data1 + temp_data2 + m[2]

            csvwriter.writerow(temp_data)
        print(temp_data)

    saveStr = json.dumps(json_data)
    with open('ball.json', 'w') as f:
        json.dump(saveStr, f)
    print(json_data)




def resolveJSON(json_str):
    data = json.loads(json_str)
    json_data = []
    for m in data:
        json_temp = {
            'no' : m[1],
            'time' : m[0],
            'balldata' :  m[2]
        }
        json_data.append(json_temp)


    saveStr = json.dumps(json_data)
    with open('balltime.json', 'w') as f:
        json.dump(saveStr, f)
    print(json_data)
    print('json_data',len(json_data))






if __name__=='__main__':
    with open('data.json', 'r') as f:
        data = json.load(f)
        resolveJSON(data)
        # ballJSON(data)