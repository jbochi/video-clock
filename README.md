
  $ python create_images.py
  $ ffmpeg -r 1/1 -i frames/frame%05d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p clock.mp4
