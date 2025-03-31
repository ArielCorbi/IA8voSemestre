import sys
sys.stdout.reconfigure(encoding='utf-8')

class DeteccionSpamMonotono:
    def __init__(self):
        self.reglas = [
            lambda correo: "oferta" in correo.lower(),
            lambda correo: "gratis" in correo.lower(),
            lambda correo: "click aquí" in correo.lower(),
            lambda correo: correo.endswith("@spam.com"),
        ]

    def es_spam(self, correo):
        for regla in self.reglas:
            if regla(correo):
                return True  # Si una regla se cumple, es spam
        return False  # Si ninguna regla se cumple, no es spam

# Prueba del sistema monótono
correos = [
    "¡Oferta exclusiva para ti!",
    "Haz click aquí para ganar un premio",
    "Consulta tu factura adjunta",
    "usuario@spam.com"
]

detector = DeteccionSpamMonotono()
for correo in correos:
    print(f"Correo: {correo} -> Spam: {detector.es_spam(correo)}")
