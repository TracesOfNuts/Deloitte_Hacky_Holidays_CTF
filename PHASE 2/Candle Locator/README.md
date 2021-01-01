![challenge](./img/Capture.PNG)

#### CHALLENGE INFORMATION

Do you know where these beautiful candles can be found?

*Author information: This challenge is developed by Deloitte.*

#### FILES

You will need the files below in order to solve this challenge.

[hanukkah.jpg](./img/hanukkah.jpg)

#### (50 Points) EXCHANGEABLE IMAGE FILE

We love these candles so much. We would like to know the street they can be found on. Can you find out?

*Flag format: streetname*
*Note: this is not a steganography challenge.*

---

#### (Solution) Candle Locator

Using the ExifTool (https://exiftool.org/), we can get the metadata of the image.

```
$ exiftool hanukkah.jpg
```

Output:

```
ExifTool Version Number         : 12.12
File Name                       : hanukkah.jpg
Directory                       : .
File Size                       : 1135 KiB
File Modification Date/Time     : 2020:12:27 10:38:41+08:00
File Access Date/Time           : 2021:01:01 20:59:10+08:00
File Inode Change Date/Time     : 2021:01:01 20:57:01+08:00
File Permissions                : rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 100
Y Resolution                    : 100
Resolution Unit                 : None
Y Cb Cr Positioning             : Centered
GPS Version ID                  : 2.3.0.0
XMP Toolkit                     : Image::ExifTool 10.80
Quality                         : 100%
DCT Encode Version              : 100
APP14 Flags 0                   : [14], Encoded with Blend=1 downsampling
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Image Width                     : 3000
Image Height                    : 3000
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3000x3000
Megapixels                      : 9.0
GPS Latitude                    : 52 deg 4' 40.06" N
GPS Longitude                   : 4 deg 20' 4.83" E
GPS Latitude Ref                : North
GPS Longitude Ref               : East
GPS Position                    : 52 deg 4' 40.06" N, 4 deg 20' 4.83" E
```

Now, use a GPS coordinate converter such as https://www.gps-coordinates.net/gps-coordinates-converter to get the location.

Flag:

```
Schenkkade
```

