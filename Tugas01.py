#2106145_A.Abdul Latif_Tugas01
def blind_search(start, goal, graph):

    # Inisialisasi antrian dan himpunan node yang telah dikunjungi
    queue = [[start]]
    visited = set()

    # Lakukan pencarian jalur terpendek
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Jika simpul yang dikunjungi sama dengan simpul tujuan, kembalikan jalur
        if node == goal:
            return path

        # Tambahkan simpul yang bertetanggaan dengan simpul yang sedang dikunjungi ke antrian
        # jika simpul tersebut belum dikunjungi sebelumnya
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    # Jika tidak ditemukan jalur, kembalikan None
    return None

# Contoh penggunaan program
graph = {
    0: [1, 3, 4],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2, 4],
    4: [0, 3],
}

start = 0
goal = 2

result = blind_search(start, goal, graph)

# Cek apakah ditemukan jalur atau tidak
if result is None:
    print("Tidak ada jalur yang ditemukan.")
else:
    print("Jalur terpendek dari", start, "ke", goal, "adalah:", result)