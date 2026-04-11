import sys

# Class untuk menyimpan Node (Data Satuan)
class Node:
    def __init__(self, id_data, nama):
        self.id = id_data
        self.nama = nama
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 1. Tambah Data (Insert)
    def insert(self, id_data, nama):
        if self.root is None:
            self.root = Node(id_data, nama)
        else:
            self._insert_rec(self.root, id_data, nama)

    def _insert_rec(self, root, id_data, nama):
        if id_data < root.id:
            if root.left is None:
                root.left = Node(id_data, nama)
            else:
                self._insert_rec(root.left, id_data, nama)
        elif id_data > root.id:
            if root.right is None:
                root.right = Node(id_data, nama)
            else:
                self._insert_rec(root.right, id_data, nama)

    # 2. Cari Data (Search)
    def search(self, root, id_data):
        if root is None or root.id == id_data:
            return root
        if id_data < root.id:
            return self.search(root.left, id_data)
        return self.search(root.right, id_data)

    # 3. Hapus Data (Delete)
    def delete(self, id_data):
        self.root = self._delete_rec(self.root, id_data)

    def _delete_rec(self, root, id_data):
        if root is None: return root
        if id_data < root.id:
            root.left = self._delete_rec(root.left, id_data)
        elif id_data > root.id:
            root.right = self._delete_rec(root.right, id_data)
        else:
            if root.left is None: return root.right
            elif root.right is None: return root.left
            temp = self._min_value_node(root.right)
            root.id = temp.id
            root.nama = temp.nama
            root.right = self._delete_rec(root.right, temp.id)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left: current = current.left
        return current

    # --- FITUR TRAVERSAL TERPISAH ---
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"ID: {root.id}\t| Nama: {root.nama}")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(f"ID: {root.id}\t| Nama: {root.nama}")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"ID: {root.id}\t| Nama: {root.nama}")

def main():
    bst = BinarySearchTree()
    
    # Memasukkan 100 data dari Excel ke dalam Tuple
    data_list = [
        (5288, "pensil"), (5993, "pulpen"), (8689, "penghapus"), (8043, "buku"), (8699, "sampul"),
        (2156, "penggaris"), (4457, "kertas"), (8938, "cat"), (2618, "stabilo"), (9033, "mobil"),
        (9971, "motor"), (3874, "becak"), (5914, "sepeda"), (2398, "kereta"), (3725, "pesawat"),
        (5210, "perahu"), (7363, "kapal"), (7631, "rakit"), (4513, "kipas"), (5656, "charger"),
        (6453, "peci"), (8783, "sarung"), (8194, "sajadah"), (9783, "smartphone"), (3685, "jam"),
        (4490, "televisi"), (8294, "laptop"), (8563, "komputer"), (1070, "mouse"), (5408, "keyboard"),
        (8258, "tablet"), (9309, "jendela"), (1138, "kaca"), (2751, "pintu"), (3258, "kompor"),
        (6402, "lemari"), (7921, "kasur"), (9781, "ranjang"), (3818, "bantal"), (5204, "baju"),
        (6119, "kaos"), (1928, "celana"), (4207, "mukena"), (7255, "jilbab"), (5309, "pigura"),
        (2897, "antena"), (8028, "kulkas"), (1660, "dispenser"), (3248, "meja"), (5641, "kursi"),
        (7376, "kemoceng"), (3525, "sapu"), (4492, "gayung"), (7187, "sabun"), (1305, "sikat"),
        (6602, "shampo"), (8153, "botol"), (3561, "gelas"), (5082, "piring"), (7151, "panci"),
        (7524, "wajan"), (9178, "blender"), (9817, "galon"), (4304, "cobek"), (6820, "termos"),
        (9151, "kran"), (3482, "selang"), (3316, "karpet"), (5192, "tikar"), (7572, "keset"),
        (7660, "sepatu"), (9224, "kaos kaki"), (5083, "jaket"), (6362, "piama"), (6465, "piano"),
        (9888, "gitar"), (4159, "angklung"), (4969, "suling"), (5097, "toples"), (6271, "parfum"),
        (9250, "sisir"), (3409, "topi"), (4577, "gunting"), (6244, "pisau"), (8612, "kaleng"),
        (4650, "tisu"), (6799, "tas"), (9298, "ikat pinggang"), (4361, "korek api"), (4379, "kopi"),
        (6928, "gula"), (3195, "cabai"), (5741, "wortel"), (6852, "timun"), (8147, "apel"),
        (8902, "jeruk"), (8967, "tomat"), (1302, "pisang"), (2363, "pepaya"), (6861, "bawang")
    ]

    for id_d, nm in data_list:
        bst.insert(id_d, nm)

    while True:
        print("\n" + "="*40)
        print("  SISTEM BST BARANG - MUHAMMAD APZIRZA RAFI")
        print("="*40)
        print("1. Tambah Data Baru")
        print("2. Cari Barang (by ID)")
        print("3. Hapus Barang (by ID)")
        print("4. Tampilkan In-Order (Urut ID)")
        print("5. Tampilkan Pre-Order (Akar ke Anak)")
        print("6. Tampilkan Post-Order (Anak ke Akar)")
        print("7. Keluar")
        
        pil = input("Pilih Menu: ")
        
        if pil == '1':
            try:
                id_i = int(input("Masukkan ID Baru: "))
                nm_i = input("Masukkan Nama Barang: ")
                bst.insert(id_i, nm_i)
                print("Data Berhasil Masuk!")
            except ValueError:
                print("Error: ID harus berupa angka!")
        elif pil == '2':
            id_c = int(input("Masukkan ID yang Dicari: "))
            res = bst.search(bst.root, id_c)
            if res:
                print(f"Hasil Pencarian: ID {res.id} adalah {res.nama}")
            else:
                print("Data Tidak Ditemukan!")
        elif pil == '3':
            id_h = int(input("Masukkan ID yang Akan Dihapus: "))
            bst.delete(id_h)
            print(f"Proses Penghapusan ID {id_h} Selesai.")
        elif pil == '4':
            print("\n--- IN-ORDER TRAVERSAL (HASIL TERURUT) ---")
            bst.inorder(bst.root)
        elif pil == '5':
            print("\n--- PRE-ORDER TRAVERSAL (PENSIL DI ATAS) ---")
            bst.preorder(bst.root)
        elif pil == '6':
            print("\n--- POST-ORDER TRAVERSAL (PENSIL DI BAWAH) ---")
            bst.postorder(bst.root)
        elif pil == '7':
            print("Terima kasih, program berakhir.")
            break
        else:
            print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()