from rest_framework.response import Response


class SerlizerValidation:
    def return_response(self , status ,message , data = None):
        response_data = {
            "status":status,
            "message":message,
        }
        if data :
            response_data["data"] = data
        return Response(status=status , data=response_data)    
    

    def custom_response(self, status,message,**kwargs):
        response_data={
            "status":status,
            "message": message,
            **kwargs
        }
        return Response(status=status ,data= response_data)