import os
import tkinter as tk
from tkinter import messagebox
import json
import winsound #BROO LE PUSE SONIDITO A LOS BOTONES

class CVApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("CV builder")
        raiz.iconbitmap("img/icono.ico")
        self.raiz.configure(bg="lightblue")
        

        # INFORMACION PERSONAL
        self.etiqueta_etapa = tk.Label(raiz, text="INFORMACION PERSONAL", font=("Helvetica", 16, "bold"))
        self.etiqueta_etapa.grid(row=0, column=0, columnspan=2, pady=10)

        self.etiqueta_nombre = tk.Label(raiz, text="¿Cuál es tu nombre completo?")
        self.etiqueta_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_nombre = tk.Entry(raiz)
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=5)

        self.etiqueta_correo = tk.Label(raiz, text="¿Cuál es tu dirección de correo electrónico?")
        self.etiqueta_correo.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada_correo = tk.Entry(raiz)
        self.entrada_correo.grid(row=2, column=1, padx=10, pady=5)

        self.etiqueta_telefono = tk.Label(raiz, text="¿Cuál es tu número de teléfono?")
        self.etiqueta_telefono.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entrada_telefono = tk.Entry(raiz)
        self.entrada_telefono.grid(row=3, column=1, padx=10, pady=5)

        self.etiqueta_linkedin = tk.Label(raiz, text="¿Tienes perfil en LinkedIn, portafolio en línea u otras redes profesionales? (Proporciona enlaces)")
        self.etiqueta_linkedin.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entrada_linkedin = tk.Entry(raiz)
        self.entrada_linkedin.grid(row=4, column=1, padx=10, pady=5)

        self.etiqueta_direccion = tk.Label(raiz, text="¿Cuál es tu dirección o ciudad de residencia?")
        self.etiqueta_direccion.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entrada_direccion = tk.Entry(raiz)
        self.entrada_direccion.grid(row=5, column=1, padx=10, pady=5)

        # Crear un botón de envío para la primera etapa
        self.boton_enviar = tk.Button(raiz, text="Enviar", command=self.enviar_info_personal)
        self.boton_enviar.grid(row=6, column=0, columnspan=2, pady=10)

        # PERFIL PROFESIONAL 
        self.etiqueta_etapa_prof = tk.Label(raiz, text="PERFIL PROFESIONAL", font=("Helvetica", 16, "bold"))
        self.etiqueta_desc_perfil = tk.Label(raiz, text="¿Cómo describirías tu perfil profesional en una o dos frases?")
        self.entrada_desc_perfil = tk.Entry(raiz)
        self.etiqueta_objetivo_prof = tk.Label(raiz, text="¿Cuál es tu objetivo profesional actual?")
        self.entrada_objetivo_prof = tk.Entry(raiz)
        self.boton_enviar_prof = tk.Button(raiz, text="Enviar", command=self.enviar_perfil_profesional)

        # EDUCACION 
        self.etiqueta_etapa_edu = tk.Label(raiz, text="EDUCACIÓN", font=("Helvetica", 16, "bold"))
        self.etiqueta_nivel_educacion = tk.Label(raiz, text="¿Cuál es tu nivel de educación más alto completado?")
        self.entrada_nivel_educacion = tk.Entry(raiz)
        self.etiqueta_institucion = tk.Label(raiz, text="¿Cuál es el nombre de la institución educativa donde estudiaste?")
        self.entrada_institucion = tk.Entry(raiz)
        self.etiqueta_campo_estudio = tk.Label(raiz, text="¿Cuál fue tu campo de estudio o especialización?")
        self.entrada_campo_estudio = tk.Entry(raiz)
        self.etiqueta_ano_graduacion = tk.Label(raiz, text="¿En qué año te graduaste?")
        self.entrada_ano_graduacion = tk.Entry(raiz)
        self.etiqueta_reconocimientos = tk.Label(raiz, text="¿Lograste algún reconocimiento o premio académico?")
        self.entrada_reconocimientos = tk.Entry(raiz)
        self.boton_enviar_edu = tk.Button(raiz, text="Enviar", command=self.enviar_educacion)

        # EXPERIENCIA LABORAL 
        self.etiqueta_etapa_exp = tk.Label(raiz, text="EXPERIENCIA LABORAL", font=("Helvetica", 16, "bold"))
        self.etiqueta_cargo = tk.Label(raiz, text="¿Cuál fue tu cargo?")
        self.entrada_cargo = tk.Entry(raiz)
        self.etiqueta_empresa = tk.Label(raiz, text="¿En qué empresa trabajaste?")
        self.entrada_empresa = tk.Entry(raiz)
        self.etiqueta_ubicacion_empresa = tk.Label(raiz, text="¿Cuál fue la ubicación de la empresa?")
        self.entrada_ubicacion_empresa = tk.Entry(raiz)
        self.etiqueta_fecha_inicio = tk.Label(raiz, text="¿Cuándo comenzaste en ese puesto?")
        self.entrada_fecha_inicio = tk.Entry(raiz)
        self.etiqueta_fecha_fin = tk.Label(raiz, text="¿Cuándo terminaste en ese puesto?")
        self.entrada_fecha_fin = tk.Entry(raiz)
        self.etiqueta_responsabilidades = tk.Label(raiz, text="¿Cuáles fueron tus principales responsabilidades y logros en ese trabajo?")
        self.entrada_responsabilidades = tk.Entry(raiz)
        self.etiqueta_proyectos = tk.Label(raiz, text="¿Trabajaste en proyectos específicos que quieras destacar?")
        self.entrada_proyectos = tk.Entry(raiz)
        self.boton_enviar_exp = tk.Button(raiz, text="Enviar", command=self.enviar_experiencia_laboral)

    def enviar_info_personal(self):
        # Obtener los valores de entrada
        nombre = self.entrada_nombre.get()
        correo = self.entrada_correo.get()
        telefono = self.entrada_telefono.get()
        linkedin = self.entrada_linkedin.get()
        direccion = self.entrada_direccion.get()

        # Aca estan tus variables bro JAJAJAJ
        self.info_personal = {
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "linkedin": linkedin,
            "direccion": direccion
        }

        # Mostrar un cuadro de mensaje con la información recopilada
        messagebox.showinfo("Información Personal Guardada", f"Información personal guardada:\n\nNombre: {nombre}\nCorreo: {correo}\nTeléfono: {telefono}\nLinkedIn/Portafolio: {linkedin}\nDirección: {direccion}")

        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

        # Ocultar los widgets de información personal
        self.etiqueta_etapa.grid_remove()
        self.etiqueta_nombre.grid_remove()
        self.entrada_nombre.grid_remove()
        self.etiqueta_correo.grid_remove()
        self.entrada_correo.grid_remove()
        self.etiqueta_telefono.grid_remove()
        self.entrada_telefono.grid_remove()
        self.etiqueta_linkedin.grid_remove()
        self.entrada_linkedin.grid_remove()
        self.etiqueta_direccion.grid_remove()
        self.entrada_direccion.grid_remove()
        self.boton_enviar.grid_remove()

        # Mostrar los widgets de perfil profesional
        self.etiqueta_etapa_prof.grid(row=0, column=0, columnspan=2, pady=10)
        self.etiqueta_desc_perfil.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_desc_perfil.grid(row=1, column=1, padx=10, pady=5)
        self.etiqueta_objetivo_prof.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada_objetivo_prof.grid(row=2, column=1, padx=10, pady=5)
        self.boton_enviar_prof.grid(row=3, column=0, columnspan=2, pady=10)

    def enviar_perfil_profesional(self):
        # Obtener los valores de los widgets de entrada
        desc_perfil = self.entrada_desc_perfil.get()
        objetivo_prof = self.entrada_objetivo_prof.get()

        # Aca estan tus variables bro JAJAJAJ
        self.perfil_profesional = {
            "desc_perfil": desc_perfil,
            "objetivo_prof": objetivo_prof
        }

        # Mostrar un cuadro de mensaje con la información recopilada
        messagebox.showinfo("Perfil Profesional Guardado", f"Perfil profesional guardado:\n\nDescripción del Perfil: {desc_perfil}\nObjetivo Profesional: {objetivo_prof}")

        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

        # Ocultar los widgets de perfil profesional
        self.etiqueta_etapa_prof.grid_remove()
        self.etiqueta_desc_perfil.grid_remove()
        self.entrada_desc_perfil.grid_remove()
        self.etiqueta_objetivo_prof.grid_remove()
        self.entrada_objetivo_prof.grid_remove()
        self.boton_enviar_prof.grid_remove()

        # Mostrar los widgets de educación
        self.etiqueta_etapa_edu.grid(row=0, column=0, columnspan=2, pady=10)
        self.etiqueta_nivel_educacion.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_nivel_educacion.grid(row=1, column=1, padx=10, pady=5)
        self.etiqueta_institucion.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada_institucion.grid(row=2, column=1, padx=10, pady=5)
        self.etiqueta_campo_estudio.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entrada_campo_estudio.grid(row=3, column=1, padx=10, pady=5)
        self.etiqueta_ano_graduacion.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entrada_ano_graduacion.grid(row=4, column=1, padx=10, pady=5)
        self.etiqueta_reconocimientos.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entrada_reconocimientos.grid(row=5, column=1, padx=10, pady=5)
        self.boton_enviar_edu.grid(row=6, column=0, columnspan=2, pady=10)

    def enviar_educacion(self):
        # Obtener los valores de los widgets de entrada
        nivel_educacion = self.entrada_nivel_educacion.get()
        institucion = self.entrada_institucion.get()
        campo_estudio = self.entrada_campo_estudio.get()
        ano_graduacion = self.entrada_ano_graduacion.get()
        reconocimientos = self.entrada_reconocimientos.get()

        # Aca estan tus variables bro JAJAJAJ
        self.educacion = {
            "nivel_educacion": nivel_educacion,
            "institucion": institucion,
            "campo_estudio": campo_estudio,
            "ano_graduacion": ano_graduacion,
            "reconocimientos": reconocimientos
        }

        # Mostrar un cuadro de mensaje con la información recopilada
        messagebox.showinfo("Educación Guardada", f"Educación guardada:\n\nNivel de Educación: {nivel_educacion}\nInstitución: {institucion}\nCampo de Estudio: {campo_estudio}\nAño de Graduación: {ano_graduacion}\nReconocimientos: {reconocimientos}")

        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        # Ocultar los widgets de educacion
        self.etiqueta_etapa_edu.grid_remove()
        self.etiqueta_nivel_educacion.grid_remove()
        self.entrada_nivel_educacion.grid_remove()
        self.etiqueta_institucion.grid_remove()
        self.entrada_institucion.grid_remove()
        self.etiqueta_campo_estudio.grid_remove()
        self.entrada_campo_estudio.grid_remove()
        self.etiqueta_ano_graduacion.grid_remove()
        self.entrada_ano_graduacion.grid_remove()
        self.etiqueta_reconocimientos.grid_remove()
        self.entrada_reconocimientos.grid_remove()
        self.boton_enviar_edu.grid_remove()

        # Mostrar los widgets de experiencia laboral
        self.etiqueta_etapa_exp.grid(row=0, column=0, columnspan=2, pady=10)
        self.etiqueta_cargo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_cargo.grid(row=1, column=1, padx=10, pady=5)
        self.etiqueta_empresa.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entrada_empresa.grid(row=2, column=1, padx=10, pady=5)
        self.etiqueta_ubicacion_empresa.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entrada_ubicacion_empresa.grid(row=3, column=1, padx=10, pady=5)
        self.etiqueta_fecha_inicio.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entrada_fecha_inicio.grid(row=4, column=1, padx=10, pady=5)
        self.etiqueta_fecha_fin.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entrada_fecha_fin.grid(row=5, column=1, padx=10, pady=5)
        self.etiqueta_responsabilidades.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entrada_responsabilidades.grid(row=6, column=1, padx=10, pady=5)
        self.etiqueta_proyectos.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entrada_proyectos.grid(row=7, column=1, padx=10, pady=5)
        self.boton_enviar_exp.grid(row=8, column=0, columnspan=2, pady=10)

    def enviar_experiencia_laboral(self):
        # Obtener los valores de los widgets de entrada
        cargo = self.entrada_cargo.get()
        empresa = self.entrada_empresa.get()
        ubicacion_empresa = self.entrada_ubicacion_empresa.get()
        fecha_inicio = self.entrada_fecha_inicio.get()
        fecha_fin = self.entrada_fecha_fin.get()
        responsabilidades = self.entrada_responsabilidades.get()
        proyectos = self.entrada_proyectos.get()

        # Aca estan tus variables bro JAJAJAJ
        self.experiencia_laboral = {
            "cargo": cargo,
            "empresa": empresa,
            "ubicacion_empresa": ubicacion_empresa,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "responsabilidades": responsabilidades,
            "proyectos": proyectos
        }

        # Mostrar un cuadro de mensaje con la información recopilada
        messagebox.showinfo("Experiencia Laboral Guardada", f"Experiencia laboral guardada:\n\nCargo: {cargo}\nEmpresa: {empresa}\nUbicación de la Empresa: {ubicacion_empresa}\nFecha de Inicio: {fecha_inicio}\nFecha de Fin: {fecha_fin}\nResponsabilidades: {responsabilidades}\nProyectos: {proyectos}")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        # Ocultar los widgets de experiencia laboral
        self.etiqueta_etapa_exp.grid_remove()
        self.etiqueta_cargo.grid_remove()
        self.entrada_cargo.grid_remove()
        self.etiqueta_empresa.grid_remove()
        self.entrada_empresa.grid_remove()
        self.etiqueta_ubicacion_empresa.grid_remove()
        self.entrada_ubicacion_empresa.grid_remove()
        self.etiqueta_fecha_inicio.grid_remove()
        self.entrada_fecha_inicio.grid_remove()
        self.etiqueta_fecha_fin.grid_remove()
        self.entrada_fecha_fin.grid_remove()
        self.etiqueta_responsabilidades.grid_remove()
        self.entrada_responsabilidades.grid_remove()
        self.etiqueta_proyectos.grid_remove()
        self.entrada_proyectos.grid_remove()
    
        # Botón para guardar el perfil completo
        self.boton_guardar_perfil = tk.Button(raiz, text="Guardar Perfil", command=self.guardar_perfil)
        self.boton_guardar_perfil.grid(row=8, column=0, columnspan=2, pady=10)
        
    def guardar_perfil(self):
        # Combinar toda la información en un solo diccionario
        perfil_completo = {
            "info_personal": self.info_personal,
            "perfil_profesional": self.perfil_profesional,
            "educacion": self.educacion,
            "experiencia_laboral": self.experiencia_laboral
        }

        # Crear la carpeta 'data' si no existe
        if not os.path.exists("data"):
            os.makedirs("data")

        # Guardar el perfil en un archivo JSON en la carpeta 'data'
        with open(os.path.join("data", "perfil de CV.json"), "w") as archivo:
            json.dump(perfil_completo, archivo, indent=4)

        # Mostrar un cuadro de mensaje confirmando que el perfil ha sido guardado
        messagebox.showinfo("Perfil Guardado", "El perfil ha sido guardado exitosamente en 'data/perfil.json'.")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# Crear la ventana principal de la aplicación
raiz = tk.Tk()
app = CVApp(raiz)
raiz.mainloop()