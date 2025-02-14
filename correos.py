import random
import smtplib

# Listas de mensajes y correos electrónicos
mensajes = ["", "", "", "", ""]
correos = ["", "", "", "", ""]

# Configuración del servidor SMTP
servidor_smtp = "smtp.gmail.com"
puerto_smtp = 587
usuario = ""  # Cambia esto por tu correo
contraseña = ""  # Usa la contraseña de aplicación generada en tu cuenta de Google Cloud Platform (https://myaccount.google.com/apppasswords)

try:
    # Conexión al servidor SMTP
    conexion = smtplib.SMTP(servidor_smtp, puerto_smtp)
    conexion.starttls()  # Iniciar conexión segura
    conexion.login(usuario, contraseña)  # Autenticación

    # Barajar la lista de mensajes para asignar amigos invisibles
    amigos_invisibles = mensajes[:]
    random.shuffle(amigos_invisibles)

    # Asegurarse de que nadie se asigne a sí mismo
    while any(mensaje == amigo for mensaje, amigo in zip(mensajes, amigos_invisibles)):
        random.shuffle(amigos_invisibles)

    # Enviar cada mensaje a un correo
    for mensaje, correo, amigo_invisible in zip(mensajes, correos, amigos_invisibles):
        asunto = "Amigo Invisible" # Modificar por lo que mas quieras
        cuerpo = (
            f"Subject: {asunto}\n\n" # Modificar por lo que mas quieras
            f"Hola {mensaje},\n\n" # Modificar por lo que mas quieras
            f"¡Te ha tocado {amigo_invisible} como tu amigo invisible!\n" # Modificar por lo que mas quieras
            f"Recuerda que el precio del regalo debe estar entre 5 y 10€.\n"    # Modificar por lo que mas quieras
            f"¡Diviértete eligiendo el regalo!"  # Modificar por lo que mas quieras
            f"Tienes hasta el dia 31 de octubre para que te regales el regalo.\n\n" # Modificar por lo que mas quieras
            f"DATE PRISAAAA" # Modificar por lo que mas quieras
        )
        conexion.sendmail(usuario, correo, cuerpo.encode('utf-8'))
        print(f"Correo enviado a {correo} con el mensaje: {mensaje} y amigo invisible: {amigo_invisible}")  # Descomentar para depuración

    conexion.quit()  # Cerrar la conexión
except Exception as e:
    print(f"Error al enviar correos: {e}")