from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="asistencias"
    )
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(auto_now_add=True)
    confianza = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ["-fecha", "-hora"]

    def __str__(self):
        return f"{self.usuario.nombre} - {self.fecha} {self.hora.strftime('%H:%M')}"
