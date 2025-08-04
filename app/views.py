from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from .services.ai_chat import ai_chat
from .services.OpenWebUIAPI import Connect_to_model



line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_SECRET_KEY)

#測試介面
def sayhello(request):
    return HttpResponse("Hello Django!")

#直接回傳使用者訊息
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

#與ollama建立連線對話
@csrf_exempt
def line_bot_webhook(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                user_message = event.message.text
                ai_response = ai_chat(user_message)  # 呼叫 Ollama 對話回應

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=ai_response)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

#與Open Web UI建立連線對話
@csrf_exempt
def OpenWebUI_webhook(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                
                user_message = event.message.text
                ai_response = Connect_to_model(user_message)  #OpenWebUI做回應
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=ai_response)
                )
        return HttpResponse(status = 200)
            
    else:
        return HttpResponseBadRequest()
