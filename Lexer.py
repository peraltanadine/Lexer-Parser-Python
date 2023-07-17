# importar librerias
import os
import ply.lex as lex
import ply.yacc as yacc
from tkinter import *
from tkinter import ttk, messagebox, filedialog


#~(ºoº)~

# Para darle jerarquía a los títulos
formato_imp = False
formato_sec = False
formato_inf = False

# Para darle jerarquía a las tablas
formato_head = False
formato_foot = False
formato_body = False

#Para diferenciar infos de section y article con los de media
formato_media = False

tokens = ('DOC', 'TEXT', 'SALTO',
          'A_ARTICLE', 'C_ARTICLE',
          'A_INFO', 'C_INFO',
          'A_TITLE', 'C_TITLE',
          'A_EMAIL', 'C_EMAIL',
          'A_STREET', 'C_STREET',
          'A_CITY', 'C_CITY', 'A_STATE',
          'C_STATE', 'A_PHONE', 'C_PHONE',
          'A_COPY', 'C_COPY', 'A_YEAR',
          'C_YEAR', 'A_HOLDER', 'C_HOLDER',
          'A_AUTHOR', 'C_AUTHOR',
          'A_DATE', 'C_DATE',
          'A_FNAME', 'C_FNAME',
          'A_SNAME', 'C_SNAME',
          'A_SECT', 'C_SECT',
          'A_SIMSECT', 'C_SIMSECT',
          'A_ABSTRACT', 'C_ABSTRACT',
          'A_PARA', 'C_PARA',
          'A_SIMPARA', 'C_SIMPARA',
          'A_IMPORT', 'C_IMPORT',
          'A_COMMENT', 'C_COMMENT',
          'A_EMPHA', 'C_EMPHA',
          'A_MEDIA', 'C_MEDIA',
          'C_MEDIABRACKET',
          'A_IMAGE', 'C_IMAGE',
          'A_IMAGED', 'A_VIDEO',
          'C_VIDEO', 'A_VIDEOD',
          'C_URLLINK', 'URL', 'MURL',
          'A_LINK', 'C_LINK',
          'A_ILIST', 'C_ILIST',
          'A_ITEM', 'C_ITEM',
          'A_TABLE', 'C_TABLE',
          'A_TGROUP', 'C_TGROUP',
          'A_THEAD', 'C_THEAD',
          'A_TFOOT', 'C_TFOOT',
          'A_TBODY', 'C_TBODY',
          'A_ROW', 'C_ROW',
          'A_ENTRYTBL', 'C_ENTRYTBL',
          'A_ENTRY', 'C_ENTRY', 'ERROR',
          'A_ADDRESS', 'C_ADDRESS', 'TABULADO', 'ESPACIO',
          )

