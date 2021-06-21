try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Modules missing {}".format(e))


def main():

    while True:
        enter = input("1 To Download all Videos of YT Playlist as Audio \n
                      "2 To Download a single Video\n
                      "e To exit")
        if enter = '1':
            url = input("\nENTER YT Playlist URL: ")
            plAudioDownload(url)
        elif enter = '2':
            pass
        elif enter = 'e':
            print("EXIT")
            exit()


def plAudioDownload(url):

    pl = Playlist(url)
    maxvids = 0
    i = 0
    plurls = pl.video_urls

    for url in plurls:
        maxvids += 1

    enter = input(
        "Press \"Enter\" to DOWNLOAD Audio of Playlist, \"e\" to EXIT: ")

    if enter == '':
        print("\n\t START DOWNLOADING (in C:/download):\n")
        for url in plurls:
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
                print("Continuing with next Video in Playlist")
                continue

            i += 1
            print(
                "Downloading({0}/{1}): {2} ({3})".format(i, maxvids, yt.title, url))
            yt.streams.get_audio_only().download("/download")
            print("Finished Downloading: {}".format(yt.title))

    elif enter == 'e':
        print("\nEXIT")
        main()

    else:
        print("\nEXIT")
        exit()


if __name__ == '__main__':
    main()
