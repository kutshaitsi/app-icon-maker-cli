import sys
import os
import json
from PIL import Image

formats = [
    ("iPhone Notification iOS 7 - 14 20pt_2x", (40, 40), 'iphone', '2x', '20x20'),
    ("iPhone Notification iOS 7 - 14 20pt_3x", (60, 60), 'iphone', '3x', '20x20'),

    ("iPhone Settings iOS 7 - 14 29pt_2x", (58, 58), 'iphone', '2x', '29x29'),
    ("iPhone Settings iOS 7 - 14 29pt_3x", (87, 87), 'iphone', '3x', '29x29'),

    ("iPhone Spotlight iOS 7 - 14 40pt_2x", (80, 80), 'iphone', '2x', '40x40'),
    ("iPhone Spotlight iOS 7 - 14 40pt_3x", (120, 120), 'iphone', '3x', '40x40'),

    ("iPhone App iOS 7 - 14 60pt_2x", (120, 120), 'iphone', '2x', '60x60'),
    ("iPhone App iOS 7 - 14 60pt_3x", (180, 180), 'iphone', '3x', '60x60'),

    ("iPad Notification iOS 7 - 14 20pt_1x", (20, 20), 'ipad', '1x', '20x20'),
    ("iPad Notification iOS 7 - 14 20pt_2x", (40, 40), 'ipad', '2x', '20x20'),

    ("iPad Settings iOS 7 - 14 29pt_1x", (29, 29), 'ipad', '1x', '29x29'),
    ("iPad Settings iOS 7 - 14 29pt_2x", (58, 58), 'ipad', '2x', '29x29'),

    ("iPad Spotlight iOS 7 - 14 40pt_1x", (40, 40), 'ipad', '1x', '40x40'),
    ("iPad Spotlight iOS 7 - 14 40pt_2x", (80, 80), 'ipad', '2x', '40x40'),

    ("iPad App iOS 7 - 14 76pt_1x", (76, 76), 'ipad', '1x', '76x76'),
    ("iPad App iOS 7 - 14 76pt_2x", (152, 152), 'ipad', '2x', '76x76'),

    ("iPad (12.9-inch) App iOS 9 - 14 83.5pt_2x", (167, 167), 'ipad', '2x', '83.5x83.5'),

    ("App Store iOS 1024pt_1x", (1024, 1024), 'ios-marketing', '1x', '1024x1024'),

    ("Mac 16pt_1x", (16, 16), 'mac', '1x', '16x16'),
    ("Mac 16pt_2x", (32, 32), 'mac', '2x', '16x16'),

    ("Mac 32pt_1x", (32, 32), 'mac', '1x', '32x32'),
    ("Mac 32pt_2x", (64, 64), 'mac', '2x', '32x32'),

    ("Mac 128pt_1x", (128, 128), 'mac', '1x', '128x128'),
    ("Mac 128pt_2x", (256, 256), 'mac', '2x', '128x128'),

    ("Mac 256pt_1x", (256, 256), 'mac', '1x', '256x256'),
    ("Mac 256pt_2x", (512, 512), 'mac', '2x', '256x256'),

    ("Mac 512pt_1x", (512, 512), 'mac', '1x', '512x512'),
    ("Mac 512pt_2x", (1024, 1024), 'mac', '2x', '512x512'),
]


def make_app_icon():
    source_file = sys.argv[1]
    output_path = sys.argv[2]

    app_icon_directory = os.path.join(output_path, "AppIcon.appiconset")

    if not os.path.exists(app_icon_directory):
        os.makedirs(app_icon_directory)

    with Image.open(source_file) as image:
        if image.size != (1024, 1024):
            raise Exception("The image size must be 1024x1024.")

        metadata_bus = []

        for name, size, idiom, scale, size_class in formats:
            duplication = image.copy()

            duplication.thumbnail(size)

            file_name = f'{name}.' + f'{image.format}'.lower()
            file_path = os.path.join(app_icon_directory, file_name)
            duplication.save(file_path, image.format)

            metadata_bus.append({'filename': file_name, 'idiom': idiom, 'scale': scale, 'size': size_class})

        contents_json_data = {
            'images': metadata_bus,
            'info': {
                'author': 'xcode',
                'version': 1
            }
        }

        contents_json_file = os.path.join(app_icon_directory, 'Contents.json')
        with open(contents_json_file, 'w', encoding='utf-8') as file:
            json.dump(contents_json_data, file)


if __name__ == '__main__':
    make_app_icon()
