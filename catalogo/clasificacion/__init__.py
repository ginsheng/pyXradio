class clasificacion(object):
    clasificaciones = {
        1: 'CASO DE COVID-19 CONFIRMADO POR ACE',
        2: 'CASO DE COVID-19 CONFIRMADO POR CDD',
        3: 'CASO DE SARS-COV-2 CONFIRMADO',
        4: 'INVÁLIDO POR LABORATORIO',
        5: 'NO REALIZADO POR LABORATORIO',
        6: 'CASO SOSPECHOSO',
        7: 'NEGATIVO A SARS-COV-2'}

    @classmethod
    def valor(cls, clasificacion_id):

        if not isinstance(clasificacion_id, int):
            return 'No encontrado'

        return cls.clasificaciones[clasificacion_id]
