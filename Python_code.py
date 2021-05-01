def generate_tabs(num_tabs, font_type):
    doc = docx.Document()
    for i in range(0, num_tabs):
        for k in range(0, 11):
            para = doc.add_paragraph()
        para_format = para.paragraph_format
        para_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        number = i + 1
        text_to_add = 'TAB ' + str(number)
        para = para.add_run(text_to_add)
        para.font.name = font_type
        para.font.size = Pt(70)
        filename = text_to_add + '.docx'
        doc.save(filename)
        doc = docx.Document()
