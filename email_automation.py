import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# Function to send an email
def send_email():
    # Email details
    sender_email = "your_email@example.com"  # Replace with your email
    receiver_email = "recipient@example.com"  # Replace with recipient's email
    password = "your_email_password"  # Replace with your email password

    # Email content
    subject = "Daily Report"
    body = "This is your daily report.\n\nRegards,\nYour Automation Script"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    # Connect to the email server
    try:
        server = smtplib.SMTP("smtp.example.com", 587)  # Replace with your SMTP server and port
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Log in to your email account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

# Schedule the email to be sent daily at a specific time
schedule.every().day.at("08:00").do(send_email)  # Replace with desired time (24-hour format)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
