from PIL import Image, ImageDraw, ImageFont
import os

def getTemplate_mm_A4LANDSCAPE():
    #TEMPLATE
    #Calculate perfect equal margins
    PAGE_WIDTH = 297  # A4 landscape width in mm
    COLUMNS = 4
    # 2.5-70-4-70-4-70-4-70-2.5 = 297
    MARGIN_W = 2.5
    GUTTER_W=4
    WINDOW_WIDTH=70

    PAGE_HEIGHT = 210 # A4 landscape height in mm
    LINES = 4
    # 5.5-46-5-46-5-46-5-46-5.5 = 210
    MARGIN_H = 5
    GUTTER_H=4
    WINDOW_HEIGHT=47
    row1_y= MARGIN_H
    row2_y= MARGIN_H + WINDOW_HEIGHT + GUTTER_H
    row3_y= MARGIN_H + WINDOW_HEIGHT + GUTTER_H + WINDOW_HEIGHT + GUTTER_H
    row4_y= MARGIN_H + WINDOW_HEIGHT + GUTTER_H + WINDOW_HEIGHT + GUTTER_H + WINDOW_HEIGHT + GUTTER_H


    col1_x= MARGIN_W
    col2_x= MARGIN_W + WINDOW_WIDTH + GUTTER_W
    col3_x= MARGIN_W + WINDOW_WIDTH + GUTTER_W + WINDOW_WIDTH + GUTTER_W
    col4_x= MARGIN_W + WINDOW_WIDTH + GUTTER_W + WINDOW_WIDTH + GUTTER_W + WINDOW_WIDTH + GUTTER_W



    # Calculate total content width and equal margins
    # Template for 4x4 grid in landscape A4 with perfectly equal margins in mm
    template_mm = {
        # Row 1
        'janela_1': {'x': col1_x, 'y': row1_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_2': {'x': col2_x, 'y': row1_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_3': {'x': col3_x ,'y': row1_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_4': {'x': col4_x, 'y': row1_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        
        # Row 2
        'janela_5': {'x': col1_x, 'y': row2_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_6': {'x': col2_x, 'y': row2_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_7': {'x': col3_x ,'y': row2_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_8': {'x': col4_x, 'y': row2_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        
        # Row 3
        'janela_9': {'x': col1_x, 'y': row3_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_10': {'x': col2_x, 'y': row3_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_11': {'x': col3_x ,'y': row3_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_12': {'x': col4_x, 'y': row3_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        
        # Row 4
        'janela_13': {'x': col1_x, 'y': row4_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_14': {'x': col2_x, 'y': row4_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_15': {'x': col3_x ,'y': row4_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
        'janela_16': {'x': col4_x, 'y': row4_y, 'w': WINDOW_WIDTH, 'h': WINDOW_HEIGHT},
    }
    return template_mm

def getData():
    #DATA
    dados = [
            {'id': 1, 'janela_id': 'janela_1', 'titulo': 'Vestido em Seda Pura', 'subtitulo': 'Oportunidade', 'descricao': 'Vestido vinho de festa, em seda pura importada de finíssima qualidade', 'valor': 'De R$989,00 por R$788,00', 'nome_loja': 'Veste Sinhá', 'endereco': 'Al ghyu 334 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img1.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 2, 'janela_id': 'janela_2', 'titulo': 'Conjunto de Blazer e Calça', 'subtitulo': 'Oferta impertível da marca X&X', 'descricao': 'Conjunto esporte para ocasiões especiais com corte moderno para uso casual chic', 'valor': 'De R$1800,00 por R$1290,00', 'nome_loja': 'SXER', 'endereco': 'Al Macucos 135 Sao Paulo SP 456 Bairro dos Pratos', 'imagem_path': 'assets/imagens/img2.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 3, 'janela_id': 'janela_3', 'titulo': 'Terno Esportivo Azul', 'subtitulo': 'Grande Promoção 30% de desconto', 'descricao': 'Terno completo com colete corte inglês em gabardine', 'valor': 'De R$3300,00 por R$2199,00', 'nome_loja': 'Dr. Terno', 'endereco': 'Al Gretyuter 3455 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img3.png', 'logo_path': 'assets/logos/logo1.png'},
            {'id': 4, 'janela_id': 'janela_4', 'titulo': 'Carteira Pelica', 'subtitulo': 'Oferta especial desconto de 50%', 'descricao': 'Carteira de festa em pelica rosa para seu sucesso criata pelo estilista JJFred. Diponível nas cores rosa, edverde , azul e creme', 'valor': 'De R$2300,00 por R$1199,00', 'nome_loja': 'Sereníssima', 'endereco': 'Al Macucos 135 Sao Paulo SP CEP 04654-000', 'imagem_path': 'assets/imagens/img4.png', 'logo_path': 'assets/logos/logo1.png'}, 
           

            {'id': 5, 'janela_id': 'janela_5', 'titulo': 'Carteira Pelica', 'subtitulo': 'Oferta especial desconto de 50%', 'descricao': 'Carteira de festa em pelica rosa para seu sucesso criata pelo estilista JJFred. Diponível nas cores rosa, edverde , azul e creme', 'valor': 'De R$2300,00 por R$1199,00', 'nome_loja': 'Sereníssima', 'endereco': 'Al Macucos 135 Sao Paulo SP CEP 04654-000', 'imagem_path': 'assets/imagens/img4.png', 'logo_path': 'assets/logos/logo1.png'}, 
            {'id': 6, 'janela_id': 'janela_6', 'titulo': 'Conjunto de Blazer e Calça', 'subtitulo': 'Oferta impertível da marca X&X', 'descricao': 'Conjunto esporte para ocasiões especiais com corte moderno para uso casual chic', 'valor': 'De R$1800,00 por R$1290,00', 'nome_loja': 'SXER', 'endereco': 'Al Macucos 135 Sao Paulo SP 456 Bairro dos Pratos', 'imagem_path': 'assets/imagens/img2.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 7, 'janela_id': 'janela_7', 'titulo': 'Terno Esportivo Azul', 'subtitulo': 'Grande Promoção 30% de desconto', 'descricao': 'Terno completo com colete corte inglês em gabardine', 'valor': 'De R$3300,00 por R$2199,00', 'nome_loja': 'Dr. Terno', 'endereco': 'Al Gretyuter 3455 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img3.png', 'logo_path': 'assets/logos/logo1.png'},
            {'id': 8, 'janela_id': 'janela_8', 'titulo': 'Vestido em Seda Pura', 'subtitulo': 'Oportunidade', 'descricao': 'Vestido vinho de festa, em seda pura importada de finíssima qualidade', 'valor': 'De R$989,00 por R$788,00', 'nome_loja': 'Veste Sinhá', 'endereco': 'Al ghyu 334 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img1.png', 'logo_path': 'assets/logos/logo_padrao.png'},

            {'id': 9, 'janela_id': 'janela_9', 'titulo': 'Carteira Pelica', 'subtitulo': 'Oferta especial desconto de 50%', 'descricao': 'Carteira de festa em pelica rosa para seu sucesso criata pelo estilista JJFred. Diponível nas cores rosa, edverde , azul e creme', 'valor': 'De R$2300,00 por R$1199,00', 'nome_loja': 'Sereníssima', 'endereco': 'Al Macucos 135 Sao Paulo SP CEP 04654-000', 'imagem_path': 'assets/imagens/img4.png', 'logo_path': 'assets/logos/logo1.png'}, 
            {'id': 10, 'janela_id': 'janela_10', 'titulo': 'Conjunto de Blazer e Calça', 'subtitulo': 'Oferta impertível da marca X&X', 'descricao': 'Conjunto esporte para ocasiões especiais com corte moderno para uso casual chic', 'valor': 'De R$1800,00 por R$1290,00', 'nome_loja': 'SXER', 'endereco': 'Al Macucos 135 Sao Paulo SP 456 Bairro dos Pratos', 'imagem_path': 'assets/imagens/img2.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 11, 'janela_id': 'janela_11', 'titulo': 'Terno Esportivo Azul', 'subtitulo': 'Grande Promoção 30% de desconto', 'descricao': 'Terno completo com colete corte inglês em gabardine', 'valor': 'De R$3300,00 por R$2199,00', 'nome_loja': 'Dr. Terno', 'endereco': 'Al Gretyuter 3455 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img3.png', 'logo_path': 'assets/logos/logo1.png'},
            {'id': 12, 'janela_id': 'janela_12', 'titulo': 'Vestido em Seda Pura', 'subtitulo': 'Oportunidade', 'descricao': 'Vestido vinho de festa, em seda pura importada de finíssima qualidade', 'valor': 'De R$989,00 por R$788,00', 'nome_loja': 'Veste Sinhá', 'endereco': 'Al ghyu 334 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img1.png', 'logo_path': 'assets/logos/logo_padrao.png'},

            {'id': 13, 'janela_id': 'janela_13', 'titulo': 'Carteira Pelica', 'subtitulo': 'Oferta especial desconto de 50%', 'descricao': 'Carteira de festa em pelica rosa para seu sucesso criata pelo estilista JJFred. Diponível nas cores rosa, edverde , azul e creme', 'valor': 'De R$2300,00 por R$1199,00', 'nome_loja': 'Sereníssima', 'endereco': 'Al Macucos 135 Sao Paulo SP CEP 04654-000', 'imagem_path': 'assets/imagens/img4.png', 'logo_path': 'assets/logos/logo1.png'}, 
            {'id': 14, 'janela_id': 'janela_14', 'titulo': 'Conjunto de Blazer e Calça', 'subtitulo': 'Oferta impertível da marca X&X', 'descricao': 'Conjunto esporte para ocasiões especiais com corte moderno para uso casual chic', 'valor': 'De R$1800,00 por R$1290,00', 'nome_loja': 'SXER', 'endereco': 'Al Macucos 135 Sao Paulo SP 456 Bairro dos Pratos', 'imagem_path': 'assets/imagens/img2.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 15, 'janela_id': 'janela_15', 'titulo': 'Terno Esportivo Azul', 'subtitulo': 'Grande Promoção 30% de desconto', 'descricao': 'Terno completo com colete corte inglês em gabardine', 'valor': 'De R$3300,00 por R$2199,00', 'nome_loja': 'Dr. Terno', 'endereco': 'Al Gretyuter 3455 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img3.png', 'logo_path': 'assets/logos/logo1.png'},
            {'id': 16, 'janela_id': 'janela_16', 'titulo': 'Vestido em Seda Pura', 'subtitulo': 'Oportunidade', 'descricao': 'Vestido vinho de festa, em seda pura importada de finíssima qualidade', 'valor': 'De R$989,00 por R$788,00', 'nome_loja': 'Veste Sinhá', 'endereco': 'Al ghyu 334 Sao Paulo SP ', 'imagem_path': 'assets/imagens/img1.png', 'logo_path': 'assets/logos/logo_padrao.png'}]
    return dados

def convert_template_mm_to_px_A4LANDSCAPE300(template_mm):
    
    # === CONFIG ===
    DPI = 300
    MM_TO_PX = DPI / 25.4
    PAGE_WIDTH_MM = 297
    PAGE_HEIGHT_MM = 210
    PAGE_WIDTH = int(PAGE_WIDTH_MM * MM_TO_PX)
    PAGE_HEIGHT = int(PAGE_HEIGHT_MM * MM_TO_PX)

    def mm_to_px(mm):
        return int(mm * MM_TO_PX)
    
    template_px= {
        key: {
            'x': mm_to_px(val['x']),
            'y': mm_to_px(val['y']),
            'w': mm_to_px(val['w']),
            'h': mm_to_px(val['h']),
        }
        for key, val in template_mm.items()
    }
    return DPI,PAGE_WIDTH,PAGE_HEIGHT,template_px

# === BACKGROUND ===
def create_background(pattern_path,PAGE_WIDTH,PAGE_HEIGHT):
    pattern = Image.open(pattern_path).convert("RGB")
    bg = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), (255, 255, 255))
    for x in range(0, PAGE_WIDTH, pattern.width):
        for y in range(0, PAGE_HEIGHT, pattern.height):
            bg.paste(pattern, (x, y))
    return bg

# === DRAW WINDOW ===
def draw_window(draw, canvas, item, rect ):
    
    def wrap_text(text, max_font, max_width, max_height):
        # wraps text to a number of lines that fit within max_width and max_height
        def get_lines(text, font, max_width):
            #wraps text to a number of lines that fit within max_width
            image = Image.new("RGB", (600, 400), "white")
            draw = ImageDraw.Draw(image)
            lines = []
            words = text.split()
            line = ""
            for word in words:
                test_line = f"{line} {word}".strip()
                width = draw.textlength(test_line, font=font)
                if width <= max_width:
                    line = test_line
                else:
                    lines.append(line)
                    line = word
            lines.append(line)
            return lines
        font = max_font
        lines= get_lines(text, font, max_width)
        nlines=len(lines)

        bbox = font.getbbox(lines[0])
        heightFont = bbox[3] - bbox[1]
        height= (heightFont + 5)*nlines
        while height > max_height:
            font_size=font.size-2
            if font_size < 24:
                nlines=nlines-1
            else:
                font=ImageFont.truetype("arialbd.ttf", font_size)
                lines= get_lines(text, font, max_width)
                nlines=len(lines)

            bbox = font.getbbox(lines[0])
            heightFont = bbox[3] - bbox[1]
            height= (heightFont + 5)*nlines   
            
        return lines,font

    font_regular = ImageFont.truetype("arialbd.ttf", 36)
    font_bold = ImageFont.truetype("arialbd.ttf", 48)
    x, y, w, h = rect['x'], rect['y'], rect['w'], rect['h']
    radius = 20
    draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, outline="black", width=2)

    # Image section
    img_w = int(w * 0.50) - 20
    img_h = img_w
    logo_h = int(h * 0.24)
    logo_w = logo_h

    img = Image.open(item["imagem_path"]).resize((img_w, img_h))
    logo = Image.open(item["logo_path"]).resize((logo_w, logo_h))

    canvas.paste(img, (x + 10, y + 10))
    canvas.paste(logo, (x + 10, y + 20 + img_h))

    # Text section
    # titulo
    ty = y + 10
    tx = x + img_w + 20
    max_font=font_bold
    text=item["titulo"]
    max_width= w - img_w - 10
    max_height= int((img_h-10)*0.4)
    lines,font= wrap_text(text, max_font, max_width, max_height)
    for line in lines:
        draw.text((tx, ty), line, font=font, fill="black")
        bbox = font.getbbox(line)
        heightFont = bbox[3] - bbox[1]
        ty += heightFont + 5 
    
    #subtitulo, descricao,valor
    ty=ty+10 # y end of title section
    text_itens=["subtitulo", "descricao", "valor"]
    max_font=font_regular
    max_height= int((img_h-10)*0.2)-10
    for text_item in text_itens:
        text=item[text_item]  
        lines,font= wrap_text(text, max_font, max_width, max_height)
        for line in lines:
            draw.text((tx, ty), line, font=font, fill="black")
            bbox = font.getbbox(line)
            heightFont = bbox[3] - bbox[1]
            ty += heightFont + 5 
        ty +=10
        
    # nome_loja, endereco
    ty=y+20+img_h
    tx=x+logo_w+20
    text_itens=["nome_loja", "endereco"]
    max_font=font_regular
    max_height= int((logo_h-10)/2.0)
    max_width=w-logo_w-20
    for text_item in text_itens:
        text=item[text_item]  
        lines,font= wrap_text(text, max_font, max_width, max_height)
        for line in lines:
            draw.text((tx, ty), line, font=font, fill="black")
            bbox = font.getbbox(line)
            heightFont = bbox[3] - bbox[1]
            ty += heightFont + 5 
 

# === MAIN GENERATOR ===
def generate_flyer(dados, template_px, pattern_path, output_path,DPI,PAGE_WIDTH,PAGE_HEIGHT):
    canvas = create_background(pattern_path,PAGE_WIDTH,PAGE_HEIGHT)
    draw = ImageDraw.Draw(canvas)
    # Load fonts (adjust paths if needed)
    for item in dados:
        janela_id = item["janela_id"]
        if janela_id not in template_px:
            continue
        draw_window(draw, canvas, item, template_px[janela_id])
    return canvas

template_mm=getTemplate_mm_A4LANDSCAPE()
dados=getData()
DPI,PAGE_WIDTH,PAGE_HEIGHT,template_px = convert_template_mm_to_px_A4LANDSCAPE300(template_mm)
canvas=generate_flyer(dados, template_px, "assets/patterns/pattern_tile.png", "folheto_final_alt.pdf",DPI,PAGE_WIDTH,PAGE_HEIGHT)
canvas.save("folheto.jpg", "JPEG")
print(f"Flyer saved as JPG: folheto.jpg")
#canvas.save('folheto.pdf', "PDF", resolution=DPI)
#print(f"Flyer saved as PDF: folheto.pdf")
