import base64
import json
import cv2
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from .models import Usuario, Asistencia


def Home(request):
    return render(request, "home.html")


def detect(request):
    if request.method == "POST":
        data = json.loads(request.body)
        image_data = data.get("image")

        if image_data:
            image_data = image_data.split(",")[1]
            image_content = base64.b64decode(image_data)
            np_arr = np.frombuffer(image_content, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            try:
                face_recognizer = cv2.face.LBPHFaceRecognizer_create()
                face_recognizer.read("Home/static/modelo/modeloLBPHFace.xml")
            except AttributeError:
                return JsonResponse(
                    {"message": "Error al cargar el clasificador facial"}, status=500
                )

            face_classifier = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                return JsonResponse(
                    {"message": "No se detectaron rostros en la imagen"}, status=400
                )

            images = ["Alan", "Anthony", "Enzo", "Erick", "Luis"]
            for x, y, w, h in faces:
                rostro = gray[y : y + h, x : x + w]
                rostro_resized = cv2.resize(
                    rostro, (150, 150), interpolation=cv2.INTER_CUBIC
                )
                label, confidence = face_recognizer.predict(rostro_resized)
                print(f"Predicción: {images[label]}, Confianza: {confidence}")

            nombre_predicho = images[label]

            usuario, created = Usuario.objects.get_or_create(
                nombre=nombre_predicho, defaults={"activo": True}
            )

            asistencia = Asistencia.objects.create(
                usuario=usuario, confianza=float(confidence)
            )

            mensaje = f"Asistencia registrada para {nombre_predicho}"
            print(f"{mensaje} - ID: {asistencia.id}")

            return JsonResponse(
                {
                    "Prediccion": nombre_predicho,
                    "asistencia_id": asistencia.id,
                    "mensaje": mensaje,
                    "confianza": confidence,
                }
            )

        return JsonResponse({"message": "No se proporcionó imagen"}, status=400)

    return JsonResponse({"message": "Método no permitido"}, status=405)
