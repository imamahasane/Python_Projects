import win32com.client

import os,time

for filename in os.listdir("/Users/macbookair/Python/Md_Imam_Ahasan.pdf"):

    if filename.endswith(".pdf"):
        word = win32com.client.Dispatch("word.Application")
        word.Visible = 0

        input_file = os.path.abspath(filename)
        con_word = word.Documents.Open(input_file)
        output_file = os.path.abspath(filename[0 : -4] + "docx".format())
        con_word.SaveAs2(output_file, FileFormat = 16)

        print("Pdf to DOCx is completed")

        con_word.Close()
        word.Quit()
        time.sleep(2)

