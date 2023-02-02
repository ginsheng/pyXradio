class estados(object):
    nombres = {
        1: 'AGUASCALIENTES',
        2: 'BAJA CALIFORNIA',
        3: 'BAJA CALIFORNIA SUR',
        4: 'CAMPECHE',
        5: 'COAHUILA DE ZARAGOZA',
        6: 'COLIMA',
        7: 'CHIAPAS',
        8: 'CHIHUAHUA',
        9: 'CIUDAD DE MÉXICO',
        10: 'DURANGO',
        11: 'GUANAJUATO',
        12: 'GUERRERO',
        13: 'HIDALGO',
        14: 'JALISCO',
        15: 'MÉXICO',
        16: 'MICHOACÁN DE OCAMPO',
        17: 'MORELOS',
        18: 'NAYARIT',
        19: 'NUEVO LEÓN',
        20: 'OAXACA',
        21: 'PUEBLA',
        22: 'QUERÉTARO',
        23: 'QUINTANA ROO',
        24: 'SAN LUIS POTOSÍ',
        25: 'SINALOA',
        26: 'SONORA',
        27: 'TABASCO',
        28: 'TAMAULIPAS',
        29: 'TLAXCALA',
        30: 'VERACRUZ DE IGNACIO DE LA LLAVE',
        31: 'YUCATÁN',
        32: 'ZACATECAS',
        36: 'ESTADOS UNIDOS MEXICANOS',
        97: 'NO APLICA',
        98: 'SE IGNORA',
        99: 'NO ESPECIFICADO'}

    @classmethod
    def nombre(cls, estado_id):

        if not isinstance(estado_id, int):
            return 'No encontrado'

        return cls.nombres[estado_id]
