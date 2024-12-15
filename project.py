from tkinter import*
from yt_dlp import YoutubeDL

def HightQuality():
    try:
        url= entry.get()

        ydl_opts={
            'fromat': 'best',
            'outtmpl':'donwloads%(titles)s.%(ext)s'

        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("the vedio has been dowloaded")




    except Exception as e:
        print("Error donloading")     

def LowtQuality():
    try:
        url= entry.get()

        ydl_opts={
            'fromat': 'best',
            'outtmpl':'donwloads%(titles)s.%(ext)s'

        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("the vedio has been dowloaded")




    except Exception as e:
        print("Error donloading") 


def GetAudio():
    try:
        url= entry.get()

        ydl_opts={
            'fromat': 'bestaudio',
            'outtmpl':'donwloads%(titles)s.%(ext)s'

        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("the vedio has been dowloaded")




    except Exception as e:
        print("Error donloading") 









window=Tk()
window.title("Mohamed ElHussein")
window.geometry("600x400")
window.configure(bg="#EEDFCC")


label=Label(window,text="Add Yor Youtube Link Here",font="bold",bg=window['bg'])
label.place(x=200,y=30)

entry=Entry(window , width=50)
entry.place(x=150,y=100)

hight=Button(window,text="Hight Quality",command=HightQuality ,font="bold",activeforeground="green")
hight.place(x=100,y=200)

low=Button(window,text="low Quality",command=LowtQuality,font="bold",activeforeground="red")
low.place(x=250,y=200)


audio=Button(window,text="Get Audio ",command=GetAudio,font="bold",activeforeground="blue")
audio.place(x=350,y=200)




window.mainloop()