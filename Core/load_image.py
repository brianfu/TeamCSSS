_image_library = {}

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    
    global _image_library
    image = _image_library.get(fullname)
    
    if image == None:
        try:
            image = pygame.image.load(fullname)
        except:
            print('Cannot load image:',name)
            raise SystemExit
        image = image.convert()
        _image_library[path] = image
        
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    
    return image, image.get_rect()
