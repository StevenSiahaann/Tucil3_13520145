# Tucil3_13520145

15-Puzzle Solver Using Branch And Bound adalah program untuk menyelesaikan 15-Puzzle dengan memperhatikan fungsi cost dan level setiap simpul. Program ini pada dasarnya adalah BFS namun terdapat prioritas saat memasukkan ke dalam queue.

Pada dasarnya algoritma Branch and Bound adalah suatu algoritma pencarian solusi yang digunakan untuk persoalan optimisasi. Lebih rinci untuk meminimalkan atau memaksimalkan suatu fungsi objektif sambil tidak melanggar batasan persoalan. Algoritma memiliki suatu fungsi pembatasan yang berguna untuk “memangkas” jalur yang dianggap tidak mengarah ke suatu solusi.

#Pada program ini diset default ukuran puzzle adalah 4x4
Jika anda ingin mengganti ukuran puzzle silahkan ubah nilai pada N (line 6)

Pastikkan IDE dan compiler anda support bahasa python.

Pastikan anda sudah mendownload modul/package yang akan digunakan ,yakni : numpy,copy,queue,time

Cara menjalankan Program : 
1. Siapkan IDE terbaik anda
2. Silahkan melakukan run program
3. Ikuti petunjuk yang terdapat pada terminal
4. Selamat Puzzle anda berhasil diselesaikan.

default folder pada program ini adalah : testcase

Jika anda ingin membaca puzzle dari file yang berbeda letak nya dengan default folder:
1. Silahkan masukkan nama folder, namun sebelumnya anda dapat menghilangkan line 192 dan membuat line 194 tidak menjadi komentar(hilangkan #)
2. Silahkan run program
3. Tunggu hingga hasil keluar
4. Selamat Puzzle anda berhasil diselesaikan


Jika anda ingin memasukkan puzzle manual :
1. Silahkan masukkan nama folder yang berisikan nama file tempat anda menuliskan matrix secara manual, namun sebelumnya anda dapat menghilangkan line 197 dan membuat line 199 tidak menjadi komentar(hilangkan #), jika tidak anda hanya dapat menentukan nama file dan nama folder mengikuti default.
2. Silahkan run program
3. Masukkan setiap elemen matrix secara manual
3. Tunggu hingga hasil keluar
4. Selamat Puzzle anda berhasil diselesaikan

Pada akhir program akan menampilkan susunan awal matrix,langkah menyelesaikan puzzle,sigma fungsi kurang(i) + x,fungsi kurang(i),  rute(path) menuju solusi dari puzzle,level ditemukannya solusi,waktu pencarian,serta simpul yang dibangkitkan.




Steven Gianmarg Haposan Siahaan 
13520145
K01
