from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("helvetica", style="B", size=27)
    pdf.cell(0, 10, "CS50 Shirtificate", new_y="NEXT", align="C")
    
    # Imagen
    pdf.image("/Users/eugeniosoria/Documents/001 PROGRAMACION WEB/01- HARVARD CS50/python_cs50/8_POO/shirtificate/shirtificate.png", x=10, y=50, w=190)  # Ajusta la posición y el tamaño según necesites
    
    # Texto sobre la imagen
    pdf.set_y(140)  # Posiciona el texto verticalmente
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)  # Blanco
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    
    # Guardar PDF
    pdf.output("shirtificatePT.pdf")
    
if __name__ == "__main__":
    main()
