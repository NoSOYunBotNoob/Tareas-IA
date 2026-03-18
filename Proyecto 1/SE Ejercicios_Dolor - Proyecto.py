class SistemaExpertoEjercicio:

    def __init__(self):
        self.hechos = {}
        self.reglas = []
        self.conclusiones = {}
        self.traza = []

    # -------------------------
    # REGLAS DIRECTAS
    # -------------------------
    def definir_reglas(self):

        self.reglas = [

        # -------- TRONCO SUPERIOR --------
        {"id":1, "premisas":[("dolor_hombro",True),("dolor_trapecio",True)], "conclusion":"Press_Militar", "certeza":0.9},

        {"id":2, "premisas":[("dolor_pecho",True)], "conclusion":"Press_Banca", "certeza":0.9},

        {"id":3, "premisas":[("dolor_biceps",True)], "conclusion":"Curl_Biceps", "certeza":0.85},

        {"id":4, "premisas":[("dolor_triceps",True)], "conclusion":"Fondos", "certeza":0.85},

        {"id":5, "premisas":[("dolor_abdominales",True)], "conclusion":"Crunches", "certeza":0.8},

        {"id":6, "premisas":[("dolor_diafragma",True)], "conclusion":"Mala_Respiracion_Ejercicio", "certeza":0.75},

        {"id":7, "premisas":[("dolor_trapecio",True)], "conclusion":"Encogimientos_Hombro", "certeza":0.8},

        {"id":8, "premisas":[("dolor_hombro",True)], "conclusion":"Elevaciones_Laterales", "certeza":0.85},

        # -------- TRONCO INFERIOR --------
        {"id":9, "premisas":[("dolor_gluteos",True)], "conclusion":"Hip_Thrust", "certeza":0.9},

        {"id":10, "premisas":[("dolor_cuadriceps",True)], "conclusion":"Sentadilla", "certeza":0.9},

        {"id":11, "premisas":[("dolor_aductores",True)], "conclusion":"Maquina_Aductores", "certeza":0.85},

        {"id":12, "premisas":[("dolor_femoral",True)], "conclusion":"Peso_Muerto", "certeza":0.9},

        {"id":13, "premisas":[("dolor_pantorrilla",True)], "conclusion":"Elevaciones_Talon", "certeza":0.85},

        {"id":14, "premisas":[("dolor_pantorrilla",True),("dolor_femoral",True)], "conclusion":"Correr", "certeza":0.8},

        {"id":15, "premisas":[("dolor_gluteos",True),("dolor_cuadriceps",True)], "conclusion":"Desplantes", "certeza":0.85},

        {"id":16, "premisas":[("dolor_cuadriceps",True),("dolor_femoral",True)], "conclusion":"Prensa_Pierna", "certeza":0.85}

        ]

    # -------------------------
    # HECHOS
    # -------------------------
    def obtener_sintomas(self):

        print("¿Dónde se localiza el dolor?")
        print("1. Tronco superior")
        print("2. Tronco inferior")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            sintomas = [
                "dolor_hombro",
                "dolor_trapecio",
                "dolor_pecho",
                "dolor_biceps",
                "dolor_triceps",
                "dolor_abdominales",
                "dolor_diafragma"
            ]
        else:
            sintomas = [
                "dolor_gluteos",
                "dolor_cuadriceps",
                "dolor_aductores",
                "dolor_femoral",
                "dolor_pantorrilla"
            ]

        for s in sintomas:
            r = input(f"{s}? (s/n): ")
            self.hechos[s] = True if r == "s" else False

    # -------------------------
    # MOTOR (igual que tu modelo)
    # -------------------------
    def motor_inferencia(self):

        for regla in self.reglas:

            cumplidas = []

            for premisa, valor in regla["premisas"]:

                if premisa in self.hechos:
                    cumplidas.append(1 if self.hechos[premisa] == valor else 0)
                else:
                    cumplidas.append(0)

            promedio = sum(cumplidas) / len(cumplidas)

            if promedio > 0:

                certeza_final = regla["certeza"] * promedio

                self.conclusiones[regla["conclusion"]] = certeza_final

                self.traza.append({
                    "regla": regla["id"],
                    "conclusion": regla["conclusion"],
                    "certeza": certeza_final
                })

    # -------------------------
    # RESULTADOS
    # -------------------------
    def mostrar_explicacion(self):

        print("\nPOSIBLES EJERCICIOS CAUSANTES")

        # ordenar por mayor certeza
        resultados = sorted(self.conclusiones.items(), key=lambda x: x[1], reverse=True)

        for c, v in resultados:
            print(c, "->", round(v * 100, 2), "%")

        print("\nTRAZA")
        for t in self.traza:
            print("Regla", t["regla"], "->", t["conclusion"],
                  "(", round(t["certeza"] * 100, 2), "%)")

# EJECUCIÓN
se = SistemaExpertoEjercicio()
se.definir_reglas()
se.obtener_sintomas()
se.motor_inferencia()
se.mostrar_explicacion()