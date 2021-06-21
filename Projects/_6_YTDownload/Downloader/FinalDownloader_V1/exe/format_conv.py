from moviepy.editor import AudioFileClip
import re
import os

class format_conv:


    def __init__(self, path):
        self.tgt_folder = path
        

    #
    def MP4toMP3(self, deletemp4):

        for file in [n for n in os.listdir(self.tgt_folder) if re.search('mp4', n)]:
            full_path = os.path.join(self.tgt_folder, file)
            output_path = os.path.join(
                self.tgt_folder, os.path.splitext(file)[0] + '.mp3')
            # .subclip(10,)  # disable if do not want any clipping
            clip = AudioFileClip(full_path)
            clip.write_audiofile(output_path)
            
            if deletemp4:
                print("Deleting {}".format(full_path))
                os.remove(full_path)    # deletes the mp4 file
            else: pass
