from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Ruangan(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Barang(models.Model):
    nama = models.CharField(max_length=50)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    kondisi = models.CharField(max_length=50)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Peminjaman(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    peminjam = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()

    def __str__(self):
        return f"{self.barang.nama} dipinjam oleh {self.peminjam.username}"

    def is_dipinjam(self):
        return self.tanggal_kembali is None

    is_dipinjam.boolean = True
    is_dipinjam.short_description = 'Status Peminjaman'
