import os
from pdf_funcs import newpage, create_pdf,print_pdf, generate_table
from pwid_funcs import generate_qr_list

def main():
    path = input("Путь до папки с QR\n")
    pdf = create_pdf()
    newpage(pdf)
    data = os.listdir(path)
    table_data = generate_qr_list(data, path)
    generate_table(pdf, table_data)
    print_pdf(pdf)
    print("PDF готов!")

if __name__ == "__main__":
    main()