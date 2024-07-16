from conversion_to_markdown import *
        
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Descripción de tu script")
    parser.add_argument('archivo', type=str, help='El archivo PDF a convertir')
    parser.add_argument('archivo_md', type=str, help='El archivo Markdown de salida')

    args = parser.parse_args()
    
    _, extension = os.path.splitext(args.archivo)
    
    match extension:
        case '.pptx':
            powerpoint_to_markdown(args.archivo, args.archivo_md)
        case '.docx':
            word_to_markdown(args.archivo, args.archivo_md)
        case '.pdf':
            pdf_to_markdown(args.archivo, args.archivo_md)        
        case _:
            print("Extensión de archivo desconocida")

    
    
