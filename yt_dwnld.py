import youtube_dl

opts = {}
def dwl():
        with youtube_dl.YoutubeDL(opts) as ydl:
                ydl.download([txt])
                ch = 1
                while (ch == int(1)):
                        url = input("Enter URL:")
                        txt = url.strip()
                        dwl()
                        ch=int(input("To Download more Videos Enter 1 else pres$



