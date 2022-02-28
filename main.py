import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from map_functions import sukurti_zemelapi
import pickle
from haversine import haversine

with open("miestai_ir_koordinates.pkl", "rb") as pkl_in:
    issaugoti_sarasai = pickle.load(pkl_in)
    miestai = issaugoti_sarasai[0]
    koordinates = issaugoti_sarasai[1]

koordinates_pasirinkti = []
kiek_nukeliauta = 0
sukurti_zemelapi(koordinates_pasirinkti)
langas = Tk()
langas.title('Kelionė po Lietuvą')
langas.geometry("+390+60")
langas.geometry("1250x925")

def image_load():
    image_load = Image.open("zemelapis.png")
    image = image_load.crop((50, 0, 1150, 870))
    image_zemelapis = ImageTk.PhotoImage(image)
    foto1 = tkinter.Label(image=image_zemelapis)
    foto1.image = image_zemelapis
    foto1.grid(row=0, column=2, columnspan=4, sticky=N + E)

# Functions
def uzbaigti_kelione():
    if len(koordinates_pasirinkti) < 2:
        status["text"] = "Dar nepradėjot kelionės!"
    else:
        koordinates_pasirinkti.append(koordinates_pasirinkti[0])
        sukurti_zemelapi(koordinates_pasirinkti)
        image_load()
        global kiek_nukeliauta
        kiek_nukeliauta += round(haversine(koordinates_pasirinkti[-1], koordinates_pasirinkti[-2]))
        status["text"] = f'Jau nukeliavot {kiek_nukeliauta}km!'
        messagebox.showinfo('Sveikiname!!!', f'Kelionė užbaigta! Nukeliavot {kiek_nukeliauta}km!')
        langas.destroy()

def itraukti_miesta():
    value = koordinates[box.curselection()[0]]
    if koordinates_pasirinkti != [] and value == koordinates_pasirinkti[-1]:
            status["text"] = "Šiuo metu esate šitame mieste!"
    else:
        if value in koordinates_pasirinkti[1:] and len(koordinates_pasirinkti) > 1:
            status["text"] = "Jau aplankėte šitą miestą!"
        else:
            koordinates_pasirinkti.append(value)
            sukurti_zemelapi(koordinates_pasirinkti)
            image_load()
            if len(koordinates_pasirinkti) > 1:
                global kiek_nukeliauta
                kiek_nukeliauta += round(haversine(koordinates_pasirinkti[-1], koordinates_pasirinkti[-2]))
                status["text"] = f'Jau nukeliavot {kiek_nukeliauta}km!'
                if value == koordinates_pasirinkti[0] and len(koordinates_pasirinkti) > 1:
                        messagebox.showinfo('Sveikiname!!!', f'Kelionė užbaigta! Nukeliavot {kiek_nukeliauta}km!')
                        langas.destroy()

def pradeti_nauja_kelione():
    koordinates_pasirinkti.clear()
    global kiek_nukeliauta
    kiek_nukeliauta = 0
    status["text"] = ""
    sukurti_zemelapi(koordinates_pasirinkti)
    image_load()

def uzdaryti_programa():
    langas.destroy()

# Graphic objects
scrollbar = Scrollbar(langas)
status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)
box = Listbox(langas, yscrollcommand=scrollbar.set)
box.insert(END, *miestai)
scrollbar.config(command=box.yview)
button1 = Button(langas, text="Įtraukti į maršrutą", command=itraukti_miesta)
button2 = Button(langas, text="Užbaigti kelionę", command=uzbaigti_kelione)
button3 = Button(langas, text="Pradėti naują kelionę", command=pradeti_nauja_kelione)
button4 = Button(langas, text="Uždaryti programą", command=uzdaryti_programa)
image_load()

# Packing
scrollbar.grid(row=0, column=0, sticky=N+S)
box.grid(row=0, column=1, sticky=N+S)
button1.grid(row=3, column=2, sticky='we')
button2.grid(row=3, column=3, sticky='we')
button3.grid(row=3, column=4, sticky='we')
button4.grid(row=3, column=5, sticky='we')
status.grid(row=4, columnspan=4, sticky=W+E)
langas.bind("<Escape>", lambda event: uzdaryti_programa())
langas.bind('<Double-Button-1>', lambda event: itraukti_miesta())

langas.mainloop()