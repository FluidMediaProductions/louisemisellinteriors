import os
import time
import base64
import io
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from PIL import Image, ImageDraw, ImageFilter
from .models import Wallpaper


def index(request):
    wallpapers = Wallpaper.objects.all()
    print(wallpapers)
    return render(request, 'wallpaper/index.html', {
        "wallpapers": wallpapers
    })


def visualize(request, id):
    wallpaper = get_object_or_404(Wallpaper, id=id)
    if request.method == "GET":
        return render(request, 'wallpaper/visualize.html', {
            "wallpaper": wallpaper
        })
    elif request.method == "POST":
        wall_width = int(request.POST['wall_width'])
        wall_height = int(request.POST['wall_height'])
        paper = Image.open(wallpaper.image.path)
        wall = Image.new('RGB', (wall_width * 10, wall_height * 10))
        num_width = int(wall_width / wallpaper.width)
        num_height = int(wall_height / wallpaper.height)
        paper_width = int((wall_width * 10) / num_width)
        paper_height = int((wall_height * 10) / num_height)
        paper_resized = paper.resize((paper_width, paper_height))
        for x in range(0, num_width + 1):
            for y in range(0, num_height + 1):
                wall.paste(paper_resized, (x * paper_width, y * paper_height))
        wall_blur = Image.new('RGBA', wall.size)
        wall_blur_draw = ImageDraw.Draw(wall_blur)
        wall_blur_draw.rectangle((0, 0, 30, wall_blur.size[1]), (0, 0, 0, 128))
        wall_blur_draw.rectangle((0, 0, wall_blur.size[0], 30), (0, 0, 0, 128))
        wall_blur_draw.rectangle((0, wall_blur.size[0] - 30, wall_blur.size[0], wall_blur.size[1]), (0, 0, 0, 128))
        wall_blur_draw.rectangle((wall_blur.size[0] - 30, 0, wall_blur.size[0], wall_blur.size[1]), (0, 0, 0, 128))
        wall_blur_blured = wall_blur.filter(ImageFilter.GaussianBlur(50))
        wall.paste(wall_blur_blured, (0, 0), wall_blur_blured)
        file_name = '{}-{}.jpg'.format(wallpaper.id, int(time.time()))
        full_path = os.path.join(settings.MEDIA_ROOT, file_name)
        wall.save(full_path)
        output = io.StringIO()
        wall.save(output, format='JPG')
        output.seek(0)
        output_s = output.read()
        b64 = base64.b64encode(output_s)
        img = 'data:image/png;base64,{0}'.format(b64)
        return render(request, 'wallpaper/visualized.html', {
            "wallpaper": wallpaper,
            "image": img
        })
