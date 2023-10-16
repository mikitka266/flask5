from django.shortcuts import render
from django.http import HttpResponse
import logging
from forms import ImageForm
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)


def main(request):
    logger.info('Main page accessed')
    return HttpResponse('Main')


def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, something went wrong')
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is the about page')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    
    else:
        form = ImageForm()
    return render(request, 'myproject/upload_image.html', {'form': form})