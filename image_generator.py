from PIL import Image, ImageDraw, ImageFont

def create_image(days_left, percent_left):

    width = 1200
    height = 675

    img = Image.new("RGB",(width,height),(10,18,40))
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    draw.text((450,80),"CUENTA REGRESIVA",fill="white",font=font)

    draw.text((560,250),str(days_left),fill="white",font=font)

    draw.text((420,330),"días para el cambio de mando",fill="white",font=font)

    # Barra de progreso
    bar_x = 200
    bar_y = 450
    bar_width = 800
    bar_height = 40

    draw.rectangle(
        (bar_x, bar_y, bar_x+bar_width, bar_y+bar_height),
        outline="white",
        width=2
    )

    progress = bar_width * (percent_left/100)

    draw.rectangle(
        (bar_x, bar_y, bar_x+progress, bar_y+bar_height),
        fill=(200,30,30)
    )

    draw.text((520,510),f"{percent_left:.1f}% restante",fill="white",font=font)

    path="contador.png"
    img.save(path)

    return path
