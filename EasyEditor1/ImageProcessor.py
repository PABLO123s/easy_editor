from PIL import Image, ImageFilter


class ImageProcessor:
    def __init__(self, workdir):
        self.current_image = None
        self.filename: str = None
        self.modified_folder = "modified"
        self.workdir = workdir

        def open(self, fn):
            self.filename = fn 
            path = os.path.join(self.workdir, self.filename)
            self.current_image = Image.open(path)


        def show(self, fn):
            ...