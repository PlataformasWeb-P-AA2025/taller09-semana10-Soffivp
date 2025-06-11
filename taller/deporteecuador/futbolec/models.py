from django.db import models

# Create your models here.
#Equipo de Futbol: nombre, siglas, username twitter

#Jugador: nombre, posición campo, número camiseta, sueldo, equipo de fútbol

#Campeonato: nombre de campeonato, nombre de auspiciante

#Campeonato Equipos: año, equipo de fútbol, campeonato

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=50)
    usernametwitter = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "%s - %s -  usuario: %s" % (self.nombre,
                self.siglas,
                self.usernametwitter)
