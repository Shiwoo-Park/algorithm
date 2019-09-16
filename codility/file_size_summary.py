"""
input
'my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'

output
'music 1011b\nimages 0b\nmovies 10200b\nother 105b'
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6

    music_exts = ["mp3", "aac", "flac"]
    img_exts = ["jpg", "bmp", "gif"]
    mov_exts = ["mp4", "avi", "mkv"]

    files = S.split("\n")
    sizes = [0, 0, 0, 0]

    for file in files:
        file_name, file_size = file.split()
        ext = file_name.split(".")[-1]
        size = int(file_size[:-1])
        # print("{} / {} / {}".format(file, ext, size))

        if ext in music_exts:
            sizes[0] += size
        elif ext in img_exts:
            sizes[1] += size
        elif ext in mov_exts:
            sizes[2] += size
        else:  # other
            sizes[3] += size

    return "music {}b\nimages {}b\nmovies {}b\nother {}b".format(*sizes)

