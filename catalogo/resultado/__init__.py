class resultado(object):
    resultados = {
        1: 'POSITIVO A SARS-COV-2',
        2: 'NO POSITIVO A SARS-COV-2',
        3: 'RESULTADO PENDIENTE',
        4: 'RESULTADO NO ADECUADO ',
        97: 'NO APLICA (CASO SIN MUESTRA)'}

    @classmethod
    def valor(cls, resultado_id):

        if not isinstance(resultado_id, int):
            return 'No encontrado'

        return cls.resultados[resultado_id]
