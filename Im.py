import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd
import qrcode

files = glob.glob("C:/Vanya/Research/Dataset/*.jpg")

column_names = ["image", "exifdata", "qrcode", "edge"]
df = pd.DataFrame(columns=column_names)

exif_datas = []
qrcodes = []
for file in files:
    basename = os.path.basename(file)
    filename = os.path.splitext(basename)[0]

    img = Image.open(file)
    exif_data = img.getexif()

    if exif_data:
        exif_content = []
        img_dict = dict(exif_data)

        interested_tags = ["Make", "Model", "Software", "DateTime"]
        exif_file_path = f"C:/Vanya/Research/Dataset/exifdata/{filename}.txt"
        with open(exif_file_path, 'w') as f:
            for key, val in img_dict.items():
                f.write('%s - %s\n' % (TAGS[key], val))

                if(TAGS[key] in interested_tags):
                    exif_content.append('%s - %s' % (TAGS[key], val))

        exif_datas.append(exif_file_path)
        code_generator = qrcode.make((" ".join(exif_content)))
        qrcode_path = f"C:/Vanya/Research/Dataset/qrcode/{filename}.png"
        code_generator.save(qrcode_path)
        qrcodes.append(qrcode_path)

df["image"] = files
df["exifdata"] = exif_datas
df["qrcode"] = qrcodes

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
print(df)

