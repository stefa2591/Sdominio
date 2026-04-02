import os
import random
import sys
import time
import names
from tqdm import tqdm

def eliminar_lineas_duplicadas(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        unique_lines = list(set(lines))

        print(f"Archivo: {file_path}")
        print(f"Líneas en el archivo original: {len(lines)}")
        print(f"Líneas duplicadas eliminadas: {len(lines) - len(unique_lines)}")
        print()

        directory = "/sdcard/SinDuplicadas"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.basename(file_path)
        output_path = os.path.join(directory, filename)

        with open(output_path, "w") as file:
            file.writelines(unique_lines)

        print(f"Archivo guardado en: {output_path}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except IOError:
        print("Error de lectura del archivo.")
        
#os.system('clear')
time.sleep(0.1)
print       ("""
\033[38;5;196m\n         
 
♡𝐅𝐑𝐈𝐄𝐍𝐃𝐒 𝐒𝐂𝐇𝐎𝐎𝐋♡

𝐂𝐀𝐓𝐀𝐋𝐈𝐍𝐀
            ＿＿＿
         ／            ▲
／￣   ヽ       ■■
●                ■■■
ヽ＿＿＿       ■■
          ）＝｜
        ／    ｜｜
    ∩∩＿＿とﾉ
    しし───┘ \n🄲🄾🄼🄱🄾    \n   🄼3🅄      \n        
     

""")
time.sleep(0.1)
def main():
    print("""\n\33[38;5;206m
    
𝕋𝕚𝕡𝕠 𝕕𝕖 ℂ𝕠𝕞𝕓𝕠 𝕡𝕒𝕣𝕒 𝕔𝕣𝕖𝕒𝕣

1) USER:PASS 2000 AL 2023  
2) USER:PASS SIMPLE NOMBRE-NOMBRE 
3) USER:PASS CON NÚMEROS DEL 1 AL 499 
4) USER:PASS CON NÚMEROS DEL 500 AL 999 
5) USER:PASS CON AÑO DE NACIMIENTO
6) USER:PASS CON NÚMEROS DEL 0 AL 0000
7) USER:PASS CON NÚMEROS DEL 111 AL 999
8) USER:PASS CON NÚMEROS 123 AL 12345
9) USER:NUMB 123 AL 123456  
10) CREA UN COMBO CON TU LISTA
11) ELIMINAR LINEAS DUPLICADAS
12) SALIR
\033[0m""")

    menu = input("Ingrese una opción: ")

    if menu == "10":
        file_path = input("Ingrese la ruta de su archivo .txt ('10' para retroceder): ")
        if file_path == "10":
            print("Volviendo al menú principal...\n")
            main()
        hwm = int(input("Número de líneas (x2): "))

        while True:
            print("""
            \33[33m
SUBMENÚ - CREA UN COMBO CON TU LISTA
            
        1) USER:PASS 2000 AL 2023
        2) USER:PASS NOMBRE-NOMBRE
        3) USER:PASS DEL 1 AL 499
        4) USER:PASS DEL 500 AL 999
        5) USER:PASS AÑO DE NACIMIENTO
        6) USER:PASS DEL 0 AL 0000
        7) USER:PASS 111, 222, ..., 999
        8) USER:PASS 123, 1234, 12345...
        9) USER:NUMB 123 AL 123456 
        10) ATRÁS
            """)

            submenu_option = input("Ingrese una opción: ")

            if submenu_option in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                with open(file_path, "r") as file:
                    names_list = file.readlines()

                filename = input("\nNombre de su Combo: ")

                print(f"Archivo: {file_path}")
                print(f"Líneas en el archivo: {len(names_list)}")
                print()
                
                if submenu_option in ["1", "3", "4", "5", "6", "7", "8"]:
                    print("Genere combinacion")
                    print("1 = Solo Izquierda")
                    print("2 = Solo Derecha")
                    print("3 = Ambas")
                    combo_option = input("Eliga su Opcion: ")

                with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                    for i in range(hwm):
                        rname = random.choice(names_list).strip()
                        rlastname = random.choice(names_list).strip()
                        if submenu_option == "1":
                            num = random.randint(2000, 2023)
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "2":
                            alln = f"{rname}:{rlastname}"
                        elif submenu_option == "3":
                            num = random.randint(1, 499)
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "4":
                            num = random.randint(500, 999)
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "5":
                            num = random.randint(1900, 2023)
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "6":
                            num = random.choice(["0", "00", "000", "0000"])
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "7":
                            num = random.choice(["111", "222", "333", "444", "555", "666", "777", "888", "999"])
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "8":
                            num = random.choice(["123", "1234", "12345", "321", "4321", "54321"])
                            if combo_option == "1":
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}"
                            elif combo_option == "2":
                                all1 = f"{rname}"
                                alln = f"{all1}:{rname}{num}"
                            else:
                                all1 = f"{rname}{num}"
                                alln = f"{all1}:{rname}{num}"
                        elif submenu_option == "9":
                            numbers1 = random.choice(["123",  "1234", "12345", "123456", "321", "4321", "54321", "654321", "1020", "102030"])
                            all1 = f"{rname}"
                            alln = f"{all1}:{numbers1}"

                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(alln + "\n")
                        pbar.update(1)
                        time.sleep(0.1)

                print(f"\nNombre de su archivo combo: {filename}@.txt")

            elif submenu_option == "10":
                break
            else:
                print("Opción no válida. Por favor, elija una opción del submenú.")

                main()

    elif menu == "11":
        file_path = input("Ingrese la ruta de su archivo .txt: ")
        
        print(f"Archivo: {file_path}")
        print()

        respuesta = input("¿Desea eliminar líneas duplicadas de este archivo?\n1 = Si\n2 = No\nRespuesta: ")

        if respuesta == "1":
            eliminar_lineas_duplicadas(file_path)
        elif respuesta == "2":
            main()
        else:
            print("Opción no válida. Volviendo al menú principal.")

    elif menu == "12":
        sys.exit()
    else:
        if menu == "1":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))
            
            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.randint(2000, 2023)
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "2":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.randint(0, 499)
                    all1 = f"{rname}"
                    alln = f"{all1}:{rname}"
                    all2 = f"{rlastname}"
                    allf = f"{all2}:{rlastname}"
                    line1 = alln + "\n"
                    line2 = allf + "\n"

                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "3":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.randint(0, 499)
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "4":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.randint(500, 999)
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "5":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.randint(1900, 2023)
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "6":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.choice(["0", "00", "000", "0000"])
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()
            
        elif menu == "7":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.choice(["111", "222", "333", "444", "555", "666", "777", "888", "999"])
                    
                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

        elif menu == "8":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))

            print("Genere combinación")
            print("1 = Solo Izquierda")
            print("2 = Solo Derecha")
            print("3 = Ambas")
            combo_option = input("Eliga su Opción: ")
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    rname = names.get_first_name()
                    rlastname = names.get_last_name()
                    num = random.choice(["12", "123", "1234", "12345", "13456", "1234567", "12345678", "123456789", "987654321","87654321", "7654321", "654321", "54321", "4321", "321", "21"])

                    if combo_option == "1":
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}"
                    elif combo_option == "2":
                        all1 = f"{rname}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}"
                        allf = f"{all2}:{rlastname}{num}"
                    else:
                        all1 = f"{rname}{num}"
                        alln = f"{all1}:{rname}{num}"
                        all2 = f"{rlastname}{num}"
                        allf = f"{all2}:{rlastname}{num}"

                    line1 = alln + "\n"
                    line2 = allf + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()
           
        elif menu == "9":
            print("\t\t (.txt) escriba ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas (x2): "))
            
            lines_set = set()

            with tqdm(total=hwm, desc="Progreso", ncols=70) as pbar:
                while len(lines_set) < hwm * 2:
                    first_name = names.get_first_name()
                    last_name = names.get_last_name()
                    numbers1 = random.choice(["123", "1234", "12345", "123456", "321", "4321", "54321", "654321", "1020", "102030"])
                    numbers2 = random.choice(["123", "1234", "12345", "123456", "321", "4321", "54321", "654321", "1020", "102030"])
                    all1 = f"{first_name}:{numbers1}"
                    all2 = f"{last_name}:{numbers2}"
                    line1 = all1 + "\n"
                    line2 = all2 + "\n"
                    
                    if line1 not in lines_set:
                        lines_set.add(line1)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)
                    
            print()

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    
