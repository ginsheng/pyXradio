class sino(object):
    opciones = {
        1: 'SI',
        2: 'NO',
        97: 'NO APLICA',
        98: 'SE IGNORA',
        99: 'NO ESPECIFICADO'}

    @classmethod
    def valor(cls, id):

        if not isinstance(id, int):
            return 'No encontrado'

        return cls.opciones[id]
