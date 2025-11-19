Bot de Telegram en Python

Este proyecto es un bot de Telegram desarrollado en Python, diseñado para responder automáticamente a mensajes. Está pensado para ser accesible desde Cuba, usando recursos gratuitos y estrategias de uptime para mantenerlo activo 24/7.

📁 Estructura del repositorio

- main.py: Código principal del bot.  
- requisitos.txt: Lista de dependencias necesarias para ejecutar el bot.  
- README.md: Documentación del proyecto.  

✅ Progreso actual

- [x] Repositorio creado en GitHub.  
- [x] Archivos main.py y requisitos.txt subidos.  
- [x] Conexión establecida con Render para despliegue en la nube.  
- [x] Variables de entorno configuradas (ej. token del bot).  

🔜 Próximos pasos

- [ ] Añadir funciones adicionales al bot según necesidades futuras.  
- [ ] Mejorar la documentación con ejemplos de uso.  
- [ ] Implementar monitoreo externo opcional para verificar uptime.  

🚀 Instalación local

1. Clona el repositorio:

   `bash
   git clone https://github.com/Pedraza2023/Telegram.git
   cd Telegram
   `

2. Instala las dependencias:

   `bash
   pip install -r requisitos.txt
   `

3. Configura tu token de Telegram como variable de entorno:

   Linux/MacOS:
   `bash
   export BOTTOKEN=tutoken_aquí
   `

   Windows (PowerShell):
   `powershell
   setx BOTTOKEN "tutoken_aquí"
   `

4. Ejecuta el bot:

   `bash
   python main.py
   `

---

💬 Ejemplo de comandos disponibles

- /start → El bot responde con un mensaje de bienvenida confirmando que está activo.  
- Texto libre → El bot repite lo que escribas, a modo de prueba de funcionamiento.  

Ejemplo:  
`
Usuario: Hola bot
Bot: Me dijiste: Hola bot
`

---

🌐 Despliegue en Render paso a paso

1. Conecta tu repositorio de GitHub a Render  
   - Ve a Render y crea una cuenta.  
   - Selecciona New Web Service y conecta tu repositorio Telegram.  

2. Configura el servicio  
   - Environment: selecciona Python 3.9+.  
   - Build Command:  
     `bash
     pip install -r requisitos.txt
     `  
   - Start Command:  
     `bash
     python main.py
     `  

3. Agrega variables de entorno  
   - En la sección Environment Variables, añade:  
     - BOT_TOKEN → tu token de Telegram.  

4. Despliega el bot  
   - Render instalará las dependencias y ejecutará main.py.  
   - El bot quedará activo 24/7 usando polling.  

5. Verifica funcionamiento  
   - Abre Telegram, escribe /start a tu bot y confirma que responde.  

---

🛠️ Troubleshooting (solución de problemas)

- Error: BOT_TOKEN no está definido  
  → Verifica que configuraste la variable de entorno en Render con el nombre exacto BOT_TOKEN.

- Error de versión: funciones no reconocidas  
  → Asegúrate de que tu requisitos.txt tenga:  
    `
    python-telegram-bot==20.7
    `  
    Si aparece Updater o Dispatcher en el código, significa que estás usando ejemplos antiguos (versión 13.x). Usa ApplicationBuilder y funciones async.

- El bot no responde en Telegram  
  → Comprueba que el servicio en Render está corriendo y que el token es válido.  
  → Revisa los logs en Render para detectar errores de conexión.

- Dependencias no instaladas  
  → Confirma que el comando de build en Render sea:  
    `bash
    pip install -r requisitos.txt
    `

- El bot se detiene inesperadamente  
  → Render reinicia automáticamente el servicio si falla. Verifica los logs para identificar el error exacto.  
  → Si el problema es recurrente, revisa el código en main.py y añade un manejador de errores (error_handler) para capturar excepciones.
