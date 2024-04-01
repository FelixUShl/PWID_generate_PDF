from fpdf import FPDF

def create_pdf() -> FPDF:
    return FPDF()

# Подготовка новой страницы к заполнению
def newpage(pdf: FPDF):
    pdf.add_page()
    pdf.image("https://proxway-ble.ru/images/logo.svg", w=50)
    pdf.set_xy(140, 10)
    pdf.set_font("Helvetica", size=16)
    pdf.multi_cell(w=60, text="https://proxway-ble.ru\n8 800 700-19-57\ninfo@proxway-ble.ru")
    pdf.set_font("Helvetica", size=9)

#Отрисовка ячейки с QR кодом и расшифровкой
def draw_cell(pdf: FPDF, x:int, y:int, qr: list):
    pdf.set_xy(x, y)
    pdf.image(qr[0], w=45)
    pdf.multi_cell(w=45, text=f"{qr[1]}\n{qr[2]}\n{qr[3]}")

def generate_table(pdf: FPDF, data: list):
    step_y = 30  # стартовый отступ от верхнего края
    step_x = 10  # стартовый отступ от бокового края
    step = 1  # считаем до 4х - кол-во столбцов
    for elem in data:
        draw_cell(pdf, step_x, step_y, elem)
        if step != 4:
            step_x += 50
            step += 1
        else:
            if (data.index(elem) + 1) % 16 == 0 and (data.index(elem) + 1) != len(data):
                newpage(pdf)
                step_y = 30  # стартовый отступ от верхнего края
                step_x = 10  # стартовый отступ от бокового края

            else:
                step_x = 10
                step_y += 62
            step = 1  # начинаем счет до 4х заново

def print_pdf(pdf: FPDF,name: str = 'QR PWID.pdf'):
    pdf.output(name)