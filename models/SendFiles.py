import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendFiles:
	
	def __init__(self, vars):
		print vars['data']
		
		
		### Email client
		fromaddr = "msolano@requiez.com"
		toaddr = vars['data']['correo']
		msg = MIMEMultipart()
		
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Transparencia Grupo Requiez"
		
		body = "Los archivos solicitados se adjuntaron en el actual correo"
		
		msg.attach(MIMEText(body, 'plain'))
		
		for file in vars['data']['files']:
			filename = file+'.pdf'
			path = os.path.dirname(os.path.abspath(__file__))+"/../static/files/"+filename
			attachment = open(path, "rb")
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		
			msg.attach(part)
		
		text = msg.as_string()

		server = smtplib.SMTP('requiez.com', 587)
		server.starttls()
		server.login(fromaddr, "36602317mario")
		server.sendmail(fromaddr, toaddr, text)

		### Email requiez
		fromaddr = "wwwmario1515@gmail.com"
		toaddr = "wwwmario1515@gmail.com"
		msg = MIMEMultipart()
		
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Transparencia Grupo Requiez"
		
		body = "Seguimiento de transparencia: \n\n"

		body += "Nombre: "+vars['data']['nombre']+"\n\n"
		body += "Correo: "+vars['data']['correo']+"\n\n"
		body += "Telefono: "+vars['data']['telefono']+"\n\n"
		body += "Empresa: "+vars['data']['empresa']+"\n\n"
		body += "Comentario: "+vars['data']['comentario']+"\n\n"

		body += "Archivos: "
		for file in vars['data']['files']:
			body += file+','

		msg.attach(MIMEText(body, 'plain'))
		
		text = msg.as_string()

		server.sendmail(fromaddr, toaddr, text)

		server.quit()
		

class SendEmail:
	
	def __init__(self, vars):
		print vars['data']

		fromaddr = "msolano@requiez.com"
		toaddr = "wwwmario1515@gmail.com"
		
		server = smtplib.SMTP('requiez.com', 587)
		server.starttls()
		server.login(fromaddr, "36602317mario")

		### Email requiez
		msg = MIMEMultipart()
		
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Transparencia Grupo Requiez"
		
		body = "Seguimiento de transparencia: \n\n"

		body += "Nombre: "+vars['data']['nombre']+"\n\n"
		body += "Correo: "+vars['data']['correo']+"\n\n"
		body += "Telefono: "+vars['data']['telefono']+"\n\n"
		body += "Empresa: "+vars['data']['empresa']+"\n\n"
		body += "Comentario: "+vars['data']['comentario']+"\n\n"

		msg.attach(MIMEText(body, 'plain'))
		
		text = msg.as_string()

		server.sendmail(fromaddr, toaddr, text)

		server.quit()
		