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

        directory = "/sdcard/choller"
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

import time
import sys

texto   = """
  ___       _              _     
 | __> _ _ <_> ___ ._ _  _| | ___
 | _> | '_>| |/ ._>| ' |/ . |<_-<
 |_|  |_|  |_|\___.|_|_|\___|/__/
  ___       _              _ 
 / __> ___ | |_  ___  ___ | |
 \__ \/ | '| . |/ . \/ . \| |
 <___/\_|_.|_|_|\___/\___/|_|
  _   _                   _         __   
 ( ) ( ) _               (_ )     /'__`\ 
 | `\| |(_) _   _    __   | |    (_)  ) )
 | , ` || |( ) ( ) /'__`\ | |       /' / 
 | |`\ || || \_/ |(  ___/ | |     /' /( )
 (_) (_)(_)`\___/'`\____)(___)   (_____/'
                                                                                
  ___    _         ___            _ 
 / __> _| |_  ___ | | ' ___ ._ _ <_>
 \__ \  | |  / ._>| |- <_> || ' || |
 <___/  |_|  \___.|_|  <___||_|_||_|                     """
                                    
                                                                        

for caracter in texto:
    sys.stdout.write("\033[95m" + caracter + "\033[0m")
    sys.stdout.flush()
    time.sleep(0.05)
    
    




print("\033[95m" + "𝚀𝚞𝚎 𝚃𝚒𝚙𝚘 𝚍𝚎 𝙲𝚘𝚖𝚋𝚘 𝚍𝚎𝚜𝚎𝚊 𝚌𝚛𝚎𝚊𝚛?" + "\033[0m\n")
print("\033[92m" + "1) NOMBRE:NOMBRE(Mix)" + "\033[0m\n")
print("\033[93m" + "2) NOMBRES (CON AÑO DE NACIMIENTO)" + "\033[0m\n")
print("\033[94m" + "3) NOMBRES (CON NÚMEROS 123 AL 12345)" + "\033[0m\n")
print("\033[95m" + "4) NOMBRES (10 Digitos)" + "\033[0m\n")
print("\033[96m" + "5) CREA UN COMBO CON TU LISTA" + "\033[0m\n")
print("\033[91m" + "6) ELIMINAR LINEAS DUPLICADAS" + "\033[0m\n")
print("\033[97m" + "7) NOMBRES (Mayusculas,Minusculas)" + "\033[0m\n")
print("\033[93m" + "Ejemplo: Juan juan" + "\033[0m")

menu = input("Ingresar opción :")


		

if menu=="1":
	print ("\t\t\33[1;33m  crea su combo\33[36m ")
	filename = input("\nNombre su Combo  :  ")
	hwm = int(input("cuantas lineas? : "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1,100000)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		all3 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all3,":",rname,num)
		all4 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all4,":",rlastname,num)
		all5 = "%s%s"%(rname,2023)
		alls = "%s%s%s%s"%(all5,":",rname,2023)
		all6 = "%s%s"%(rlastname,2023)
		allg = "%s%s%s%s"%(all6,":",rlastname,2023)
		all7 = "%s%s"%(rname,2024)
		alle = "%s%s%s%s"%(all7,":",rname,2024)
		all8 = "%s%s"%(rlastname,2024)
		alld = "%s%s%s%s"%(all8,":",rlastname,2024)
		all9 = "%s"%(rname)
		allt = "%s%s%s"%(all9,":",rname)
		all10 = "%s"%(rlastname)
		ally = "%s%s%s"%(all10,":",rlastname)
		all11 = "%s%s"%(rname,123)
		allp = "%s%s%s%s"%(all11,":",rname,123)
		all12 = "%s%s"%(rlastname,123)
		allj = "%s%s%s%s"%(all12,":",rlastname,123)
		all13 = "%s"%(num)
		allv = "%s%s%s"%(all13,":",num)
		print(alln)
		print(allf)
		print(alln.lower())
		print(allf.lower())
		print(alls.upper())
		print(allg.upper())
		print(alle.lower())
		print(alld.lower())
		print(allt.lower())
		print(ally.lower())
		print(allt)
		print(ally)
		print(allp.lower())
		print(allj.lower())
		print(allv)
		F ="/sdcard/combo/"+filename+".txt"
		f = open(F, "a+",encoding= "utf-8")
		f.write(alln)
		f.write("\n")
		f.write(allf)
		f.write("\n")
		f.write(alln.lower())
		f.write("\n")
		f.write(allf.lower())
		f.write("\n")
		f.write(alls.upper())
		f.write("\n")
		f.write(allg.upper())
		f.write("\n")
		f.write(alle.lower())
		f.write("\n")
		f.write(alld.lower())
		f.write("\n")
		f.write(allt.lower())
		f.write("\n")
		f.write(ally.lower())
		f.write("\n")
		f.write(allt.upper())
		f.write("\n")
		f.write(ally.upper())
		f.write("\n")
		f.write(allp.lower())
		f.write("\n")
		f.write(allj.lower())
		f.write("\n")
		f.write(allp.upper())
		f.write("\n")
		f.write(allj.upper())
		f.write("\n")
		f.write(allv)
		f.write("\n")
		f.close()
		i = 1
		
	output_file = input("\n\33[33msu archivo de texto se guardara\nen carpeta combo\n\33[36m ")
	
