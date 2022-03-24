import argparse

import qrcode
from qrcode.image.styledpil import StyledPilImage
# Some import issues, need to fix
# from qrcode.image.styles.moduledrawers.pil import (
#     SquareModuleDrawer,
#     GappedSquareModuleDrawer,
#     CircleModuleDrawer,
#     RoundedModuleDrawer,
#     VerticalBarsDrawer,
#     HorizontalBarsDrawer
# )
from qrcode.image.styles.colormasks import *

from PIL import Image

class QrCodeGen():

    def __init__(self):

        self.parser = argparse.ArgumentParser(
            description= 'Generate Custom Qr Codes', 
            epilog= 'Qr Code Generated',
            argument_default=None,
            add_help=True
        )

        self.parser.add_argument(
            '--dest',
            action='store',
            nargs=1,
            default=None,
            required=True,
            help='write qr code to filepath at dest'
        )

        self.parser.add_argument(
            '--img_src',
            action='store',
            nargs=1,
            default=None,
            required=False,
            help='Logo to put in Qr Code'
        )

        self.parser.add_argument(
            '--data_src',
            action='store',
            nargs=1,
            default=None,
            required=True,
            help='Data to convert to QR Code'
        )

        self.parser.add_argument(
            '--color',
            action='store',
            nargs=1,
            default=None,
            required=False,
            help='Color of Qr Code Lines'
        )

        self.parser.add_argument(
            '--style',
            action='store',
            nargs=1,
            default=None,
            required=False,
            choices= ['square', 'gapped_square', 'circle',
             'rounded', 'vertical_bars', 'horizontal_bars'],
            help='Color of Qr Code Lines'
        )

        self.args = self.parser.parse_args()
        self.resolve_args()

    def resolve_args(self):
        logo = None

        if None != self.args.img_src:
            logo = Image.open(self.args.img_src[0])

            qr_width = 100
            
            # adjust image size
            wpercent = (qr_width/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((qr_width, hsize), Image.ANTIALIAS)

        else:
            logo = Image.new("RGB", (0,0))
        

        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

        # adding URL or text to QRcode
        QRcode.add_data(self.args.data_src[0])
        
        # generating QR code
        QRcode.make()
        
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=self.args.color[0], back_color="white",
            # module_drawer=self.get_style()
            ).convert('RGB')
        
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        
        # save the QR code generated
        QRimg.save(self.args.dest[0])
        
        print('QR code generated!')

    # def get_style(self):
    #     if None == self.arg.style:
    #         return RoundedModuleDrawer()
    #     elif 'square' == self.arg.style[0]:
    #         return SquareModuleDrawer()
    #     elif 'gapped' == self.arg.style[0]:
    #         return GappedSquareModuleDrawer()
    #     elif 'circle' == self.arg.style[0]:
    #         return CircleModuleDrawer()
    #     elif 'round' == self.arg.style[0]:
    #         return RoundedModuleDrawer()
    #     elif 'vertical' == self.arg.style[0]:
    #         return VerticalBarsDrawer()
    #     elif 'horizontal' == self.arg.style[0]:
    #         return HorizontalBarsDrawer()
    #     else:
    #         return SquareModuleDrawer()

        

if __name__ == "__main__":
    an_obj = QrCodeGen()
