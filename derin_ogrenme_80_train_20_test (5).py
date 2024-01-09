from google.colab import drive
drive.mount('/content/drive')


import os

# Dosyalarınızın bulunduğu dizini belirtin
data_tumor = '/content/drive/MyDrive/Kidney_Cancer/Kidney Cancer/Tumor'
data_normal = '/content/drive/MyDrive/Kidney_Cancer/Kidney Cancer/Normal'

# Dosyaları listele
file_list = os.listdir(data_tumor)
file_list2 = os.listdir(data_normal)

# Dosyaları kontrol etmek için yazdırın
print(file_list)
print(file_list2)



import shutil
from sklearn.model_selection import train_test_split

# Dosyaların bulunduğu ana dizin
normal_path = os.path.join(data_normal)
tumor_path = os.path.join(data_tumor)

# Train ve test setlerini oluştur
normal_images = os.listdir(normal_path)
tumor_images = os.listdir(tumor_path)

# Train ve test setlerini oluşturulan klasörlere taşı
train_path = '/content/drive/MyDrive/Kidney_Cancer/train'
test_path = '/content/drive/MyDrive/Kidney_Cancer/test'
validation_path = '/content/drive/MyDrive/Kidney_Cancer/validation'

# Klasörleri oluştur
os.makedirs(os.path.join(train_path, 'normal'), exist_ok=True)
os.makedirs(os.path.join(train_path, 'tumor'), exist_ok=True)

os.makedirs(os.path.join(test_path, 'normal'), exist_ok=True)
os.makedirs(os.path.join(test_path, 'tumor'), exist_ok=True)

os.makedirs(os.path.join(validation_path, 'normal'), exist_ok=True)
os.makedirs(os.path.join(validation_path, 'tumor'), exist_ok=True)

# Normal ve tumor verilerini ayırmak için train_test_split kullanın
normal_train, normal_test = train_test_split(normal_images, test_size=0.2, random_state=42)
tumor_train, tumor_test = train_test_split(tumor_images, test_size=0.2, random_state=42)

# Train ve test setlerini oluşturulan normal ve tumor klasörlerine taşıyın
for image in normal_train:
    src = os.path.join(normal_path, image)
    dest = os.path.join(train_path, 'normal', image)
    shutil.copy(src, dest)

for image in normal_test:
    src = os.path.join(normal_path, image)
    dest = os.path.join(test_path, 'normal', image)
    shutil.copy(src, dest)

for image in tumor_train:
    src = os.path.join(tumor_path, image)
    dest = os.path.join(train_path, 'tumor', image)
    shutil.copy(src, dest)

for image in tumor_test:
    src = os.path.join(tumor_path, image)
    dest = os.path.join(test_path, 'tumor', image)
    shutil.copy(src, dest)

# Train setini daha da bölmek için %10'unu validation seti olarak kullanın
train_images = os.listdir(os.path.join(train_path, 'normal')) + os.listdir(os.path.join(train_path, 'tumor'))
train_data, validation_data = train_test_split(train_images, test_size=0.1, random_state=42)

# Validation setini oluşturulan validation klasörüne taşıyın
for image in validation_data:
    if image in os.listdir(os.path.join(train_path, 'normal')):
        src = os.path.join(train_path, 'normal', image)
        dest = os.path.join(validation_path, 'normal', image)
        shutil.move(src, dest)
    elif image in os.listdir(os.path.join(train_path, 'tumor')):
        src = os.path.join(train_path, 'tumor', image)
        dest = os.path.join(validation_path, 'tumor', image)
        shutil.move(src, dest)