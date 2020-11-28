import base64
import requests
import json

def vision_api_ocr(image_file, api_key=""):
    with open(image_file, 'rb') as image:
        #base64にエンコード
        base64_image = base64.b64encode(image.read()).decode()

    url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(api_key)
    header = {'Content-Type': 'application/json'}
    #パラメータの設定
    body = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                #typeを変化させることによって顔検出、ラベル検出などができる
                #参照：https://cloud.google.com/vision/docs/?hl=ja
                'type': 'TEXT_DETECTION',
                'maxResults': 1,
            }]

        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    # jsonで吐き出し    response
    # fw = open('vision_response.json','w')
    # json.dump(response,fw,indent=4)

    # print("responseの値は?" + str(response))
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    return text

# imgの画像ファイルのあるPATHは皆様の環境に合わせて変更してください。
img = "/static/images/ichika.png"
key = "Google Cloud PlatformのKey"
data = vision_api_ocr(img, key)
print(data)
