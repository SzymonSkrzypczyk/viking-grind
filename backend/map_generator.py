from PIL import Image, ImageDraw, ImageFont
import io
import time

me = [
    "1. Przygotuj się fizycznie i mentalnie.",
    "2. Pozyskaj odpowiednie pozwolenia i zezwolenia w Nepalu.",
    "3. Zorganizuj ekspedycję z doświadczonymi przewodnikami i porterami.",
    "4. Rozpocznij trekking do bazy pod Everestem.",
    "5. Przejdź przez szereg aklimatyzacji w bazie pod Everestem.",
    "6. Dokonaj ostatecznego podejścia do szczytu, uwzględniając odpowiednie warunki pogodowe.",
    "7. Wróć bezpiecznie do bazy i kontynuuj zejście."
]

fills = [
    (255,255,255),
    (0,255,0),
    (0,0,255),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255)
]

class MapGenerator:

    def __init__(self, json_data: str, image_path: str, steps: int) -> None:
        self.json_data = json_data
        self.image = Image.open(image_path)
        self.pixmap = ImageDraw.Draw(self.image, "RGBA")
        self.steps = steps
    
    def generate_map(self) -> io.BytesIO:
        #self.image.show()
        
        #coords, font = self.calculate_coords(longest_word)
        self.draw_rectangles()
        #for idx, coord in enumerate(coords):
        #   I1 = ImageDraw.Draw(self.image)
        #    I1.text(coord, me[idx], fill=(255, 255, 255), font=font)

        self.draw_steps(me)
        self.image.show()


    def draw_rectangles(self) -> None:
        rect1, rect2 = self.calc_rects()
        self.pixmap.rectangle(rect1, fill=(148, 77, 25,170))
        self.pixmap.rectangle(rect2, fill=(148, 77, 25,170))
        

    def draw_steps(self, steps: list, margin: float = 0.02) -> None:
        rect1, rect2 = self.calc_rects()
        clusters = (len(steps)+1)//2
        init_font = ImageFont.truetype("arial.ttf", 20)
        increment = (self.image.height - 2*margin*self.image.height) / clusters
        print("H", self.image.height, "I", increment, "C", clusters)
        
        x = 0
        for i in range(len(steps)):
            if (i+1) % 2:
                box = (rect1[0][0], rect1[0][1]+x*increment)
            else:
                box = (rect2[0][0], rect2[0][1]+(x)*increment)
                x += 1
            text = self.split_text(steps[i], init_font)
            print(box)
            
            self.pixmap.multiline_text(box, text, "#fff", font=init_font)


    def calc_rects(self, ratio: float = 0.4, margin: float = 0.02) -> tuple:
        width, height = self.image.size
        rect1 = [(margin*width, margin*width), (width*ratio, height-margin*width)]
        rect2 = [((1-ratio)*width, margin*width), (width*(1-margin), height-margin*width)]
        return (rect1, rect2)
    

    def split_text(self, text: str, font: ImageFont.ImageFont) -> str:
        print(font.getlength(text), 0.4*self.image.width)
        tt = text.split(" ")
        merged = text
        left = " ".join(tt[:(len(tt))])
        i = 0
        while font.getlength(left) > 0.35*self.image.width:
            left = tt[:(len(tt)-i)]
            merged = " ".join(left + ["\n"] + tt[(len(tt)-i):])
            left = " ".join(left)
            i += 1
        return merged

    


mg = MapGenerator("json_data", r"backend\temp\viking.jpg", 10)
mg.generate_map()



    