import os, pathlib
import subprocess
import pymupdf4llm

def word_to_markdown(doc_file, output_file):
    try:
        # Comando para convertir de Docx a Markdown usando Pandoc
        command = ['pandoc', doc_file, '-f', 'docx', '-t', 'markdown', '-o', output_file]
        
        # Ejecutar el comando
        result = subprocess.run(command, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        
        # Verificar si la conversión fue exitosa
        if result.returncode == 0:
            print(f"Conversión exitosa: {output_file}")
        else:
            print(f"Error en la conversión: {result.stderr.decode('utf-8')}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error durante la ejecución de Pandoc: {e.output.decode('utf-8')}")
        
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        
def powerpoint_to_markdown(ppt_file, output_file):
    try:
        # Comando para convertir de PPTx a Markdown usando PPTx2MD
        command = ['pptx2md', ppt_file, '-o', output_file]
        
        # Ejecutar el comando
        result = subprocess.run(command, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        
        # Verificar si la conversión fue exitosa
        if result.returncode == 0:
            print(f"Conversión exitosa: {output_file}")
        else:
            print(f"Error en la conversión: {result.stderr.decode('utf-8')}")
        
    except Exception as e:
        print(f"Error inesperado: {str(e)}")        
        
def pdf_to_markdown(pdf_file, output_file):
    output = pymupdf4llm.to_markdown(pdf_file, write_images = False)
    pathlib.Path(output_file).write_bytes(output.encode())        