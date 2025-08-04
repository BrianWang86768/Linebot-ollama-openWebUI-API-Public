import requests
import time

def chat_with_model(token, uesr_text):
    #計算回覆時間 coting response time
    start_time = time.time()

    #OpenWebUI API URL
    url = 'https://YOUR_OPENWEBUI_URL/api/chat/completions'

    # OpenWebUI API headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # OpenWebUI API request body
    data = {
      "model": "YOUR_MODEL_NAME",# Replace with your actual model name
      "messages": [
        {
          "role": "user",
          "content": uesr_text
        }
      ]
    }

    response = requests.post(url, headers=headers, json=data)
    end_time = time.time()
    execution_time = end_time - start_time
    print("程式執行時間：", execution_time, "秒")
    if (response.status_code == 200):
      return response.json()
    else:
      return "error"


def Connect_to_model(uesr_text):
    #OpenWebUI token
    token = 'YOUR_OPENWEBUI_TOKEN'  # Replace with your actual OpenWebUI token
    
    #呼叫Chat_with_model並攜帶token與訊息
    response = chat_with_model(token, uesr_text)

    #偵錯回傳是否為error 否則回應訊息 是則回應伺服器維護
    if(response != "error"):
        httpresponse = response["choices"][0]["message"]["content"]
        return httpresponse
    else:
        httpresponse = "伺服器維護中，請稍後再試。"
        return httpresponse
