from rest_framework.views import APIView
import time
import threading
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils import SerlizerValidation
from .serializer import userAddListSerializer
from .models import Notification

messages = []
def event_stream():
    while True:
             
        if messages:
            msg = messages.pop(0)
            yield f"data: {msg}\n\n"

        # yield "event: heartbeat\ndata: keep-alive\n\n"
        time.sleep(2)    

# def event_stream():
#     while True:
#         yield f"event: heartbeat\ndata: alive\n\n"
#         import time; time.sleep(2)

class SSEAPI(APIView):
    " new sse API Endpoint"
    permission_classes=[IsAuthenticated]

    def get(self,request):
        response = StreamingHttpResponse(event_stream(),content_type = "text/event-stream")
        response['Cache-Control'] = 'no-cache'
        # response['X-Accel-Buffering'] = 'no'
        return response 

class SSETriger(APIView):
    
    def post(self,request):
        data = request.data.get("message" , "no message provided")
        messages.append(data)
        return Response({'status':'queued','data':data})
    
class UserAddListView(APIView ,SerlizerValidation ):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        user_id = user.id
        print("user id",user_id)
        request.data['user_id'] = user_id
        serializer = userAddListSerializer(data = request.data)

        
        if not serializer.is_valid():
            return self.return_response(status.HTTP_400_BAD_REQUEST ,"Invalid data",data=serializer.errors)
        serializer.save()
        # data = request.data.get({"message":serializer.data},{ "error":"no message provided"})
        messages.append(serializer.data)
        Notification.objects.create(message=serializer.data , user_id=user_id)
        return self.return_response(status.HTTP_201_CREATED ,"User Add List created successfully",data=serializer.data)
