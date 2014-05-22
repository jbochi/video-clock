from PIL import Image, ImageDraw, ImageFont

fontsize = 180
font = ImageFont.truetype("Ubuntu-M.ttf", fontsize)

for i in range(3600):
    image = Image.new("RGBA", (480,270), (255,255,255))
    draw = ImageDraw.Draw(image)
    hour = i / 60
    minute = i % 60
    text = "%02d:%02d" % (hour, minute)
    frame = "frames/frame%05d.jpg" % i
    print text, frame
    draw.text((10, 20), text, (0,0,0), font=font)
    image.save(frame)
