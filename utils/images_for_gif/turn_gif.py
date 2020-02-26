import imageio
import os  

def read_png():
    path = os.path.join(__file__, "..")
    png_list = os.listdir(path)
    png_list.remove('turn_gif.py')
    # print(png_list)
    png_list.sort(key=lambda x: int(x[:1] if x[1]=='.' else int(x[:2])))
    # print(png_list)
    return png_list
  
def create_gif(image_list, gif_name, duration=0.3):
    frames = []
    for image_name in image_list:
        image_path = os.path.join(__file__, "..", image_name)
        frames.append(imageio.imread(image_path))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    #这里放上自己所需要合成的图片
    image_list = read_png()
    gif_name = 'exp_4.gif'
    gif_path = os.path.join(__file__, "..", gif_name)
    create_gif(image_list, gif_path)

if __name__ == '__main__':
    main()
    # read_png()