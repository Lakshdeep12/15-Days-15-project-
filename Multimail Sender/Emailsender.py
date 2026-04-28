import smtplib as sp 

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        server = sp.SMTP('smtp.gmail.com', 587) 
        server.starttls()
        server.login(sender_email, sender_password)
        
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender_email, recipient_email, message)
        
        server.quit()   
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")    

# Example usage
sender_email = "user@gmail.com"
sender_password = "your_password"  # ⚠️ avoid hardcoding passwords
recipient_email = "recipient@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python." 

send_email(sender_email, sender_password, recipient_email, subject, body)