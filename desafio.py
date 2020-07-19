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
    print("""Hola, aquí podrás saber aproximadamente
    cuantos días haz vivido""")
    año = int(input("""Pero primero necesito saber en que año naciste.
    ejemplo(1999): """))
    mes = int(input("Y... ¿el mes? ejemplo(4): "))
    dia = int(input("¿Cuál fue tu día de nacimiento? ejemplo (7): "))
    if dia > day:
        day = day + 31
        month = month - 1
        seg_dia = (day - dia) * dia_en_seg
        if mes > month:
            month = month + 12
            year = year + 1
            seg_mes = (month - mes) * mes_en_seg
            seg_año = (year - año)
            seg_totales = seg_dia + seg_mes + seg_año
            print("haz vivido: " + str(seg_totales) + " segundos")
        else:
            seg_mes = (month - mes) * mes_en_seg
            seg_año = (year - año)
            seg_totales = seg_dia + seg_mes + seg_año
            print("haz vivido: " + str(seg_totales) + " segundos")
    else:
        seg_dia = (day - dia) * dia_en_seg 
        if mes > month:
            month = month + 12
            year = year + 1
            seg_mes = (month - mes) * mes_en_seg
            seg_año = (year - año)
            seg_totales = seg_dia + seg_mes + seg_año
            print("haz vivido: " + str(seg_totales) + " segundos")
        else:
            seg_mes = (month - mes) * mes_en_seg
            seg_año = (year - año)
            seg_totales = seg_dia + seg_mes + seg_año
            print("haz vivido: " + str(seg_totales) + " segundos")
    


if __name__ == "__main__":
    run()
