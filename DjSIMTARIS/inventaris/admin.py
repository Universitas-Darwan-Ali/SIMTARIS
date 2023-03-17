from django.contrib import admin
from .models import Kategori, Ruangan, Barang, Peminjaman

admin.site.site_header = 'SIM INVENTARIS UNDA'

class BarangAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'jumlah', 'kondisi', 'ruangan')
    list_filter = ('kategori', 'ruangan')

class PeminjamanAdmin(admin.ModelAdmin):
    list_display = ('barang', 'peminjam', 'tanggal_pinjam', 'tanggal_kembali', 'is_dipinjam')
    list_filter = ('tanggal_pinjam', 'tanggal_kembali', 'barang__kategori', 'barang__ruangan')
    search_fields = ('barang__nama', 'peminjam__username')

admin.site.register(Kategori)
admin.site.register(Ruangan)
admin.site.register(Barang, BarangAdmin)
admin.site.register(Peminjaman, PeminjamanAdmin)
