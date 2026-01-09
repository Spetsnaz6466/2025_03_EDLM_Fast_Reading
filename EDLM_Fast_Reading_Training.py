import os,csv,time

# TXT files: https://www.gutenberg.org/

def intro():
    os.system("clear")
    os.system("explorer.exe .")
    print("\n#   INTRO   #")
    print("This program was designed as a tool for Speed Reading. In order to do so it")
    print("reads a TXT file on UTF format and print it by lines or chunks of a line")
    print("TXT files can be found on https://www.gutenberg.org")
    print("[ ]: Line number\n")
    print("Printing files on the current working directory")
    os.system("ls -lsa")

def _fileByParragraph(book,line__):
    """
    Get a text book and a line where to start presenting the
    book by parragraphs printed line by line
    """
    _count = 0    # Line counter
    _time = 0     # Time counter
    with open(book) as file0:
        file1 = csv.reader(file0)
        for i in file1:
            _count +=1
            if int(line__) <= _count:
                #print(i)
                if i == []:
                    time.sleep(3)
                    os.system("clear")
                else:
                    a=0    # List element counter
                    _line = ""
                    print(f'[{_count}] ', end="")
                    while a <= len(i)-1:
                        if a == 0:
                            _line = _line + i[a]
                        else:
                            _line = _line + ", " + i[a]
                        if len(i[a]) > 60:
                            _time =_time  + 5
                        elif len(i[a]) > 30:
                            _time =_time + 4
                        else:
                             _time =_time + 1
                        a+=1
                    print(_line)
                    time.sleep(_time)
                    _line, _time = 0, 0


def _fileLineByLine(book,line__):
    """
    Get a text book and a line where to start presenting the lines
    """
    _count = 0    # Line counter
    _time = 0     # Time counter
    with open(book) as file0:
        file1 = csv.reader(file0)
        for i in file1:
            _count +=1
            if line__ <= _count:
                #print(i)
                if i == []:
                    # Limpiar la pantalla si es una linea en blanco (nuevo parrafo)
                    time.sleep(3)
                    os.system("clear")
                else:
                    a=0    # List element counter
                    _line = ""
                    # Como referencia Se imprime el numero de linea [{_count}]
                    print(f'[{_count}] ', end="")
                    while a <= len(i)-1:
                        print("aaa  ",i[a], end="")
                        if len(i[a]) > 60:
                            _time =_time  + 5
                        elif len(i[a]) > 30:
                            _time =_time + 4
                        else:
                             _time =_time + 3
                        a+=1
                    print("bbb   ",_line)
                    time.sleep(_time)
                    _line, _time = 0, 0

def _fileNormalReading(book,line__):
    """
    Get a text book and a line where to start presenting the lines
    """
    _count = 0    # Line counter
    with open(book) as file0:
        file1 = csv.reader(file0)
        os.system("clear")
        for i in file1:
            _count +=1
            linea =""
            if i == []:
                os.system("clear")
            elif int(line__) <= _count:
                if len(i) == 1:
                    linea = i[0]
                elif len(i) > 1:
                    for row in range(len(i)):
                        if row != len(i)-1:
                            linea = linea + i[row]  + ","
                        else: linea = linea + i[row]
                print(f'[{_count}] ', linea , end = " ")
                input()


if __name__ == "__main__":
    intro()
    book = input("Input text file for reading: ")
    default = 0
    line__ = input("Input text line number [0 = File Begin]: ")
    if line__ =="":
        line__ = default
        print("Begin selected...")
    default = "l"
    opcion = input("Read text by Parragraph ( p ) / line( l ) / Normal ( n ) : ")
    if opcion == "":
        opcion = default
        print("Line selected ...")
    if opcion =="p" :
        _fileByParragraph(book,line__)
    elif opcion == "l" :
        _fileLineByLine(book,line__)
    elif opcion == "n" :
        _fileNormalReading(book,line__)
