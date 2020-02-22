from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import webbrowser
import os


#
#   DOWNLOAD VIDEO AS MP3 (maybe also MP4(Video)) to fixed Location(where main file is stored)
#   © by saltyDeADEYe
#


def main():

    clear()

    print("")

    sUrlSearch = "https://www.youtube.com/results?search_query="
    sUrlFirstResult = "https://www.youtube.com"
    sUrlDownload = "https://www.y2mate.com/youtube-mp3/"

    sSearchTerm = input("\nEnter your search term: ")

    print("\n\tYou searched for: " + sSearchTerm + "\n")

    sSearchTerm = sSearchTerm.replace(" ", "+")
    sUrlSearch += sSearchTerm

    webbrowser.open_new(sUrlSearch)

    ytHTML = getHTMLFile(sUrlSearch)

    createLinksFile("links.txt", ytHTML)

    sVideoUrl = getLine("links.txt", "watch")
    print(sVideoUrl)

    sDownloadLinkTerm = sVideoUrl.split("=")

    sDownloadLinkTerm = sDownloadLinkTerm[1]
    print(sDownloadLinkTerm)

    sUrlFirstResult += sVideoUrl
    print("First Video: \n\n\t" + sUrlFirstResult + "")
    webbrowser.open_new(sUrlFirstResult)
    print("\n\tOpened links in Browser \n")

    sUrlDownload += sDownloadLinkTerm
    print("Download Link: \n\n\t" + sUrlDownload + "")
    webbrowser.open_new(sUrlDownload)
    print("\n\tOpened link in Browser \n")


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
