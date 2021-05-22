with open('documento.txt', encoding='utf-8') as f :

# el (as) es para decirle que cambie toda la expresión por f

    doc = f.read()

    print(doc)

    f.close()
#ahora para agregar contenido al archivo sin abrir el archivo

new = 'certus-clase2\n'
with open('documento.txt', "a" ,encoding='utf-8') as f :
    
    f.write(new)