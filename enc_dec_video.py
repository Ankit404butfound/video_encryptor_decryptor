import os
import sys

def encrypt(mp4, key):
    name = os.path.basename(mp4).split(".")[0]
    os.system(f"ffmpeg -i {mp4} -vcodec copy -acodec copy -encryption_scheme cenc-aes-ctr -encryption_key {key} -encryption_kid a7e61c373e219033c21091fa607bf3b8 {name}_encrypted.mp4")
    print(f"File has been encrypted with key '{key}'")

    

def decrypt(mp4, key):
    os.system(f"mpv --demuxer-lavf-o=decryption_key={key} {mp4}")
    print("Playing video")


if __name__ == "__main__":
    try:
        mp4 = sys.argv[1]
        key = sys.argv[2]
        command = sys.argv[3]

        if command == "encrypt":
            encrypt(mp4, key)

        else:
            decrypt(mp4, key)

    except Exception as e:
        print(e)
