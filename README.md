# Botini - Discord Bot con IA Gemini

Botini es un bot de Discord desarrollado en Python, diseñado para ofrecer una experiencia divertida e interactiva en servidores de Discord. En lugar de ser un bot tradicional de Discord, Botini usa una cuenta de usuario normal, permitiendo funciones únicas para trolear amigos y realizar tareas automáticas gracias a la inteligencia artificial Gemini. Algunas de las funciones principales incluyen banear y kickear usuarios, responder a mensajes de forma inteligente y otras interacciones personalizables.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- **Interacciones Inteligentes**: Botini usa la inteligencia artificial Gemini para responder de forma inteligente y natural a los mensajes en el servidor.
- **Moderación Automática**: Puede realizar acciones como banear o kickear usuarios según ciertas condiciones establecidas o comandos dados.
- **Funciones Divertidas**: Incluye comandos y respuestas automáticas para trolear a amigos y añadir diversión al chat.
- **Uso de Cuenta de Usuario Normal**: Botini actúa desde una cuenta normal de usuario, proporcionando una experiencia única de bot en Discord.

## Instalación

1. **Clona el repositorio**
    ```bash
    git clone https://github.com/Yitzhakbuff/Botini.git
    cd Botini
    ```

2. **Configura el entorno**:
    - Asegúrate de tener Python 3.8 o superior.
    - Instala las dependencias necesarias.
    
    ```bash
    pip install -r requirements.txt
    ```

3. **Configura las credenciales de tu cuenta de usuario**:
    - Botini funciona usando una cuenta de usuario en lugar de una cuenta de bot. Configura el token de la cuenta de usuario en un archivo `.env` o directamente en el código (si es seguro).
    - **Nota**: Usar una cuenta de usuario en Discord para propósitos de bot está en contra de los Términos de Servicio de Discord. Ten en cuenta los riesgos asociados antes de continuar.

4. **Ejecuta el bot**:
    ```bash
    python botini.py
    ```

## Uso

- Una vez que Botini esté activo en el servidor, puedes usar los comandos disponibles y experimentar las respuestas automáticas de la IA.
- **Comandos Disponibles**:
    - `/ban [usuario]` - Banea al usuario especificado.
    - `/kick [usuario]` - Expulsa al usuario especificado.
    - Otros comandos para trolear y interactuar serán documentados o puedes explorarlos en el código fuente.

**Nota**: Botini actúa con lógica propia en algunas interacciones, gracias a su integración con la IA, y puede reaccionar de forma espontánea en el chat.

## Contribuciones

Las contribuciones son bienvenidas. Puedes enviar tus mejoras o sugerencias a través de [GitHub](https://github.com/Yitzhakbuff/Botini/).

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcion`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Agrega nueva función'`).
4. Envía los cambios a tu rama (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

**Nota Importante**: Usar cuentas de usuario en lugar de cuentas de bot para automatización va en contra de los Términos de Servicio de Discord y puede conllevar sanciones. Este proyecto está diseñado para fines educativos y experimentales; utiliza este software bajo tu propia responsabilidad.
