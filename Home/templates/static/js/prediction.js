const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
  
  // Ajusta el tamaño del canvas
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
  
  // Dibuja el frame del video
ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  // Convierte el canvas a blob
const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg'));
  
  // Envíalo a Python mediante fetch
const formData = new FormData();
formData.append("imagen", blob, "captura.jpg");
  
const respuesta = await fetch("http://127.0.0.1:8000/detect", {
    method: "POST",
    body: formData
});
  
const resultado = await respuesta.json();
console.log(resultado);