from rest_framework.response import Response
from django.core.mail import send_mail


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
    


class EmailUtils:
    @staticmethod
    def send_email(subject, message, recipient_list, html_message=None):
        try:
            email_from = "rajnagani3131@gmail.com"
            send_mail(subject, message, email_from,recipient_list, html_message=None)
            return True
        except Exception as e:
            print(str(e))
            return False

    @staticmethod
    def welcom_email(email,firstname):
        subject = f"Welcome To With JWT"
        message =f"""
            Welcom to JWT {firstname} 

            You face any Problem so you send mail here
"""
        recipient_list =[email]
        return EmailUtils.send_email(subject , message,recipient_list)
