from psd_tools import PSDImage
import os


if __name__ == '__main__':

  parent_dir = './Assets/'
  path = ''
  file_path = 'PeaBots_skin3.psd'

  psd = PSDImage.open(file_path)
  # psd.compose().save('example.png')
  f = open("rarity3.txt", "w")

  for layer in list(psd.descendants()):
  
    if not layer.is_group():
      pil_img = layer.topil(apply_icc=True)
      file_path = os.path.join(path, layer.name + ".png")
      pil_img.save(file_path)
      f.write("(%s) %d %d\n" % (file_path, layer.left, layer.top))
    else:
      path_dirs = layer.name.split('/')
      if len(path_dirs) == 2:
        path1 = os.path.join(parent_dir, path_dirs[0])
        os.mkdir(path1)
        path = os.path.join(path1, path_dirs[1])
        os.mkdir(path)
      else:
        path = os.path.join(parent_dir, path_dirs[0])
        os.mkdir(path)
      #print(path)
      
