# Video encryption and decryption...
#### Please download ffmpeg from here https://www.gyan.dev/ffmpeg/builds/ and put the ffmpeg.exe in the same directory
#### Also download mpv-1.dll from here https://github.com/Ankit404butfound/data/blob/main/mpv-1.dll and do the same
#### Execute pip install -r requirements.txt

# Command to encrypt
#### `python enc_dec_video.py <video_to_encrypt>.mp4 <key_in_base_16> encrypt`

# Command to play encrypted file
#### `python tkmpvplayer.py <hex_key> <path_to_encrypted_file>`

#### Key for uploaded mp4 is 76a6c65c5ea762046bd749a2e632ccbb


# Command to build exe
#### Type `pyinstaller --onefile -w <path_to_python_file>`
#### You many remove the -w flag if you need console along with the exe for debugging.
