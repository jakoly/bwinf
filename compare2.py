from pathlib import Path
from PIL import Image
from collections import Counter

def quantize(pixel, step=16):
    return tuple((c // step) * step for c in pixel)

def auswerten(landf, gesr=0.0, gesg=0.0, gesb=0.0):
    pfad = Path(__file__).parent / "res" / f"{landf}.png"
    img = Image.open(pfad).convert("RGBA")

    pixelcount = img.width*img.height
    pixels = [quantize(p) for p in img.getdata()]
    counter = Counter(pixels)
    leer = counter[quantize((0,0,0,0))]

    for color, count in counter.most_common():
        if color[3]!=0:
            gesr+=count*color[0]
            gesg+=count*color[1]
            gesb+=count*color[2]
        dpr=gesr/(pixelcount-leer)
        dpg=gesg/(pixelcount-leer)
        dpb=gesb/(pixelcount-leer)
    return tuple([round(dpr),round(dpg),round(dpb)])

land1name = input('Was ist dein Land?').strip().lower().capitalize()
land1=auswerten(land1name)
print ('Durchschnittspixel von',land1name,land1[0],land1[1],land1[2])

ordner = Path(__file__).parent / "res"
dges2=int(720)
for datei in ordner.glob("*.png"):
    land2name = datei.stem
    land2=auswerten(land2name)
    if land2name!=land1name:
        dr=abs(land2[0]-land1[0])
        dg=abs(land2[1]-land1[1])
        db=abs(land2[2]-land1[2])
        dges=dr+dg+db
        print(land2name,dges)          
        if dges<dges2:
            dges2=dges
            land2name2=land2name
            land22=land2
print ('Durchschnittspixel von',land2name2,land22[0],land22[1],land22[2])
print(land2name2,'ist',land1name,'am ähnlichsten')
print(dges2)