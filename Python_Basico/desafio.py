# Creado por MAU
def cuenta(seg_totales): 
    LIMITE = 1000
    i = 0

    while i < seg_totales:
        print(str(i))
        i += 1
        if i == LIMITE:
            print("Ya estas muy viejo!!!!! Si sigo contando tardare 1000 años xD")
            print("Haz vivido: " + str(seg_totales) + " segundos")
            break     

def mes_mas(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg):
    seg_mes = (month + 12 - mes) * mes_en_seg
    seg_año = (year - 1 - año) * año_en_seg
    seg_totales = seg_dia + seg_mes + seg_año
    cuenta(seg_totales)

def mes_menos(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg):
    seg_mes = (month - mes) * mes_en_seg
    seg_año = (year - año) * año_en_seg
    seg_totales = seg_dia + seg_mes + seg_año
    cuenta(seg_totales)

def run():
    #Día actual
    import datetime
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    #Conversión de dia, mes y año en segundos
    dia_en_seg = 86400
    mes_en_seg = 31 * dia_en_seg
    año_en_seg = 12 * mes_en_seg

    print("Hola, aquí podrás saber aproximadamente cuantos días haz vivido")
    año = int(input("""Primero necesito saber en que año naciste.
    ejemplo( 1999 ): """))
    mes = int(input("Y... ¿el mes? ejemplo( 4 ): "))
    dia = int(input("Ahora... ¿Cuál fue tu día de nacimiento? ejemplo ( 7 ): "))
    if dia > day:
        day = day + 31
        month = month - 1
        seg_dia = (day - dia) * dia_en_seg
        if mes > month:
            mes_mas(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg)
        else:
            mes_menos(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg)
    else:
        seg_dia = (day - dia) * dia_en_seg 
        if mes > month:
            mes_mas(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg)
        else:
            mes_menos(seg_dia, month, mes, mes_en_seg, año, year, año_en_seg)
       


if __name__ == "__main__":
    run()