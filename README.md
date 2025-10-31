# Sistema de Registro de Asistencia con Reconocimiento Facial

Este proyecto es un aplicativo web diseñado para automatizar el registro de asistencia utilizando reconocimiento facial.  
El sistema se basa en el uso de la librería OpenCV para el procesamiento de imágenes y el entrenamiento de modelos de reconocimiento facial mediante el algoritmo **LBPH (Local Binary Patterns Histograms)**.  
Posteriormente, el modelo se integra en una aplicación web desarrollada en Python, permitiendo identificar a los usuarios en tiempo real y registrar su asistencia automáticamente.
---

## Características principales

- Detección y reconocimiento facial en tiempo real.  
- Soporte para múltiples personas.  
- Registro automático de asistencia con fecha y hora.  

---

**Lenguaje:**  
- Python 3.12.10

**Librerías y dependencias principales:**  
- OpenCV  
- NumPy  
- Django

**Pasos de instalación y configuración:**  

1. **Clonar el repositorio del proyecto:**  
  ```bash
  git clone https://github.com/tu-usuario/registro-asistencia-facial.git
  cd registro-asistencia-facial
  ```
2. **Instalar dependencias**
  ```bash
  pip install -r requeriments.txt
  ```
3. **Realizar migraciones**
  ```bash
python manage.py makemigrations
python manage.py migrate
```
4. **Ejecutar el servidor**
  ```bash
python manage.py runserver
```

