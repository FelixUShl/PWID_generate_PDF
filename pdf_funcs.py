from fpdf import FPDF

def create_pdf() -> FPDF:
    return FPDF()

# Подготовка новой страницы к заполнению
def newpage(pdf: FPDF):
    pdf.add_page()
    pdf.image("proxway_logo.png", w=50)
    pdf.set_xy(140, 10)
    pdf.set_font("Helvetica", size=16)
    pdf.multi_cell(w=60, text="https://proxway-ble.ru\n\ninfo@proxway-ble.ru")
    pdf.set_font("Helvetica", size=9)

#Отрисовка ячейки с QR кодом и расшифровкой
def draw_cell(pdf: FPDF, x:int, y:int, qr: list):
    pdf.set_xy(x, y)
    pdf.image(qr[0], w=45)
    pdf.multi_cell(w=45, text=f"{qr[1]}\n{qr[2]}\n{qr[3]}")

def print_pdf(pdf: FPDF,name: str = 'QR PWID.pdf'):
    pdf.output(name)