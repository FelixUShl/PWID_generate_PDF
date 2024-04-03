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
    pdf.set_font("Helvetica", size=6.5)

#Отрисовка ячейки с QR кодом и расшифровкой
def draw_cell(pdf: FPDF, x:int, y:int, qr: list):
    pdf.set_xy(x, y)
    pdf.image(qr[0], w=30)
    pdf.multi_cell(w=31, text=f"{qr[1]}\n{qr[2]}\n{qr[3]}")

def generate_table(pdf: FPDF, data: list):
    step_y = 30  # стартовый отступ от верхнего края
    step_x = 20  # стартовый отступ от бокового края
    step = 1  # считаем до 4х - кол-во столбцов
    for elem in data:
        draw_cell(pdf, step_x, step_y, elem)
        if step != 5:
            step_x += 37
            step += 1
        else:
            if (data.index(elem) + 1) % 30 == 0 and (data.index(elem) + 1) != len(data):
                newpage(pdf)
                step_y = 30  # стартовый отступ от верхнего края
                step_x = 20  # стартовый отступ от бокового края

            else:
                step_x = 20
                step_y += 42
            step = 1  # начинаем счет до 4х заново

def print_pdf(pdf: FPDF,name: str = 'QR PWID.pdf'):
    pdf.output(name)