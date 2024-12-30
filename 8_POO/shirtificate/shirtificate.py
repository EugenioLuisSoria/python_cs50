from fpdf import FPDF, Align



def main():
    #name = input("Name: ")
    name = "Euge"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=27)
    pdf.cell(0,14, "CS50 Shirtificate", new_y="NEXT", align='C', center=True)
    pdf.image("/Users/eugeniosoria/Documents/001 PROGRAMACION WEB/01- HARVARD CS50/python_cs50/8_POO/shirtificate/shirtificate.png", Align.C, 25, 200, keep_aspect_ratio=True)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,145, f"{name} took CS50", new_y="NEXT", align='C', center=True)
    return pdf.output("/Users/eugeniosoria/Documents/001 PROGRAMACION WEB/01- HARVARD CS50/python_cs50/8_POO/shirtificate/shirtificate.pdf")




if __name__ == "__main__":
    main()
