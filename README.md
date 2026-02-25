1. El Punto de Entrada y el Árbol de la PáginaPythonimport flet as ft

def main(page: ft.Page):
    # ... configuración ...
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.Page: No es solo una ventana; es el Contenedor Raíz. Imagínalo como el <body> en HTML. Controla el alineamiento, el espaciado (padding) y el tema.target=main: Es un callback. Flet inicia un servidor interno y, cuando un cliente (tú) se conecta, ejecuta esta función pasando la instancia de la página.view=ft.AppView.WEB_BROWSER: Cambia el renderizado de una ventana nativa (SO) a un servidor web local (habitualmente en el puerto 8550).2. Definición de Objetos de Estado (Inputs)Pythontxt_nombre = ft.TextField(label="Nombre", border_color="#F200FF", expand=True)
Aquí estás creando instancias de clase.expand=True: Esto es clave en el diseño responsivo. Le dice al control que ocupe todo el espacio disponible dentro de su contenedor (un Row o Column).Identificadores: Al guardar el TextField en la variable txt_nombre, creas una referencia persistente. Esto te permite consultar txt_nombre.value en cualquier momento, incluso fuera de la función donde se creó.3. Generación Dinámica de OpcionesPythondd_semestre = ft.Dropdown(
    options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
)
List Comprehension: Aquí aplicas lógica de Python puro para la interfaz. En lugar de escribir 6 líneas de código, generas objetos ft.dropdown.Option dinámicamente. Esto es lo que hace a Flet potente: puedes usar todas las herramientas de Python para construir la UI.4. El Ciclo de Vida del Evento (enviar_click)Esta es la parte más compleja y "elaborada" del sistema:Pythondef enviar_click(e):
    # 1. Captura de datos (Pull Model)
    # 2. Lógica de validación
    # 3. Mutación del estado del control (txt_resultado.value = "...")
    # 4. Sincronización (page.update())
El parámetro e: Es un objeto ControlEvent. Contiene información sobre quién disparó el evento (el botón), las coordenadas del clic, etc.Validación de Cortocircuito: El uso de if/elif asegura que el programa se detenga en el primer error encontrado, mejorando la experiencia del usuario (UX) al no saturarlo con todos los errores a la vez.page.update(): Flet usa un sistema de Estado Diferido. Cuando cambias txt_resultado.value, el cambio solo ocurre en la memoria de Python. page.update() envía un paquete JSON al navegador con los cambios para que la UI se refresque.5. Composición de la UI (Layout Engine)Pythonpage.add(
    ft.Column([
        ft.Row([dd_carrera, dd_semestre], spacing=10),
        # ...
    ], spacing=15)
)
Flet utiliza un sistema de Flexbox:ft.Column: Define un eje principal vertical. El spacing=15 separa los elementos automáticamente sin necesidad de márgenes manuales.ft.Row: Anidado dentro de la columna, crea un eje horizontal. Es ideal para formularios donde quieres que dos campos compartan una línea.6. Resumen de Propiedades AvanzadasPropiedadFunción Técnicabgcolor="#000000"Define el fondo en formato Hexadecimal.weight=ft.FontWeight.BOLDAccede a las constantes de tipografía del framework.on_clickEs un puntero a la función. No lleva paréntesis () porque no queremos que se ejecute al cargar, sino cuando ocurra el evento.
