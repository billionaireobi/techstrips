from django.shortcuts import render,redirect
from django.conf import settings


from django.core.mail import EmailMessage

def homepage(request):
    if request.method == "POST":
        # Collect form data
        message_name = request.POST.get('message_name', '').strip()
        message_email = request.POST.get('message_email', '').strip()
        message_subject = request.POST.get('message_subject', '').strip()
        message_message = request.POST.get('message_message', '').strip()

        # Validate form data
        if not (message_name and message_email and message_subject and message_message):
            return render(request, "index.html", {
                "success": False,
                "error": "All fields are required."
            })

        # Create HTML email content
        email_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                }}
                .content {{
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                h1 {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <div class="content">
                <h1>New Message from {message_name}</h1>
                <p><strong>Email:</strong> {message_email}</p>
                <p><strong>Subject:</strong> {message_subject}</p>
                <p><strong>Message:</strong><br>{message_message}</p>
            </div>
        </body>
        </html>
        """

        # Send the email
        try:
            email = EmailMessage(
                subject=f"Contact Page Message: {message_subject}",
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,
                to=['eugineosoroobiero@gmail.com'],
            )
            email.content_subtype = "html"  # Specify the email content type as HTML
            email.send()

            # Redirect to the homepage with a success flag
            return redirect(f"/?success=1&name={message_name}")
        except Exception as e:
            print(f"Error sending email: {e}")
            return render(request, "index.html", {
                "success": False,
                "error": "Failed to send email. Please try again later."
            })

    # Check for success flag in GET request
    success = request.GET.get('success', '') == '1'
    message_name = request.GET.get('name', '')

    return render(request, "index.html", {
        "success": success,
        "message_name": message_name,
    })

# def homepage(request):
#     if request.method == "POST":
#         message_name = request.POST.get('message_name')
#         message_email = request.POST.get('message_email')
#         message_subject = request.POST.get('message_subject')
#         message_message = request.POST.get('message_message')
        
#         data= {
#             'message_name': message_name,
#             'message_email': message_email,
#             'message_subject': message_subject,
#             'message_message': message_message,
#         }
#         message = '''
#         New message: {}
#         From: {}
#         '''.format(data['message_message'], data['message_email'])
#         send_mail(data['message_subject'], message, '', ['eugineosoroobiero@gmail.com'])
#         return render(request, "index.html", {"message_name":message_name,"success": True})       

#     return render(request, "index.html", {"success": False})
