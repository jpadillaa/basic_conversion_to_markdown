# Basic Conversion to Markdown
Basic Conversion of Files from PDF, DOCX, and PPTX to Markdown

## Requisitos

Lista de los requisitos previos para ejecutar el proyecto, como versiones específicas de software o dependencias. 
- [Pandoc](https://pandoc.org/installing.html  "Ir al sitio web de Pandoc")

## Instalación

Instrucciones para instalar el proyecto. Si tienes un archivo `requirements.txt`, incluye las instrucciones para instalar las dependencias.

```bash
pip install -r requirements.txt
```

## Convertir a Markdown
### Documento de Word 

```bash
python main documento_de_entrada.docx documento_de_salida.md
```
### Documento de Powerpoint

```bash
python main presentacion_de_entrada.pptx documento_de_salida.md
```
### Documento en formato PDF

```bash
python main un_pdf_de_entrada.docx documento_de_salida.md
```
