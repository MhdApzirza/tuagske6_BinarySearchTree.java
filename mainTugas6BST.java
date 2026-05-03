import java.util.Scanner;

class Node {
    int id;
    String nama;
    Node left, right;

    public Node(int id, String nama) {
        this.id = id;
        this.nama = nama;
        left = right = null;
    }
}

class BinarySearchTree {
    Node root;

    void insert(int id, String nama) {
        root = insertRec(root, id, nama);
    }

    Node insertRec(Node root, int id, String nama) {
        if (root == null) {
            root = new Node(id, nama);
            return root;
        }
        if (id < root.id)
            root.left = insertRec(root.left, id, nama);
        else if (id > root.id)
            root.right = insertRec(root.right, id, nama);
        return root;
    }

    Node search(Node root, int id) {
        if (root == null || root.id == id)
            return root;
        if (root.id < id)
            return search(root.right, id);
        return search(root.left, id);
    }

    void delete(int id) {
        root = deleteRec(root, id);
    }

    Node deleteRec(Node root, int id) {
        if (root == null) return root;
        if (id < root.id)
            root.left = deleteRec(root.left, id);
        else if (id > root.id)
            root.right = deleteRec(root.right, id);
        else {
            if (root.left == null) return root.right;
            else if (root.right == null) return root.left;
            root.id = minValue(root.right);
            root.right = deleteRec(root.right, root.id);
        }
        return root;
    }

    int minValue(Node root) {
        int minv = root.id;
        while (root.left != null) {
            minv = root.left.id;
            root = root.left;
        }
        return minv;
    }

    // --- FITUR TRAVERSAL TERPISAH ---
    void inorder(Node root) {
        if (root != null) {
            inorder(root.left);
            System.out.println("ID: " + root.id + " \t| Nama: " + root.nama);
            inorder(root.right);
        }
    }

    void preorder(Node root) {
        if (root != null) {
            System.out.println("ID: " + root.id + " \t| Nama: " + root.nama);
            preorder(root.left);
            preorder(root.right);
        }
    }

    void postorder(Node root) {
        if (root != null) {
            postorder(root.left);
            postorder(root.right);
            System.out.println("ID: " + root.id + " \t| Nama: " + root.nama);
        }
    }
}

public class Tugas6BST {
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();
        Scanner sc = new Scanner(System.in);

        // Masukkan 100 data otomatis
        int[][] excelData = {
            {5288, 5993, 8689, 8043, 8699, 2156, 4457, 8938, 2618, 9033},
            {9971, 3874, 5914, 2398, 3725, 5210, 7363, 7631, 4513, 5656},
            {6453, 8783, 8194, 9783, 3685, 4490, 8294, 8563, 1070, 5408},
            {8258, 9309, 1138, 2751, 3258, 6402, 7921, 9781, 3818, 5204},
            {6119, 1928, 4207, 7255, 5309, 2897, 8028, 1660, 3248, 5641},
            {7376, 3525, 4492, 7187, 1305, 6602, 8153, 3561, 5082, 7151},
            {7524, 9178, 9817, 4304, 6820, 9151, 3482, 3316, 5192, 7572},
            {7660, 9224, 5083, 6362, 6465, 9888, 4159, 4969, 5097, 6271},
            {9250, 3409, 4577, 6244, 8612, 4650, 6799, 9298, 4361, 4379},
            {6928, 3195, 5741, 6852, 8147, 8902, 8967, 1302, 2363, 6861}
        };
        String[][] excelNama = {
            {"pensil", "pulpen", "penghapus", "buku", "sampul", "penggaris", "kertas", "cat", "stabilo", "mobil"},
            {"motor", "becak", "sepeda", "kereta", "pesawat", "perahu", "kapal", "rakit", "kipas", "charger"},
            {"peci", "sarung", "sajadah", "smartphone", "jam", "televisi", "laptop", "komputer", "mouse", "keyboard"},
            {"tablet", "jendela", "kaca", "pintu", "kompor", "lemari", "kasur", "ranjang", "bantal", "baju"},
            {"kaos", "celana", "mukena", "jilbab", "pigura", "antena", "kulkas", "dispenser", "meja", "kursi"},
            {"kemoceng", "sapu", "gayung", "sabun", "sikat", "shampo", "botol", "gelas", "piring", "panci"},
            {"wajan", "blender", "galon", "cobek", "termos", "kran", "selang", "karpet", "tikar", "keset"},
            {"sepatu", "kaos kaki", "jaket", "piama", "piano", "gitar", "angklung", "suling", "toples", "parfum"},
            {"sisir", "topi", "gunting", "pisau", "kaleng", "tisu", "tas", "ikat pinggang", "korek api", "kopi"},
            {"gula", "cabai", "wortel", "timun", "apel", "jeruk", "tomat", "pisang", "pepaya", "bawang"}
        };

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                bst.insert(excelData[i][j], excelNama[i][j]);
            }
        }

        while (true) {
            System.out.println("\n=== MENU BINARY SEARCH TREE (BST) ===");
            System.out.println("1. Tambah Data Manual");
            System.out.println("2. Cari Data (by ID)");
            System.out.println("3. Hapus Data (by ID)");
            System.out.println("4. Tampilkan In-Order (Terurut)");
            System.out.println("5. Tampilkan Pre-Order");
            System.out.println("6. Tampilkan Post-Order");
            System.out.println("7. Keluar");
            System.out.print("Pilih Menu: ");
            int pil = sc.nextInt();

            switch (pil) {
                case 1:
                    System.out.print("ID Baru: "); int id = sc.nextInt();
                    System.out.print("Nama Baru: "); String nm = sc.next();
                    bst.insert(id, nm);
                    break;
                case 2:
                    System.out.print("Masukkan ID yang dicari: "); int idCari = sc.nextInt();
                    Node res = bst.search(bst.root, idCari);
                    if (res != null) System.out.println("Ditemukan: " + res.nama);
                    else System.out.println("Data tidak ditemukan.");
                    break;
                case 3:
                    System.out.print("ID yang dihapus: "); int idHapus = sc.nextInt();
                    bst.delete(idHapus);
                    System.out.println("ID " + idHapus + " berhasil dihapus.");
                    break;
                case 4:
                    System.out.println("\n--- IN-ORDER TRAVERSAL ---");
                    bst.inorder(bst.root);
                    break;
                case 5:
                    System.out.println("\n--- PRE-ORDER TRAVERSAL ---");
                    bst.preorder(bst.root);
                    break;
                case 6:
                    System.out.println("\n--- POST-ORDER TRAVERSAL ---");
                    bst.postorder(bst.root);
                    break;
                case 7:
                    System.out.println("Program Berakhir.");
                    System.exit(0);
                default:
                    System.out.println("Pilihan salah!");
            }
        }
    }
}