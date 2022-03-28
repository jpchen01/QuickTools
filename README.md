# Quick Tools
## A Collection of Scripts and Tools for future use

### Python
QR Code Generator : Written for Python 3.7, uses argparse, qrcode, PIL
- Creating Gifs with Alpha Channels : tif_to_gif.py, tif_req.txt

    Without Embedded Image
    ```
    python qr_code_gen.py --dest ../dest_path.png --color orange --data_sec google.com
    ```

    With Embedded Image
    ```
    python qr_code_gen.py --img_src ../a_src_image   --dest ../dest_path.png --color orange --data_sec google.com
    ```
