import os
import shutil
from dotenv import load_dotenv

load_dotenv()


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def create_directory(destination, light_cal=False, subfolder=''):
    if light_cal:
        folder_path = os.path.join(os.getenv('LIGHTS_DIR'), os.path.join(subfolder, destination))
    elif destination in cal_types:
        folder_path = os.path.join(os.getenv(f'{destination.upper()}_DIR'), folder_name)
    else:
        folder_path = os.path.join(os.getenv('LIGHTS_DIR'), os.path.join(destination, f'lights\\{folder_name}'))

    if os.path.exists(folder_path):
        print(f'Skipping create sub-directory {folder_path} as it already exists')
        return

    print(f'Creating a {destination} directory for {folder_path}')
    os.makedirs(folder_path)


def move_files(subdir):
    try:
        cwd = os.getcwd()

        if subdir in cal_types:
            file_dir_src = os.path.join(cwd, f'data\\{subdir}')
            file_dir_dest = os.path.join(os.getenv(f'{subdir.upper()}_DIR'), folder_name)
        else:
            file_dir_src = os.path.join(cwd, f'data\\lights\\{subdir}')
            file_dir_dest = os.path.join(os.getenv('LIGHTS_DIR'), f'{subdir}\\lights\\{folder_name}')

        for file in get_files(file_dir_src):
            if file.endswith('.jpg'):
                print(f'Skipping JPG file {file}')
                continue

            print(f'Moving {file}')
            shutil.move(os.path.join(file_dir_src, file), os.path.join(file_dir_dest, file))
    except Exception as e:
        print(f'An exception occurred {e}')


def make_symlinks(subfolder):
    for cal_type in cal_types:
        create_directory(cal_type, True, subfolder)
        cal_src = os.path.join(os.getenv(f'{cal_type.upper()}_DIR'), folder_name)
        cal_dest = os.path.join(os.getenv('LIGHTS_DIR'), f'{subfolder}\\{cal_type}\\{folder_name}')

        os.symlink(cal_src, cal_dest)


prefix = os.getenv("PREFIX")
suffix = os.getenv("SUFFIX")
cal_types = ['flats', 'bias']
folder_name = f'{prefix}_{suffix}'
light_folders = os.listdir(os.path.join(os.getcwd(), 'data\\lights'))

for cal_type in cal_types:
    create_directory(cal_type)
    move_files(cal_type)

for light in light_folders:
    create_directory(light)
    move_files(light)
    make_symlinks(light)