if menu=="7":
	print ("\t\t\33[1;336m (.txt) escriba \33[36m ")
	filename = input("\nNombre su Combo  : ")
	hwm = int(input("numero de lineas : "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,0)
		all1 = "%s"%(rname)
		alln = "%s%s"%(all1," ",)
		all2 = "%s"%(rname)
		alln = "%s%s"%(all2," ",) 
		all3 = "%s"%(rname)
		alle = "%s%s"%(all3," ",)
		 
		
		print(alln)
		print(alln.lower())
		print(alle.upper())
		F ="/sdcard/combo/"+filename+".txt"
		f = open(F, "a+",encoding= "utf-8")
		f.write(alln)
		f.write("\n")
		f.write(alln.lower())
		f.write("\n")
		f.write(alle.upper())
		f.write("\n")

		f.close()
		i += 1

if menu == "6":
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
            
if menu == "2":
            print("\t\t  ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas : "))

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
                    num = random.randint(1900, 2024)
                    
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
                        with open(f"/sdcard/combo/"+filename+".txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/combo/"+filename+".txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)
           

            print()

if menu == "3":
            print("\t\t  ")
            filename = input("\nNombre de su Combo: ")
            hwm = int(input("Número de líneas : "))

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
                        with open(f"/sdcard/combo/"+filename+".txt", "a+", encoding="utf-8") as f:
                            f.write(line1)

                    if line2 not in lines_set:
                        lines_set.add(line2)
                        with open(f"/sdcard/combo/"+filename+".txt", "a+", encoding="utf-8") as f:
                            f.write(line2)

                    pbar.update(1)
                    time.sleep(0.1)

            print()

if menu == "5":
        file_path = input("Ingrese la ruta de su archivo .txt ('10' para retroceder): ")
        if file_path == "10":
            print("Volviendo al menú principal...\n")
            main()
        hwm = int(input("Número de líneas : "))

        while True:
            print("""
            \33[33m
SUBMENÚ - CREA UN COMBO CON TU LISTA
            
      1) USUARIO:CONTRASEÑA 2000 AL 2024
      2) USUARIO:CONTRASEÑA NOMBRE-NOMBRE
      3) USUARIO:CONTRASEÑA DEL 1 AL 499
      4) USUARIO:CONTRASEÑA DEL 500 AL 999
      5) USUARIO:CONTRASEÑA AÑO DE NACIMIENTO
      6) USUARIO:CONTRASEÑA DEL 0 AL 0000
      7) USUARIO:CONTRASEÑA 111, 222, ..., 999
      8) USUARIO:CONTRASEÑA 123, 1234, 12345..
      9) USUARIO:CONTRASEÑA 123 AL 123456 

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
                            num = random.randint(2000, 2024)
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

                        with open(f"/sdcard/combo/{filename}@.txt", "a+", encoding="utf-8") as f:
                            f.write(alln + "\n")
                        pbar.update(1)
                        time.sleep(0.1)

                print(f"\nNombre de su archivo combo: {filename}@.txt")


            elif submenu_option == "10":
                break
            else:
                print("Opción no válida. Por favor, elija una opción del submenú.")

                main()    
                      
print()

if menu=="4":
	c = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
n = int(input("""   \33[0m\n\nIngrese la cantidad que desea: """))
print (" ")
print (" ")
print ("\t\t\33[1;100m No pongas (.txt) \33[0m ")
filename = input("\nnombre el combo: ")
filename = filename + ".txt"
print (" ")



f = open(filename, "w")
f.write("")
f.close()



i = 1

while i <= n:
   g1=random.randint(0,61)
   g2=random.randint(0,61)
   g3=random.randint(0,61)
   g4=random.randint(0,61)
   g5=random.randint(0,61)
   g6=random.randint(0,61)
   g7=random.randint(0,61)
   g8=random.randint(0,61)
   g9=random.randint(0,61)
   g10=random.randint(0,61)
   c1 = c[g1]
   c2 = c[g2]
   c3 = c[g3]
   c4 = c[g4]
   c5 = c[g5]
   c6 = c[g6]
   c7 = c[g7]
   c8 = c[g8]
   c9 = c[g9]
   c10 = c[g10]
   user = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
   g1=random.randint(1,61)
   g2=random.randint(1,61)
   g3=random.randint(1,61)
   g4=random.randint(1,61)
   g5=random.randint(1,61)
   g6=random.randint(1,61)
   g7=random.randint(1,61)
   g8=random.randint(1,61)
   g9=random.randint(1,61)
   g10=random.randint(1,61)
   c1 = c[g1]
   c2 = c[g2]
   c3 = c[g3]
   c4 = c[g4]
   c5 = c[g5]
   c6 = c[g6]
   c7 = c[g7]
   c8 = c[g8]
   c9 = c[g9]
   c10 = c[g10]
   pw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
   user=user+":"+pw 
   print(i," = ",user)
   f = open(filename, "a")
   f.write(user)
   f.write("\n")
   f.close()
   i += 1
   


print ("\33[1;37;42m")
print (n," Archivo guardado exitosamente: ",filename,)
print ("\33[0m")

print()

if menu=="0":

     x = input("\n \33[33m YA ESTAS LISTO TU NUEVO COMBO...")
