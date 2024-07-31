import face_recognition
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SuspectForm
from .models import Suspect
import face_recognition

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")


def recognize_suspect(photo):
    # Load the uploaded image
    uploaded_image = face_recognition.load_image_file(photo)
    uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

    if not uploaded_face_encodings:
        return None

    uploaded_face_encoding = uploaded_face_encodings[0]

    suspects = Suspect.objects.all()
    for suspect in suspects:
        suspect_image_path = suspect.photo.path
        suspect_image = face_recognition.load_image_file(suspect_image_path)
        suspect_face_encodings = face_recognition.face_encodings(suspect_image)

        if not suspect_face_encodings:
            continue

        suspect_face_encoding = suspect_face_encodings[0]

        match = face_recognition.compare_faces([uploaded_face_encoding], suspect_face_encoding)[0]
        if match:
            return suspect

    return None

@login_required
def upload_suspect(request):
    if request.method == 'POST':
        form = SuspectForm(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']
            suspect = recognize_suspect(photo)
            if suspect:
                # Display suspect details if recognized
                return render(request, 'suspect_details.html', {'suspect': suspect})
            else:
                # Save new suspect if not recognized
                form.save()
                return redirect('suspect_list')
    else:
        form = SuspectForm()
    return render(request, 'upload_suspect.html', {'form': form})

@login_required
def suspect_list(request):
    suspects = Suspect.objects.all()
    return render(request, 'suspect_list.html', {'suspects': suspects})
