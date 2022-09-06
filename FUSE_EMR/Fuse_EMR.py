
import os

# Instructions: 
# #1): Copy your Tp on TP variable
# #2): Son 'slector' variable type the shop you are working, dont use capital letters 
# #3): On console see the adrees you need
TP = 'I:\\engineering\dev\\team_func\\esomarri\EMR\\PO_minus11'
print('Your TP:', TP)
xcc_fuse = '\\EnvironmentFile_CLASS_EMR_MCCSP.env'
mcc_fuse = '\\EnvironmentFile_CLASS_EMR_MCCSP.env'
selector = 'mcc'


# VAriable for the SCRIPT 
lineas = []
lineas_fuse =[]
fuse_dir = []
dir_fuse = []
final_addres = []
addres = []
adrees_num = []
adrees_num1 = []
adrees_num2 = []
adrees_int = []
adrees_str = []
int_address = []
int_address1 = []

if selector == 'mcc': 
    print("Working on MCC")
    print('\n')
    def open_TP():
        fuse_file = TP +  mcc_fuse
        archivo = open( fuse_file, 'r')
        for linea in archivo.readlines(): 
            lineas.append(linea)
            if 'FUSE_ROOT_DIR' in linea:
                print(lineas[1])
        #return lineas 
    open_TP() 

    def get_fuse_dir():
        fuse_dir.append(lineas[1].split())
        print('DIR Fuse:',fuse_dir[0][2])
        dir_fuse.append(fuse_dir[0][2]) # fuse direction 
    get_fuse_dir()

    def open_TP():
        print('***** FUSE Info *****')
        print('\n')
        str_dir_fuse = str(dir_fuse[0]).replace('"','').replace(';','')
        #print('STR:', str_dir_fuse)
        dir_file = str(str_dir_fuse) + "\\fusedef.txt" 
        #print('File:', dir_file)

        file = open(dir_file) 
        content = file.readlines() 
        adrees_str = content[18160].replace(':','')
        addres.append(adrees_str.split())
        print(' FULL Addres:',addres)
        print(' Addres:',addres[0][2]) 
        adrees_num = addres[0][2].split('-')
        adrees_num1 = str(adrees_num).replace(':','')
        adrees_num2 = adrees_num1.replace(':','')
        int_address.append(adrees_num2)
        initial_list = adrees_num2

        op = initial_list.strip('][').split(', ')

        int1 = int(op[0].replace("'", " "))
        int2 = int(op[1].replace("'", " "))
        print("Addres #1: ", int1)
        print("Addres #2: ", int2)
        if int1<int2:
            print(int1,'is smaller than',int2)
        elif int1 > int2:
            print(int2,'is smaller than',int1)  
    open_TP() 

if selector == 'xcc': 
    print("Working on XCC")
    print('\n')
    def open_TP():
        fuse_file = TP +  xcc_fuse
        archivo = open( fuse_file, 'r')
        for linea in archivo.readlines(): 
            lineas.append(linea)
            if 'FUSE_ROOT_DIR' in linea:
                print(lineas[1])
        #return lineas 
    open_TP() 

    def get_fuse_dir():
        fuse_dir.append(lineas[1].split())
        print('DIR Fuse:',fuse_dir[0][2])
        dir_fuse.append(fuse_dir[0][2]) # fuse direction 
    get_fuse_dir()

    def open_TP():
        print('***** FUSE Info *****')
        print('\n')
        str_dir_fuse = str(dir_fuse[0]).replace('"','').replace(';','')
        #print('STR:', str_dir_fuse)
        dir_file = str(str_dir_fuse) + "\\fusedef.txt" 
        #print('File:', dir_file)

        file = open(dir_file) 
        content = file.readlines() 
        adrees_str = content[18160].replace(':','')
        addres.append(adrees_str.split())
        print(' FULL Addres:',addres)
        print(' Addres:',addres[0][2]) 
        adrees_num = addres[0][2].split('-')
        adrees_num1 = str(adrees_num).replace(':','')
        adrees_num2 = adrees_num1.replace(':','')
        int_address.append(adrees_num2)
        initial_list = adrees_num2

        op = initial_list.strip('][').split(', ')

        int1 = int(op[0].replace("'", " "))
        int2 = int(op[1].replace("'", " "))
        print("Addres #1: ", int1)
        print("Addres #2: ", int2)
        if int1<int2:
            print(int1,'is smaller than',int2)
        elif int1 > int2:
            print(int2,'is smaller than',int1)  
    open_TP() 