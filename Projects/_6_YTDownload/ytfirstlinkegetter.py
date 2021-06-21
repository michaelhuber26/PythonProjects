from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import webbrowser
import os
from pytube import YouTube



#
#   DOWNLOAD VIDEO AS MP3 (maybe also MP4(Video)) to fixed Location(where main file is stored)
#   © by saltyDeADEYe
#


def main():

    clear()

    print("")

    sSearchTerm = input("\nEnter your search term: ")
    url = getFirstVideoURL(sSearchTerm)
    print("\n\tYou searched for: " + sSearchTerm + "\n")

   
    yt = YouTube(url)
    stream = yt.streams

    # print(stream.all())   #print all avavialbe streams
    print("Link to Thumbnail:   {}".format(yt.thumbnail_url))

    enter = input("Press Enter to download Audio:")

    if enter == '':
        stream.get_audio_only().download()

    else:
        exit()



def getFirstVideoURL(sSearchTerm):

    sUrlFirstResult = "https://www.youtube.com"
    sUrlSearch = getSearchURL(sSearchTerm)

    print("sUrlSearch: " + sUrlSearch)

    ytHTML = getHTMLFile(sUrlSearch)

    createLinksFile("links.txt", ytHTML)

    sVideoUrl = getLine("links.txt", "watch")
    print("sVideoUrl: "+ sVideoUrl)

    sDownloadLinkTerm = sVideoUrl.split("=")

    sDownloadLinkTerm = sDownloadLinkTerm[1]
    print("sDownloadLinkTerm: " + sDownloadLinkTerm)

    sUrlFirstResult += sVideoUrl
    # print("First Video: \n\n\t" + sUrlFirstResult + "")
    # webbrowser.open_new(sUrlFirstResult)
    # print("\n\tOpened links in Browser \n")


    return sUrlFirstResult


def getSearchURL(sSearchTerm):
    sUrlSearch = "https://www.youtube.com/results?search_query="

    sSearchTerm = sSearchTerm.replace(" ", "+")
    sUrlSearch += sSearchTerm

    # webbrowser.open_new(sUrlSearch)   #opens link in browser
    return sUrlSearch





def clear():
    return os.system('cls')  # on Windows System


def getLine(path, stringToMatch):
    search = open(path)
    for line in search:
        if len(line) < 25:
            if stringToMatch in line:
                search.close()
                return line
    search.close()
    print("\n\tNO VIDEOS FOUND!!!")

    return "HALLO"


def getHTMLFile(sUrlSearch):

    try:
        ytFile = urllib.request.urlopen(sUrlSearch)
    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('URLError: {}'.format(e.reason))
    else:
        ytHTML = ytFile.read()
        ytFile.close()
        return ytHTML


def createLinksFile(name, HTMLFile):
    linkFile = open(name, "w")
    soup = BeautifulSoup(HTMLFile, features="html.parser")
    for links in soup.find_all('a'):
        linkFile.write(links.get('href')+"\n")

    linkFile.close()


if __name__ == '__main__':
    main()
