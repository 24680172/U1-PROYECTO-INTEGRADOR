import flet as ft

def main(page: ft.Page):
    # ---------------- CONFIGURACIÓN ----------------
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#000000"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # ---------------- CONTROLES ----------------
    txt_nombre = ft.TextField(label="Nombre", border_color="#F200FF", expand=True)
    txt_control = ft.TextField(label="Número de control", border_color="#F200FF", expand=True)
    txt_email = ft.TextField(label="Email", border_color="#F200FF")

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#F200FF",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#F200FF",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # ---------------- RADIO BUTTON GÉNERO ----------------
    genero_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro"),
        ])
    )

    # ---------------- MENSAJE DE RESULTADO ----------------
    txt_resultado = ft.Text("", color="green", weight=ft.FontWeight.BOLD)

    # ---------------- FUNCIÓN ENVIAR ----------------
# ---------------- FUNCIÓN ENVIAR ----------------
    def enviar_click(e):
        # 1. Validación de campos vacíos
        if (
            not txt_nombre.value or
            not txt_control.value or
            not txt_email.value or
            not dd_carrera.value or
            not dd_semestre.value or
            not genero_group.value
        ):
            txt_resultado.value = " ¡¡Por favor completa todos los campos!!"
            txt_resultado.color = "red"
        
        # 2. NUEVA VALIDACIÓN: Verificar si contiene el '@'
        elif "@" not in txt_email.value:
            txt_resultado.value = " El email no es válido (falta el '@')"
            txt_resultado.color = "red"
            
        else:
            # Si pasa todas las validaciones
            txt_resultado.value = (
                f"Registro exitoso\n"
                f"Nombre: {txt_nombre.value}\n"
                f"Control: {txt_control.value}\n"
                f"Email: {txt_email.value}\n"
                f"Carrera: {dd_carrera.value}\n"
                f"Semestre: {dd_semestre.value}\n"
                f"Género: {genero_group.value}"
            )
            txt_resultado.color = "white"

            # Limpiar campos
            txt_nombre.value = ""
            txt_control.value = ""
            txt_email.value = ""
            txt_nombre.value = ""
            dd_carrera.value = None
            dd_semestre.value = None
            genero_group.value = None

        page.update()

    # ---------------- BOTÓN ----------------
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=400,
        on_click=enviar_click
    )

    # ---------------- INTERFAZ ----------------
    page.add(
        ft.Column([
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            ft.Text("Género:", color="#4D2A32", weight=ft.FontWeight.BOLD),
            genero_group,
            btn_enviar,
            txt_resultado
        ], spacing=15)
    )

# Ejecutar en navegador
ft.app(target=main, view=ft.AppView.WEB_BROWSER)