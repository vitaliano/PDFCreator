from PIL import Image, ImageDraw, ImageFont
import os

def getTemplate_mm_A4LANDSCAPE():
    #TEMPLATE
    #Calculate perfect equal margins
    PAGE_WIDTH = 297  # A4 landscape width in mm
    COLUMNS = 4
    # 13.5-60-10-60-10-60-10-60-13.5 = 297
    MARGIN_W = 13.5 
    GUTTER_W=10
    WINDOW_WIDTH=60

    PAGE_HEIGHT = 210 # A4 landscape height in mm
    LINES = 4
    # 10-40-10-40-10-40-10-40-10 = 210
    MARGIN_H = 10 
    GUTTER_H=10
    WINDOW_HEIGHT=40
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
    dados = [{'id': 1, 'janela_id': 'janela_1', 'nome_loja': 'Loja 1', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'}, 
            {'id': 2, 'janela_id': 'janela_2', 'nome_loja': 'Loja 2', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 3, 'janela_id': 'janela_3', 'nome_loja': 'Loja 3', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 4, 'janela_id': 'janela_4', 'nome_loja': 'Loja 4', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 5, 'janela_id': 'janela_5', 'nome_loja': 'Loja 5', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 6, 'janela_id': 'janela_6', 'nome_loja': 'Loja 6', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 7, 'janela_id': 'janela_7', 'nome_loja': 'Loja 7', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 8, 'janela_id': 'janela_8', 'nome_loja': 'Loja 8', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 9, 'janela_id': 'janela_9', 'nome_loja': 'Loja 9', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 10, 'janela_id': 'janela_10', 'nome_loja': 'Loja 10', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 11, 'janela_id': 'janela_11', 'nome_loja': 'Loja 11', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 12, 'janela_id': 'janela_12', 'nome_loja': 'Loja 12', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 13, 'janela_id': 'janela_13', 'nome_loja': 'Loja 13', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 14, 'janela_id': 'janela_14', 'nome_loja': 'Loja 14', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 15, 'janela_id': 'janela_15', 'nome_loja': 'Loja 15', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'},
            {'id': 16, 'janela_id': 'janela_16', 'nome_loja': 'Loja 16', 'texto_1': 'Oferta especial', 'texto_2': 'Desconto de até 30%', 'texto_3': 'Válido até 31/10', 'texto_4': 'Consulte condições', 'imagem_path': 'assets/imagens/imagem_padrao.png', 'logo_path': 'assets/logos/logo_padrao.png'}]
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
def draw_window(draw, canvas, item, rect, font_regular, font_bold):
    x, y, w, h = rect['x'], rect['y'], rect['w'], rect['h']
    radius = 20
    draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, outline="black", width=2)

    # Image section
    img_w = int(w * 0.4) - 20
    img_h = int(h * 0.6)
    logo_h = int(h * 0.3)
    logo_w = img_w

    img = Image.open(item["imagem_path"]).resize((img_w, img_h))
    logo = Image.open(item["logo_path"]).resize((logo_w, logo_h))

    canvas.paste(img, (x + 10, y + 10))
    canvas.paste(logo, (x + 10, y + 20 + img_h))

    # Text section
    tx = x + int(w * 0.4) + 20
    ty = y + 10
    draw.text((tx, ty), item["nome_loja"], font=font_bold, fill="black")
    for i in range(1, 4):
        draw.text((tx, ty + 30 + (i - 1) * 30), item[f"texto_{i}"], font=font_regular, fill="black")

    draw.text((x + 10 + logo_w + 10, y + 20 + img_h + logo_h // 2), item["texto_4"], font=font_regular, fill="black")

# === MAIN GENERATOR ===
def generate_flyer(dados, template_px, pattern_path, output_path,DPI,PAGE_WIDTH,PAGE_HEIGHT):
    canvas = create_background(pattern_path,PAGE_WIDTH,PAGE_HEIGHT)
    draw = ImageDraw.Draw(canvas)

    # Load fonts (adjust paths if needed)
    font_regular = ImageFont.truetype("arial.ttf", 24)
    font_bold = ImageFont.truetype("arialbd.ttf", 28)

    for item in dados:
        janela_id = item["janela_id"]
        if janela_id not in template_px:
            continue
        draw_window(draw, canvas, item, template_px[janela_id], font_regular, font_bold)

    canvas.save("canvas.jpg", "JPEG")
    print(f"Flyer saved as JPG: {output_path}")
    canvas.save(output_path, "PDF", resolution=DPI)
    print(f"Flyer saved as PDF: {output_path}")

template_mm=getTemplate_mm_A4LANDSCAPE()
dados=getData()
DPI,PAGE_WIDTH,PAGE_HEIGHT,template_px = convert_template_mm_to_px_A4LANDSCAPE300(template_mm)
generate_flyer(dados, template_px, "assets/patterns/pattern_tile.png", "folheto_final_alt.pdf",DPI,PAGE_WIDTH,PAGE_HEIGHT)
