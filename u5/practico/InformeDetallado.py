from models import Asistencia

class InformeDetallado:
    AULA = 1
    ED_FIS = 2

    PRESENTE = 's'
    AUSENTE = 'n'
    AUSENTE_JUS = str
    AUSETE_INJUS = None

    def __init__(self, idest, nomb, apel):
        self.idest = idest
        self.nomb = nomb
        self.apel = apel
        self.aula = {'presente': 0, 'justificadas': 0, 'nojustificadas': 0}
        self.ed_fis = {'presente': 0, 'justificadas': 0, 'nojustificadas': 0}
        self.total = 0

    def agregarAsistencia(self, asistencia):
        tipo_clase = asistencia[2]
        if asistencia[0] == self.AUSENTE:
            self.total += 1 if tipo_clase == self.AULA else 0.5

        asistio_key = 'presente' if asistencia[0] == self.PRESENTE else ( 'justificadas' if asistencia[1] is not None else 'nojustificadas')
        if tipo_clase == self.AULA:
            self.aula[asistio_key] += 1
        elif tipo_clase == self.ED_FIS:
            self.ed_fis[asistio_key] += 1

