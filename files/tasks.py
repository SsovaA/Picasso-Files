from celery import shared_task
from .models import File
from .utils import *
from PIL import Image

@shared_task()
def file_process_task(file_id):
    try:
        file = File.objects.get(pk=file_id)
    except:
        print (f'File ID: {file_id} not found')
        return
    
    file_path = file.file.path
    match get_file_extention(file_path):
        case "txt":
            f = open(file_path, 'a')
            f.write("Append text")
            f.close()

        case "jpg":
            size = 128, 128
            try:
                im = Image.open(file_path)
                im.thumbnail(size, Image.Resampling.LANCZOS)
                im.save(file_path, "JPEG")
            except IOError:
                print (f'Cannot create thumbnail for {file.id}')

        case _:
            print("Other file")

    file.processed = True
    file.save()
