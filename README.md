# Correo
# Secret Santa - Email Sender

This Python script randomly assigns participants for a Secret Santa gift exchange and sends them an email notifying them of their assigned person. It ensures that no participant is assigned to themselves.

## Features

- **Random Assignment:** Shuffles the list of participants randomly.
- **Validation:** Prevents any participant from being assigned to themselves.
- **Email Sending:** Uses Gmail's SMTP server to send notifications.
- **Customization:** Easily modify messages, subjects, and recipient details.

## Requirements

- **Python 3.x:** Ensure you have a recent version of Python installed.
- **Internet Connection:** Required to connect to the SMTP server.
- **Gmail Account:** Needed to send emails. If you use two-factor authentication, you will need to generate an [App Password](https://myaccount.google.com/apppasswords).

## Configuration

1. **Install Python 3.x:** If you haven't installed it yet, download it from [python.org](https://www.python.org/).

2. **Edit the Script:**  
   Open the Python file and make the following changes:
   - **User and Password:**  
     Replace `usuario` with your Gmail address and `contraseña` with the generated app password.
   - **Participants Lists:**  
     Populate the `mensajes` and `correos` lists with the names and email addresses of the participants, respectively.
   - **Message Customization:**  
     Modify the email subject (`asunto`) and body (`cuerpo`) as desired.

## Execution

To run the script, open a terminal, navigate to the directory where the file is located, and execute:

```bash
python your_script_name.py
