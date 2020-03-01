import imageio
import os  

def read_png_4():
    path = os.path.join(__file__, "..")
    file_list = os.listdir(path)
    png_list = file_list.copy()
    for png in file_list:
        if len(png) > 6 or png[-4:]!='.png' or png[0]=='x':
            # print(png)
            png_list.remove(png)
        # gif is bigger than 5 MB
        # so let go some images
        elif int(png[0:-4]) % 2 == 0:
            png_list.remove(png)
    png_list.sort(key=lambda x: int(x[:1] if x[1]=='.' else int(x[:2])))
    # print(png_list)
    return png_list

def read_png_1():
    path = os.path.join(__file__, "..")
    file_list = os.listdir(path)
    png_list = file_list.copy()
    for png in file_list:
        if len(png) <= 6 or png[-4:]!='.png':
            # print(png)
            png_list.remove(png)
    png_list.sort(key=lambda x: int(x[:1] if x[1]=='_' else int(x[:2])))
    print(png_list)
    return png_list

  
def create_gif(image_list, gif_name, duration=0.3):
    frames = []
    for image_name in image_list:
        image_path = os.path.join(__file__, "..", image_name)
        frames.append(imageio.imread(image_path))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main_4():
    image_list = read_png_4()
    gif_name = 'exp_4.gif'
    gif_path = os.path.join(__file__, "..", gif_name)
    create_gif(image_list, gif_path)

def main_1():
    image_list = read_png_1()
    gif_name = 'exp_1.gif'
    gif_path = os.path.join(__file__, "..", gif_name)
    create_gif(image_list, gif_path)

def main_x():
    path = os.path.join(__file__, "..")
    file_list = os.listdir(path)
    png_list = file_list.copy()
    for png in file_list:
        if png[0]!='x':
            png_list.remove(png)
        else:
            # print(png[1:-4])
            pass
    png_list.sort(key=lambda x: int(x[1:-4]))
    print(png_list)
    gif_name = 'exp_4x.gif'
    gif_path = os.path.join(__file__, "..", gif_name)
    create_gif(png_list, gif_path)

if __name__ == '__main__':
    main_4()
    # main_1()
    # read_png()
    # main_x()