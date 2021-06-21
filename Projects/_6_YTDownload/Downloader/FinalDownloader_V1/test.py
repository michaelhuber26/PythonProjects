try:
    from format_conv import format_conv
except Exception as e:
    print(e)


path = input("PATH: ")
f = format_conv(path)
input()
f.MP4toMP3(False)
print("FINISHED")



