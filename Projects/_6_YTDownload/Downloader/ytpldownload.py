try:
    from pytube import YouTube
    from pytube import Playlist
    import os
    import msvcrt
    import pathlib

except Exception as e:
    print("Modules missing: {}".format(e))

STITLE = """
  __   _______   ____                      _                 _           
  \ \ / /_   _| |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \ V /  | |   | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |   | |   | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|   |_|   |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   

                        © Copyright 2020 Michael Huber 
"""
overlay = """

        '1' - Download all Videos of a YT Playlist as Audio
        '2' - Download a single Video as Audio
        '3' - Set URL of Video or Playlist 
        '4' - Set PATH of Save location (if path is empty, file saved at default location)
        '5' - Change Audioformat
        '?' - For help
        'e' - To exit

Enter:   """

mp3 = False

def main():
    clear()
    path = pathlib.Path(__file__).parent.absolute()
    global mp3
    url = ""
    

    while True:
       
        clear()
        if mp3: audiformat = "MP3"
        else:   audiformat = "MP4"

        print(STITLE)
        print("PATH: \t\t{0}\nURL: \t\t{1}\nAudioformat: \t{2}".format(
            path, url, audiformat))
        print(overlay, end="")
        
        enter = msvcrt.getch().decode('ASCII')      
        # msvcrt.getch(): gets only 1 char .decode('ASCII') 
        # decode('ASCII'): turns input(bytestring) into ASCII (char)


        if enter == '1':
            clear()
            plAudioDownload(url, path)
            input("Press ENTER to continue")

        elif enter == '2':
            clear()
            videoAudioDownload(url, path)
            input("Press ENTER to continue")
            
        elif enter == '3':
            clear()
            url = input("\nENTER YT Video or Playlist URL: ")

        elif enter == '4':
            clear()
            path = input("\nENTER PATH: ")
        
        elif enter == '5':
            mp3 = not mp3

        elif enter == '?':
            clear()
            help = """

            if the path is empty 
            the default save location is where the .py or .exe file is executed

            PRESS ANY KEY TO ESCAPE
            """
            print(help)
            input()

            
        elif enter == 'e':
            clear()
            print("EXIT")
            exit()
            

def plAudioDownload(url, path):

    global mp3
    pl = Playlist(url)
    maxvids = 0
    i = 0
    plurls = pl.video_urls

    for url in plurls:
        maxvids += 1

    print("Press \"Enter\" to DOWNLOAD Audio of Playlist, \"e\" to EXIT: ")
    enter = msvcrt.getch().decode('ASCII')

    if enter == '\r':
        print("\n\t START DOWNLOADING (in {}):\n".format(path))
        for url in plurls:
            try:
                yt = YouTube(url)

                while yt.title == "YouTube":
                    print("Error \nRequesting new ")
                    yt = YouTube(url)
            except KeyError as e:
                print(
                    "KEYERROR \"{}\"".format(e))
                print("{} is maybe  not available in your Country widepeeposad (skipped)".format(yt.title))
                print("Continuing with next Video in Playlist")
                continue
            except:
                print("ERROR MAYBE INCORRECT LINK")
                input()
                main()
                
            i+=1
            print("Downloading({0}/{1}): {2} ({3})".format(i, maxvids, yt.title, url))
            yt.streams.get_audio_only().download(path)
            print("Finished Downloading: {}".format(yt.title))
            
    elif enter == 'e':
        print("\nEXIT")
        main()

    else:
        print("\nEXIT")
        main()


def videoAudioDownload(url, path):
    global mp3

    print("Press \"Enter\" to DOWNLOAD Audio of Video, \"e\" to EXIT: ")
    enter = msvcrt.getch().decode('ASCII')

    if enter == '\r':
        print("\n\t START DOWNLOADING (in {}):\n".format(path))
        try:
            yt = YouTube(url)
            while yt.title == "YouTube":
                print("Error \nRequesting new ")
                yt = YouTube(url)
        except KeyError as e:
            print(
                "KEYERROR \"{}\"".format(e))
            print("{} is maybe  not available in your Country widepeeposad (skipped)".format(
                yt.title))
        except:
            print("ERROR MAYBE INCORRECT LINK")
            input()
            main()

        print(
            "Downloading: {0} ({1})".format(yt.title, url))
        yt.streams.get_audio_only().download(path)
        print("Finished Downloading: {}".format(yt.title))

    elif enter == 'e':
        print("\nEXIT")
        main()

    else:
        print("\nEXIT")
        main()


def clear():
    return os.system('cls')  # on Windows System


if __name__ == '__main__':
    main()

