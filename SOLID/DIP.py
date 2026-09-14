#Dependency Inversion Principle

from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str):
        pass

#Concrete Implementation
class GmailClient(EmailClient):
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} with subject {subject} and body {body}")


class OutlookClient(EmailClient):
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} with subject {subject} and body {body}")


#High-level module
class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_email(self, to: str, subject: str, body: str):
        self.email_client.send_email(to, subject, body)

    def reset_password(self, email: str, new_password: str):
        self.email_client.send_email(email, "Reset Password", f"Your new password is {new_password}")


if __name__ == "__main__":
    gmail_client = GmailClient()
    outlook_client = OutlookClient()
    email_service = EmailService(gmail_client)
    email_service.send_email("test@example.com", "Test Subject", "Test Body")
    email_service.reset_password("test@example.com", "NewPassword123")