file = ""
# Funciones del LEXER
def t_SALTO(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    file.write(os.linesep)


def t_DOC(t):
    r'<!DOCTYPE\s+article>'
    file.write("<!DOCTYPE html>")
    return t


def t_A_ARTICLE(t):
    r'<article>'
    file.write("<html>\n<head>\n</head>\n\t<body>")
    return t


def t_C_ARTICLE(t):
    r'</article>'
    file.write("\n\t</body>\n</html>")
    return t


def t_A_INFO(t):
    r'<info>'
    global formato_inf, formato_media
    if formato_media:
        formato_inf = True
        file.write(" ")
    else:
        formato_inf = True
        formato1 = """<p style="background-color: green"><font size ="8px" color = "white"> """
        file.write(formato1)
    return t


def t_C_INFO(t):
    r'</info>'
    global formato_inf, formato_media
    if formato_media:
        file.write(" ")
        formato_inf = False
    else:
        formato_inf = False
        file.write("</font>\n</p>")
    return t


def t_A_TITLE(t):
    r'<title>'
    global formato_imp, formato_sec,formato_inf
    if formato_inf:
        file.write(" ")
    else:
        if formato_imp:
            file.write("<h3>")
        else:
            if formato_sec:
                file.write("<h2>")
            else:
                file.write("<h1>")
    return t


def t_C_TITLE(t):
    r'</title>'
    global formato_imp, formato_sec, formato_inf
    if formato_inf:
        file.write(" ")
    else:
        if formato_imp:
            file.write("</h3>")
        else:
            if formato_sec:
                file.write("</h2>")
            else:
                file.write("</h1>")
    return t


def t_A_ADDRESS(t):
    r'<address>'
    return t


def t_C_ADDRESS(t):
    r'</address>'
    return t


def t_A_STREET(t):
    r'<street>'
    return t


def t_C_STREET(t):
    r'</street>'
    return t


def t_A_CITY(t):
    r'<city>'
    return t


def t_C_CITY(t):
    r'</city>'
    return t


def t_A_STATE(t):
    r'<state>'
    return t


def t_C_STATE(t):
    r'</state>'
    return t


def t_A_PHONE(t):
    r'<phone>'
    return t


def t_C_PHONE(t):
    r'</phone>'
    return t


def t_A_DATE(t):
    r'<date>'
    return t


def t_C_DATE(t):
    r'</date>'
    return t


def t_A_EMAIL(t):
    r'<email>'
    return t


def t_C_EMAIL(t):
    r'</email>'
    return t


def t_A_AUTHOR(t):
    r'<author>'
    return t


def t_C_AUTHOR(t):
    r'</author>'
    return t


def t_A_FNAME(t):
    r'<firstname>'
    return t


def t_C_FNAME(t):
    r'</firstname>'
    return t


def t_A_SNAME(t):
    r'<surname>'
    return t


def t_C_SNAME(t):
    r'</surname>'
    return t


def t_A_COPY(t):
    r'<copyright>'
    return t


def t_C_COPY(t):
    r'</copyright>'
    return t


def t_A_YEAR(t):
    r'<year>'
    return t


def t_C_YEAR(t):
    r'</year>'
    return t


def t_A_HOLDER(t):
    r'<holder>'
    return t


def t_C_HOLDER(t):
    r'</holder>'
    return t

def t_A_SECT(t):
    r'<section>'
    global formato_sec
    formato_sec = True
    file.write("<section>")
    return t


def t_C_SECT(t):
    r'</section>'
    global formato_sec
    formato_sec = False
    file.write("</section>")
    return t


def t_A_SIMSECT(t):
    r'<simplesect>'
    global formato_sec
    formato_sec = True
    file.write("<section>")
    return t


def t_C_SIMSECT(t):
    r'</simplesect>'
    global formato_sec
    formato_sec = False
    file.write("</section>")
    return t


def t_A_ABSTRACT(t):
    r'<abstract>'
    global formato_imp
    formato_imp = True
    return t


def t_C_ABSTRACT(t):
    r'</abstract>'
    global formato_imp
    formato_imp = False
    return t


def t_A_PARA(t):
    r'<para>'
    global formato_inf
    if formato_inf:
        file.write(" ")
    else:
        file.write("<p>")
    return t


def t_C_PARA(t):
    r'</para>'
    global formato_inf
    if formato_inf:
        file.write(" ")
    else:
        file.write("</p>")
    return t


def t_A_SIMPARA(t):
    r'<simpara>'
    global formato_inf
    if formato_inf:
        file.write(" ")
    else:
        file.write("<p>")
    return t


def t_C_SIMPARA(t):
    r'</simpara>'
    global formato_inf
    if formato_inf:
        file.write(" ")
    else:
        file.write("</p>")
    return t

#La  etiqueta important no tiene un igual en html, por lo que se decidio usar aside por sus mayor parecido
def t_A_IMPORT(t):
    r'<important>'
    global formato_imp
    formato_imp = True
    formato2 = """<aside style="background-color: red"><font color = "white"> """
    file.write(formato2)
    return t


def t_C_IMPORT(t):
    r'</important>'
    global formato_imp
    formato_imp = False
    file.write("\n</font>\n</aside>")
    return t

#Decidimos usar Negrita por razones esteticas
def t_A_COMMENT(t):
    r'<comment>'
    return t


def t_C_COMMENT(t):
    r'</comment>'
    return t


def t_A_EMPHA(t):
    r'<emphasis>'
    return t


def t_C_EMPHA(t):
    r'</emphasis>'
    return t


def t_C_MEDIABRACKET(t):
    r'/>'
    file.write(">")
    return t


def t_A_MEDIA(t):
    r'<mediaobject>'
    global formato_media
    formato_media = True
    return t


def t_C_MEDIA(t):
    r'</mediaobject>'
    global formato_media
    formato_media = False
    return t


def t_A_IMAGE(t):
    r'<imageobject>'
    return t


def t_C_IMAGE(t):
    r'</imageobject>'
    return t


def t_A_IMAGED(t):
    r'<imagedata\s+fileref='
    formatoimg = '''<img src='''
    file.write(formatoimg)
    return t


def t_A_VIDEO(t):
    r'<videoobject>'
    file.write("<video>")
    return t


def t_C_VIDEO(t):
    r'</videoobject>'
    file.write("</video>")
    return t


def t_A_VIDEOD(t):
    r'<videodata\s+fileref='
    formatovid = '''<source src='''
    file.write(formatovid)
    return t


def t_URL(t): #ACEPTA URLS ABSOLUTAS
    r'\"(http|https|ftp|ftps)://[^/\s:]+(:\d+)?(/[^#\s]*)?(\#\S*)?\"'
    file.write(t.value)
    return t

def t_MURL(t):
    r'\"([\/*[a-zA-Z0-9]*\.(gif|jpg|jpeg|png|bmp|svg|mp4|avi|mov)?)\"'
    file.write(t.value)
    return t
def t_A_LINK(t):
    r'<link\s+xlink:href= '
    formato3 = """<a href= """
    file.write(formato3)
    return t


def t_C_URLLINK(t):
    r' >'
    formato4 = """ > """
    file.write(formato4)
    return t


def t_C_LINK(t):
    r'</link>'
    file.write("</a>")
    return t


def t_A_ILIST(t):
    r'<itemizedlist>'
    file.write("<ul>")
    return t


def t_C_ILIST(t):
    r'</itemizedlist>'
    file.write("</ul>")
    return t


def t_A_ITEM(t):
    r'<listitem>'
    file.write("<li>")
    return t


def t_C_ITEM(t):
    r'</listitem>'
    file.write("</li>")
    return t


def t_A_TABLE(t):
    r'<informaltable>'
    formato5 = '''<table style="border: black 2px solid;">'''
    file.write(formato5)
    return t


def t_C_TABLE(t):
    r'</informaltable>'
    file.write("</table>")
    return t


def t_A_TGROUP(t):
    r'<tgroup>'
    return t


def t_C_TGROUP(t):
    r'</tgroup>'
    return t


def t_A_THEAD(t):
    r'<thead>'
    global formato_head
    formato_head = True
    file.write("<thead>")
    return t


def t_C_THEAD(t):
    r'</thead>'
    global formato_head
    formato_head = False
    file.write("</thead>")
    return t


def t_A_TFOOT(t):
    r'<tfoot>'
    global formato_foot
    formato_foot = True
    file.write("<tfoot>")
    return t


def t_C_TFOOT(t):
    r'</tfoot>'
    global formato_foot
    formato_foot = False
    file.write("</tfoot>")
    return t


def t_A_TBODY(t):
    r'<tbody>'
    global formato_body
    formato_body = True
    file.write("<tbody>")
    return t


def t_C_TBODY(t):
    r'</tbody>'
    global formato_body
    formato_body = False
    file.write("</tbody>")
    return t


def t_A_ROW(t):
    r'<row>'
    file.write("<tr>")
    return t


def t_C_ROW(t):
    r'</row>'
    file.write("</tr>")
    return t


def t_A_ENTRYTBL(t):
    r'<entrytbl>'
    return t


def t_C_ENTRYTBL(t):
    r'</entrytbl>'
    return t


# No encontramos la exacta equivalente en HTML
def t_A_ENTRY(t):
    r'<entry>'
    global formato_body, formato_foot, formato_head
    formato6 = ''' <td style="border: black 1px solid;"> '''
    formato7 = ''' <th style="border: black 1px solid;"> '''
    if formato_foot:
        file.write(formato6)
    else:
        if formato_body:
            file.write(formato6)
        else:
            file.write(formato7)
    return t


def t_C_ENTRY(t):
    r'</entry>'
    global formato_body, formato_foot, formato_head

    if formato_foot:
        file.write('</td>')
    else:
        if formato_body:
            file.write('</td>')
        else:
            file.write('</th>')
    return t


def t_TAB(t):
    r'\t'
    file.write("\t")
    pass


def t_ESPACIO(t):
    r'\ '
    file.write(" ")
    pass


t_ignore = '\r'

def t_TEXT(t):
    r'[^<>]+'
    file.write(t.value)
    return t

# Control de errores de caracteres inválidos
def t_error(t):
    t.lexer.skip(1)


# Control de errores de token mal escrito
def t_ERROR(t):
    # esta expresion regular toma una cadena que comience por < seguida por caracteres que no sean >, termina en >,
    # si no hay ningun otro token que cumpla la condicion sera marcado como ERROR
    r'<[^>]+>'
    msjError = f"Error léxico: Token mal escrito {t.value}\n"
    OutputBox.insert("end", msjError)
    return t


lexer = lex.lex()


# Funciones del PARSER
# MAYUSCULA TERMINALES (TOKENS) minuscula no terminales
def p_sigma(p):
    '''sigma : DOC A_ARTICLE info title cont C_ARTICLE
    | DOC A_ARTICLE title cont C_ARTICLE
    | DOC A_ARTICLE info cont C_ARTICLE
    | DOC A_ARTICLE cont C_ARTICLE '''

def p_info(p):
    '''info : A_INFO dtinfo C_INFO '''

def p_dtinfo(p):
    '''dtinfo : title
       | author
       | abstract
       | abstract dtinfo
       | media
       | media dtinfo
       | title dtinfo
       | author dtinfo
       | address
       | copy
       | date
       | address dtinfo
       | copy dtinfo
       | date dtinfo '''

def p_title(p):
    '''title : A_TITLE  tlt C_TITLE '''

def p_tlt(p):
    '''tlt : TEXT
    | empha
    | link
    | email
    | TEXT tlt
    | empha tlt
    | link tlt
    | email tlt '''

def p_empha(p):
    '''empha : A_EMPHA sp C_EMPHA '''


def p_sp(p):
    ''' sp : TEXT sp
    | link sp
    | email sp
    | empha sp
    | comment sp
    | author sp
    | TEXT
    | link
    | email
    | empha
    | comment
    | author  '''


def p_link(p):
    '''link : A_LINK URL C_URLLINK sp C_LINK
     | A_LINK MURL C_URLLINK sp C_LINK '''


def p_email(p):
    '''email : A_EMAIL nm C_EMAIL '''


def p_nm(p):
    '''nm : TEXT
    | link
    | empha
    | comment
    | TEXT nm
    | link nm
    | empha nm
    | comment nm '''


def p_comment(p):
    '''comment : A_COMMENT sp C_COMMENT '''

def p_author(p):
    '''author : A_AUTHOR names C_AUTHOR '''


def p_names(p):
    '''names : fname
    | sname
    | fname names'''


def p_fname(p):
    '''fname : A_FNAME nm C_FNAME '''


def p_sname(p):
    '''sname : A_SNAME nm C_SNAME '''


def p_address(p):
    '''address : A_ADDRESS contad C_ADDRESS'''


def p_contad(p):
    '''contad : TEXT
        | street
        | city
        | state
        | street contad
        | city contad
        | state contad
        | phone
        | email
        | TEXT contad
        | phone contad
        | email contad '''


def p_street(p):
    '''street : A_STREET nm C_STREET '''


def p_city(p):
    '''city : A_CITY nm C_CITY '''


def p_state(p):
    '''state : A_STATE nm C_STATE '''


def p_phone(p):
    '''phone : A_PHONE nm C_PHONE '''


def p_copy(p):
    '''copy : A_COPY year holder C_COPY
    | A_COPY year C_COPY '''


def p_year(p):
    '''year : A_YEAR nm C_YEAR
        | A_YEAR nm C_YEAR year'''


def p_holder(p):
    '''holder : A_HOLDER nm C_HOLDER
    | A_HOLDER nm C_HOLDER holder '''


def p_date(p):
    '''date : A_DATE nm C_DATE'''

def p_cont(p):
    '''cont : data sections
    | data '''

def p_data(p):
    '''data : simpara
    | para
    | ilist
    | table
    | media
    | import
    | abstract
    | comment
    | simpara data
    | para data
    | ilist data
    | table data
    | media data
    | import data
    | abstract data
    | comment data '''


def p_simpara(p):
    '''simpara : A_SIMPARA sp C_SIMPARA '''


def p_para(p):
    '''para : A_PARA dtp C_PARA '''


def p_dtp(p):
    '''dtp : TEXT dtp
        | empha dtp
        | link dtp
        | email dtp
        | author dtp
        | comment dtp
        | ilist dtp
        | import dtp
        | table dtp
        | media dtp
        | TEXT
        | empha
        | link
        | email
        | author
        | comment
        | ilist
        | import
        | table
        | media '''

#<(￣︶￣)>

def p_ilist(p):
    '''ilist : A_ILIST item C_ILIST  '''

def p_item(p):
    '''item : A_ITEM dlist C_ITEM
    | A_ITEM dlist C_ITEM item '''


def p_dlist(p):
    '''dlist : import
    | para
    | simpara
    | ilist
    | table
    | media
    | comment
    | abstract
    | address
    | address dlist
    | import dlist
    | para dlist
    | simpara dlist
    | ilist dlist
    | table dlist
    | media dlist
    | comment dlist
    | abstract dlist '''

def p_import(p):
    '''import : A_IMPORT title data C_IMPORT
        | A_IMPORT  data C_IMPORT '''

#(っ˘̩╭╮˘̩)っ

def p_table(p):
    '''table : A_TABLE tabdata C_TABLE '''



def p_tabdata(p):
    '''tabdata : media tabdata
        | tgroup tabdata
        | tgroup
        | media '''

def p_media(p):
    '''media : A_MEDIA info extramedia C_MEDIA
    | A_MEDIA extramedia C_MEDIA '''

def p_extramedia(p):
    '''extramedia : video extramedia
        | image extramedia
        | image
        | video   '''

def p_video(p):
    '''video : A_VIDEO info A_VIDEOD URL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO info A_VIDEOD MURL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO  A_VIDEOD MURL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO  A_VIDEOD URL C_MEDIABRACKET  C_VIDEO '''
def p_image(p):
    '''image : A_IMAGE info  A_IMAGED URL C_MEDIABRACKET C_IMAGE
    | A_IMAGE info  A_IMAGED MURL C_MEDIABRACKET C_IMAGE
    | A_IMAGE  A_IMAGED MURL C_MEDIABRACKET C_IMAGE
    | A_IMAGE  A_IMAGED URL C_MEDIABRACKET C_IMAGE '''

def p_tgroup(p):
    '''tgroup : A_TGROUP  thead tbody tfoot C_TGROUP
    | A_TGROUP  tbody  tfoot C_TGROUP
    | A_TGROUP  thead tbody  C_TGROUP
    | A_TGROUP  tbody  C_TGROUP '''

def p_thead(p):
    ''' thead : A_THEAD row C_THEAD'''

def p_row(p):
    '''row : A_ROW entry C_ROW row
    | A_ROW entrytbl C_ROW row
    | A_ROW entrytbl C_ROW
    | A_ROW entry C_ROW '''

def p_entry(p):
    '''entry : A_ENTRY dent C_ENTRY
    | A_ENTRY dent C_ENTRY entry
    | A_ENTRY dent C_ENTRY entrytbl '''

def p_dent(p):
    ''' dent : TEXT dent
    | ilist dent
    | import dent
    | para dent
    | simpara dent
    | media dent
    | comment dent
    | abstract dent
    | TEXT
    | ilist
    | import
    | para
    | simpara
    | media
    | comment
    | abstract '''

def p_abstract(p):
    '''abstract : A_ABSTRACT title dabs C_ABSTRACT
    | A_ABSTRACT dabs C_ABSTRACT'''

def p_dabs(p):
    ''' dabs : para dabs
    | simpara dabs
    | para
    | simpara '''

def p_entrytbl(p):
    '''entrytbl : A_ENTRYTBL thead tbody C_ENTRYTBL
    | A_ENTRYTBL thead tbody C_ENTRYTBL entry
    | A_ENTRYTBL thead tbody C_ENTRYTBL entrytbl'''

def p_tbody(p):
    ''' tbody : A_TBODY row C_TBODY '''

def p_tfoot(p):
    '''tfoot : A_TFOOT row C_TFOOT'''

def p_sections(p):
    ''' sections : sect sections
    | simsect sections
    | sect
    | simsect  '''

def p_sect(p):
    '''sect : A_SECT info title cont C_SECT
    | A_SECT info cont C_SECT
    | A_SECT title cont C_SECT
    | A_SECT cont C_SECT '''

def p_simsect(p):
    '''simsect : A_SIMSECT info title data C_SIMSECT
    | A_SIMSECT  title data C_SIMSECT
    | A_SIMSECT  info data C_SIMSECT
    | A_SIMSECT   data C_SIMSECT '''

def p_error(p):
    global errores
    if p:
        errorMsg = f"Error de sintaxis en línea {p.lineno}. Culpable: {p.value}\n"
        OutputBox.insert("end", errorMsg)
        parser.errok()
        errores += 1
    else:
        errorMsg = "Fin del archivo \n"
        OutputBox.insert("end", errorMsg)


# ¬(;_;)¬

# construir el parser
parser = yacc.yacc(errorlog=yacc.NullLogger()) #Esto para evitar que los warnings impidan la ejecucion del exe
xml_Name = "ARTICULO.xml"
entrada = ""
def Analisis():
    global entrada, file, errores
    entrada = TextBox.get("1.0", 'end-1c')
    if entrada == "":
        messagebox.showwarning("Aviso de Compilacion", "No hay estímulo")
    else:
        OutputBox.delete(1.0, END)
        errores = 0
        file = open(xml_Name.replace(".xml", ".html"), "w")
        lexer.lineno = 1
        parser.parse(entrada)
        file.close()
        if errores == 0:
            messagebox.showinfo("Aviso de Compilacion", "Analisis exitoso \n HTML generado")
        else:
            messagebox.showerror("Aviso de Compilacion", f"Analisis Finalizado, se encontraron errores {errores}")



def Examinar():
    global xml_Name
    Limpiar()
    xml_Name = filedialog.askopenfilename(initialdir="/./prueba", title="Seleccionar Articulo",filetypes=(("Archivo XML", "*.xml*"),("Todos los archivos", "*.*")))
    if not xml_Name.endswith(".xml"):
        messagebox.showerror("Aviso de Compilacion","Extension no admitida, seleccionar .XML")
    else:
        with open(xml_Name, "r", encoding="utf-8") as archivo:
            TextBox.insert('1.0', archivo.read())


# CODIGO DE INTERFAZ GRAFICA
directorio_actual = os.path.dirname(os.path.abspath("__file__"))  # Para obtener la ruta donde esta alojado el programa, volviendolo portable
Interfaz = Tk()
Interfaz.config(bg="#1c2242")
Interfaz.title("Lexer Docbook XML")
Icono = os.path.join(directorio_actual, 'LexerParser.ico')
Interfaz.iconbitmap(Icono)
Interfaz.resizable()  # Se puede agrandar o reducir

# Centrar la Interfaz al momento de abrirla
x = Interfaz.winfo_screenwidth()
y = Interfaz.winfo_screenheight()
w = (x / 2) - (1280 / 2)
h = (y / 2) - (720 / 2)
Interfaz.geometry(f"1280x720+{int(w)}+{int(h)}")

# Creamos los diferentes titulos y subtitulos de la interfaz, todos reescalables
Titulo = Label(text="Lexer DocBook XML")
Titulo.config(font=('Terminal 25 bold'), bg="#1c2242", fg="#e6e7f5")
Titulo.place(relx=0.5, rely=0.05, anchor=CENTER)

LabelInt = Label(text="Modo Interactivo (Consola)")
LabelInt.config(font=('Terminal 18 bold'), bg="#1c2242", fg="#e6e7f5")
LabelInt.place(relx=0.44, rely=0.15, anchor=E)

LabelOut = Label(text="Resultados")
LabelOut.config(font=('Terminal 18 bold'), bg="#1c2242", fg="#e6e7f5")
LabelOut.place(relx=0.68, rely=0.15, anchor=W)

# Las cajas de textos que recibiran el estimulo y mostrarán los tokens correspondientes
TextBox = Text(Interfaz, width=60, height=20, font=("Terminal", 15))
TextBox.place(relx=0.49, rely=0.5, relwidth=0.45, relheight=0.5, anchor=E)
OutputBox = Text(Interfaz, width=60, height=20, font=("Terminal", 15))
OutputBox.place(relx=0.51, rely=0.5, relwidth=0.45, relheight=0.5, anchor=W)


# Funcion implementada unicamente para la interfaz, permite limpiar la zona de texto, para poder cambiar de ejemplo
def Limpiar():
    global entrada, xml_Name
    TextBox.delete(1.0, END)
    OutputBox.delete(1.0, END)
    xml_Name = "ARTICULO.xml"
    entrada = ""

# Asignamos un estilo de boton por defecto
BotonPred = ttk.Style()
BotonPred.configure('New.TButton', font=('Terminal', 15, 'bold'), border=100, borderwidth=100, background='#701f1f',width=20, height=10)

# Creamos los botones para cada una de las acciones
Boton_Abrir = ttk.Button(text="Abrir Archivo", command=Examinar, style='New.TButton').place(relx=0.26, rely=0.8,anchor=E)
Boton_Token = ttk.Button(text="Iniciar Parser", command=Analisis, style='New.TButton').place(relx=0.45, rely=0.8,anchor=E)
Boton_Cerrar = ttk.Button(text="Cerrar", command=lambda: Interfaz.quit(), style='New.TButton').place(relx=0.75,rely=0.8, anchor=W)
Boton_LimpiarInput = ttk.Button(text="Limpiar", command=Limpiar, style='New.TButton').place(relx=0.65, rely=0.8,anchor=CENTER)
Interfaz.mainloop()  # Esto es lo que mantendra la interfaz abierta hasta que se use el boton cerrar