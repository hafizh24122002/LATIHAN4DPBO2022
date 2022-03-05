# LATIHAN4DPBO2022

*Saya Hafizh Lutfi Hidayat mengerjakan Latihan 4 dalam mata kuliah
Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.*

Link Desain : 
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Design1.png
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Design2.png

Saya membagi kelas kedalam dua bagian dimana pada bagian pertama menggunakan konsep *Hirearchical Inheritance*, dimana terdapat class `Vehicle` sebagai parent dari class `Ship` dan `Airplane`. Alasannya adalah karena `Ship` dan `Airplane` merupakan sebuah kendaraan atau `Vehicle`. Kemudian pada bagian kedua menggunakan konsep *Multiple Inheritance*, dimana terdapat class `Person` yang merupakan derived class dari dua class yaitu `Driver` dan `Job`. Alasannya adalah karena `Person` memiliki pekerjaan (`Job`) dan kendaraan (`Driver`). Pada awalnya saya ingin menggabungkan kedua desain menjadi satu dimana class `Driver` dapat dihubungkan dengan `Vehicle`, namun tidak jadi saya implementasikan karena attribute yang dispesifikasikan tidak cocok untuk melakukan hal tersebut. Jika saya memodifikasi attribute agar cocok maka akan menjadi tidak sesuai spesifikasi yang diberikan karena perubahan yang diperlukan cukup drastis.

Tipe data yang digunakan menyesuaikan dengan kebutuhan. Terdapat juga banyak penggunaan tipe data enum pada program ini, alasannya adalah untuk menjaga integritas data jika ingin diolah dimana menurut saya menjadi hal yang cukup penting untuk pengembangan selanjutnya khususnya untuk attribute yang memiliki anggota list yang terbatas. Tentunya enum tidak bisa diimplementasikan untuk semua attribute khususnya untuk attribute yang bersifat dinamis dimana anggota list dapat bertambah atau berkurang (misalnya pada tipe bahan bakar dimana terus dilakukan inovasi dengan teknologi serta sumber daya baru), atau pada attribute yang memiliki input yang sangat luas sehingga tidak mungkin untuk dibuat list nya (misalnya nama).

Untuk method `move()` pada class `Vehicle` saya buat sehingga dapat menerima input jenis kendaraan manakah yang sedang bergerak, Jadi pada class `Ship` dan `Airplane` terdapat method tambahan yang menggunakan method dari `Vehicle` ditambahkan dengan parameter yang sesuai.

Link Hasil Eksekusi:
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Result/1.png
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Result/2.png
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Result/3.png
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Result/4.png
- https://github.com/hafizh24122002/LATIHAN4DPBO2022/blob/main/Picture/Result/5.png
