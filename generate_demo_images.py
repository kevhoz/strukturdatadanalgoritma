"""
Script untuk generate Demo Awal images (PNG) untuk semua pertemuan baru.
Menggunakan PIL/Pillow dengan style dark theme (Atom One Dark).
Jalankan: python generate_demo_images.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# KONFIGURASI STYLE (Atom One Dark)
# ============================================================
BG_COLOR       = (33, 37, 43)       # background gelap
PANEL_COLOR    = (40, 44, 52)       # panel sedikit lebih terang
GUTTER_COLOR   = (35, 39, 46)       # gutter nomor baris
HEADER_COLOR   = (30, 33, 40)       # header bar
BORDER_COLOR   = (60, 65, 75)       # border tipis

# Warna teks
COLOR_WHITE    = (220, 223, 228)    # teks biasa
COLOR_KEYWORD  = (198, 120, 221)    # keyword (class, def, if, return, ...)
COLOR_STRING   = (152, 195, 121)    # string
COLOR_NUMBER   = (209, 154, 102)    # angka
COLOR_COMMENT  = (92, 99, 112)      # komentar
COLOR_FUNC     = (97, 175, 239)     # nama fungsi
COLOR_SELF     = (224, 108, 117)    # self / parameter
COLOR_CYAN     = (86, 182, 194)     # None / True / False

IMG_WIDTH  = 700
PADDING    = 20
GUTTER_W   = 40
LINE_H     = 22
FONT_SIZE  = 14
HEADER_H   = 32


def load_font(size=FONT_SIZE):
    """Coba load monospace font, fallback ke default."""
    font_paths = [
        "C:/Windows/Fonts/consola.ttf",      # Consolas
        "C:/Windows/Fonts/cour.ttf",         # Courier New
        "C:/Windows/Fonts/lucon.ttf",        # Lucida Console
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def simple_colorize(token: str):
    """Kembalikan warna berdasarkan isi token (sederhana)."""
    keywords = {"class", "def", "if", "else", "elif", "return", "while",
                "for", "in", "not", "and", "or", "import", "from", "pass",
                "None", "True", "False", "print", "self", "is", "lambda",
                "try", "except", "with", "as", "raise", "break", "continue"}
    if token in keywords:
        if token in ("None", "True", "False"):
            return COLOR_CYAN
        if token == "self":
            return COLOR_SELF
        return COLOR_KEYWORD
    if token.startswith(("#",)):
        return COLOR_COMMENT
    if token.startswith(('"', "'")) or (token.startswith('"""') or token.startswith("'''")):
        return COLOR_STRING
    if token.lstrip('-').isdigit():
        return COLOR_NUMBER
    return COLOR_WHITE


def render_line_colored(draw, x, y, code_line, font):
    """Render satu baris kode dengan pewarnaan token sederhana."""
    # Komentar: seluruh baris berwarna sama
    stripped = code_line.lstrip()
    if stripped.startswith("#"):
        draw.text((x, y), code_line, font=font, fill=COLOR_COMMENT)
        return

    # String pendek dalam tanda kutip
    # Tokenisasi sederhana: split by space, tapi pertahankan spasi
    col = x
    tokens = code_line.split(" ")
    for i, tok in enumerate(tokens):
        color = simple_colorize(tok.strip(":(),=[]{}"))
        # Cek apakah ada string literal
        if ('"' in tok or "'" in tok) and not tok.startswith("#"):
            color = COLOR_STRING
        draw.text((col, y), tok, font=font, fill=color)
        col += font.getlength(tok) + font.getlength(" ")


def make_image(title: str, subtitle: str, code_lines: list, output_path: str):
    """
    Buat satu PNG image berisi kode program.

    Args:
        title: judul header (contoh: "Demo Awal 1 - Circular LL")
        subtitle: baris kecil di bawah title
        code_lines: list of string, tiap string = 1 baris kode
        output_path: path lengkap file PNG output
    """
    font      = load_font(FONT_SIZE)
    font_bold = load_font(FONT_SIZE + 1)
    font_sm   = load_font(FONT_SIZE - 2)

    num_lines  = len(code_lines)
    code_area_h = num_lines * LINE_H + PADDING
    img_height  = HEADER_H + PADDING + code_area_h + PADDING

    img  = Image.new("RGB", (IMG_WIDTH, img_height), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # --- Header bar ---
    draw.rectangle([0, 0, IMG_WIDTH, HEADER_H], fill=HEADER_COLOR)
    draw.line([(0, HEADER_H), (IMG_WIDTH, HEADER_H)], fill=BORDER_COLOR, width=1)

    # Traffic-light dots
    dot_y = HEADER_H // 2
    draw.ellipse([12, dot_y-5, 22, dot_y+5], fill=(255, 95, 87))
    draw.ellipse([28, dot_y-5, 38, dot_y+5], fill=(255, 189, 46))
    draw.ellipse([44, dot_y-5, 54, dot_y+5], fill=(40, 200, 64))

    # Title text
    draw.text((68, dot_y - FONT_SIZE // 2 + 1), title, font=font_bold, fill=COLOR_WHITE)

    # Subtitle kecil (pojok kanan)
    sub_w = font_sm.getlength(subtitle)
    draw.text((IMG_WIDTH - sub_w - 12, dot_y - (FONT_SIZE - 2) // 2 + 1),
              subtitle, font=font_sm, fill=COLOR_COMMENT)

    # --- Gutter ---
    draw.rectangle([0, HEADER_H + 1, GUTTER_W, img_height], fill=GUTTER_COLOR)

    # --- Kode ---
    code_start_y = HEADER_H + PADDING
    for idx, line in enumerate(code_lines):
        y = code_start_y + idx * LINE_H
        # Nomor baris
        line_num = str(idx + 1)
        num_w = font_sm.getlength(line_num)
        draw.text((GUTTER_W - num_w - 6, y + 2), line_num,
                  font=font_sm, fill=COLOR_COMMENT)
        # Kode
        render_line_colored(draw, GUTTER_W + 10, y, line, font)

    # --- Border bawah ---
    draw.line([(0, img_height - 1), (IMG_WIDTH, img_height - 1)],
              fill=BORDER_COLOR, width=1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"  Saved: {output_path}")


# ============================================================
# DATA KODE UNTUK SETIAP DEMO AWAL
# ============================================================

images_data = {

    # ── Pert 15-16 ──────────────────────────────────────────
    "images/pert15-16/demo_awal_1.png": {
        "title": "Demo Awal 1 - Circular Linked List",
        "subtitle": "Pert 15-16",
        "code": [
            "class Node:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.next = None",
            "",
            "class CircularLL:",
            "    def __init__(self):",
            "        self.head = None",
            "",
            "    def insert_akhir(self, data):",
            "        new = Node(data)",
            "        if not self.head:",
            "            self.head = new",
            "            new.next = self.head",
            "            return",
            "        ptr = self.head",
            "        while ptr.next != self.head:",
            "            ptr = ptr.next",
            "        ptr.next = new",
            "        new.next = self.head",
            "        print('Insert:', data)",
            "",
            "    def tampil(self):",
            "        ptr = self.head",
            "        hasil = []",
            "        while True:",
            "            hasil.append(str(ptr.data))",
            "            ptr = ptr.next",
            "            if ptr == self.head:",
            "                break",
            "        print('Circular traversal:', ' -> '.join(hasil),",
            "              '-> (kembali ke Head)')",
            "",
            "cll = CircularLL()",
            "cll.insert_akhir(10)",
            "cll.insert_akhir(20)",
            "cll.insert_akhir(30)",
            "cll.tampil()",
        ],
    },

    "images/pert15-16/demo_awal_2.png": {
        "title": "Demo Awal 2 - Double Linked List Insert",
        "subtitle": "Pert 15-16",
        "code": [
            "class Node:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.prev = None",
            "        self.next = None",
            "",
            "class DoubleLL:",
            "    def __init__(self):",
            "        self.head = None",
            "        self.tail = None",
            "",
            "    def insert_akhir(self, data):",
            "        new = Node(data)",
            "        if not self.head:",
            "            self.head = self.tail = new",
            "        else:",
            "            new.prev = self.tail",
            "            self.tail.next = new",
            "            self.tail = new",
            "        print('Insert akhir:', data)",
            "",
            "    def insert_depan(self, data):",
            "        new = Node(data)",
            "        new.next = self.head",
            "        if self.head:",
            "            self.head.prev = new",
            "        self.head = new",
            "        print('Insert depan:', data)",
            "",
            "    def tampil_maju(self):",
            "        ptr, result = self.head, []",
            "        while ptr:",
            "            result.append(str(ptr.data))",
            "            ptr = ptr.next",
            "        print('Maju: ', ' <-> '.join(result), '-> None')",
            "",
            "    def tampil_mundur(self):",
            "        ptr, result = self.tail, []",
            "        while ptr:",
            "            result.append(str(ptr.data))",
            "            ptr = ptr.prev",
            "        print('Mundur:', ' <-> '.join(result), '-> None')",
            "",
            "dll = DoubleLL()",
            "dll.insert_akhir(20)",
            "dll.insert_akhir(30)",
            "dll.insert_depan(10)",
            "dll.tampil_maju()",
            "dll.tampil_mundur()",
        ],
    },

    "images/pert15-16/demo_awal_3.png": {
        "title": "Demo Awal 3 - Double LL Delete",
        "subtitle": "Pert 15-16",
        "code": [
            "# Menggunakan class DoubleLL dari Demo Awal 2",
            "",
            "    def delete_head(self):",
            "        if not self.head:",
            "            return",
            "        print('Delete Head:', self.head.data)",
            "        if self.head == self.tail:",
            "            self.head = self.tail = None",
            "        else:",
            "            self.head = self.head.next",
            "            self.head.prev = None",
            "",
            "    def delete_tail(self):",
            "        if not self.tail:",
            "            return",
            "        print('Delete Tail:', self.tail.data)",
            "        if self.head == self.tail:",
            "            self.head = self.tail = None",
            "        else:",
            "            self.tail = self.tail.prev",
            "            self.tail.next = None",
            "",
            "    def tampil(self):",
            "        ptr, r = self.head, []",
            "        while ptr:",
            "            r.append(str(ptr.data))",
            "            ptr = ptr.next",
            "        print('List:', ' <-> '.join(r))",
            "",
            "# --- Test ---",
            "dll = DoubleLL()",
            "for v in [10, 20, 30, 40]:",
            "    dll.insert_akhir(v)",
            "print('List awal:', '10 <-> 20 <-> 30 <-> 40')",
            "dll.delete_head()",
            "dll.tampil()",
            "dll.delete_tail()",
            "dll.tampil()",
        ],
    },

    "images/pert15-16/demo_awal_4.png": {
        "title": "Demo Awal 4 - Double Circular LL",
        "subtitle": "Pert 15-16",
        "code": [
            "class Node:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.prev = None",
            "        self.next = None",
            "",
            "class DoubleCirLL:",
            "    def __init__(self):",
            "        self.head = None",
            "        self.tail = None",
            "",
            "    def append(self, data):",
            "        new = Node(data)",
            "        if not self.head:",
            "            self.head = self.tail = new",
            "            new.next = new.prev = new",
            "        else:",
            "            new.prev = self.tail",
            "            new.next = self.head",
            "            self.tail.next = new",
            "            self.head.prev = new",
            "            self.tail = new",
            "        print('Append:', data)",
            "",
            "    def tampil_maju(self):",
            "        ptr, r = self.head, []",
            "        while True:",
            "            r.append(ptr.data)",
            "            ptr = ptr.next",
            "            if ptr == self.head: break",
            "        print('Maju: ', ' <-> '.join(r),",
            "              '<-> (kembali A)')",
            "",
            "    def tampil_mundur(self):",
            "        ptr, r = self.tail, []",
            "        while True:",
            "            r.append(ptr.data)",
            "            ptr = ptr.prev",
            "            if ptr == self.tail: break",
            "        print('Mundur:', ' <-> '.join(r),",
            "              '<-> (kembali D)')",
            "",
            "dc = DoubleCirLL()",
            "for v in ['A','B','C','D']: dc.append(v)",
            "dc.tampil_maju()",
            "dc.tampil_mundur()",
        ],
    },

    # ── Pert 17-18 ──────────────────────────────────────────
    "images/pert17-18/demo_awal_1.png": {
        "title": "Demo Awal 1 - Stack LL Push & Pop",
        "subtitle": "Pert 17-18",
        "code": [
            "class Node:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.next = None",
            "",
            "class StackLL:",
            "    def __init__(self):",
            "        self.top = None",
            "",
            "    def push(self, data):",
            "        new = Node(data)",
            "        new.next = self.top",
            "        self.top = new",
            "        print('Push:', data)",
            "",
            "    def pop(self):",
            "        if not self.top:",
            "            return None",
            "        val = self.top.data",
            "        self.top = self.top.next",
            "        print('Pop:', val)",
            "        return val",
            "",
            "    def peek(self):",
            "        if self.top:",
            "            print('Top:', self.top.data)",
            "",
            "# --- Test ---",
            "s = StackLL()",
            "s.push('A')",
            "s.push('B')",
            "s.push('C')",
            "s.peek()",
            "s.pop()",
            "s.pop()",
            "s.peek()",
        ],
    },

    "images/pert17-18/demo_awal_2.png": {
        "title": "Demo Awal 2 - Stack LL Clear & isEmpty",
        "subtitle": "Pert 17-18",
        "code": [
            "# Lanjutan class StackLL dari Demo Awal 1",
            "",
            "    def isEmpty(self):",
            "        return self.top is None",
            "",
            "    def clear(self):",
            "        self.top = None",
            "        print('Clear stack...')",
            "",
            "    def tampil(self):",
            "        ptr, r = self.top, []",
            "        while ptr:",
            "            r.append(str(ptr.data))",
            "            ptr = ptr.next",
            "        print('Stack: [' + ' -> '.join(r) + ' -> None]')",
            "",
            "# --- Test ---",
            "s = StackLL()",
            "s.push('A')",
            "s.push('B')",
            "s.push('C')",
            "s.tampil()",
            "print('isEmpty:', s.isEmpty())",
            "s.clear()",
            "print('isEmpty:', s.isEmpty())",
            "result = s.pop()",
            "print('Pop dari stack kosong:', result)",
        ],
    },

    "images/pert17-18/demo_awal_3.png": {
        "title": "Demo Awal 3 - Queue LL Enqueue & Dequeue",
        "subtitle": "Pert 17-18",
        "code": [
            "class Node:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.next = None",
            "",
            "class QueueLL:",
            "    def __init__(self):",
            "        self.head = None",
            "        self.tail = None",
            "",
            "    def enqueue(self, data):",
            "        new = Node(data)",
            "        if not self.tail:",
            "            self.head = self.tail = new",
            "        else:",
            "            self.tail.next = new",
            "            self.tail = new",
            "        print('Enqueue:', data)",
            "",
            "    def dequeue(self):",
            "        if not self.head:",
            "            return None",
            "        val = self.head.data",
            "        self.head = self.head.next",
            "        if not self.head:",
            "            self.tail = None",
            "        print('Dequeue:', val)",
            "        return val",
            "",
            "    def front(self):",
            "        if self.head:",
            "            print('Front:', self.head.data)",
            "",
            "# --- Test ---",
            "q = QueueLL()",
            "q.enqueue('A')",
            "q.enqueue('B')",
            "q.enqueue('C')",
            "q.front()",
            "q.dequeue()",
            "q.dequeue()",
            "q.front()",
        ],
    },

    "images/pert17-18/demo_awal_4.png": {
        "title": "Demo Awal 4 - Queue DLL",
        "subtitle": "Pert 17-18",
        "code": [
            "class DNode:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.prev = None",
            "        self.next = None",
            "",
            "class QueueDLL:",
            "    def __init__(self):",
            "        self.head = None",
            "        self.tail = None",
            "",
            "    def enqueue(self, data):",
            "        new = DNode(data)",
            "        if not self.tail:",
            "            self.head = self.tail = new",
            "        else:",
            "            new.prev = self.tail",
            "            self.tail.next = new",
            "            self.tail = new",
            "",
            "    def dequeue(self):",
            "        if not self.head: return None",
            "        val = self.head.data",
            "        self.head = self.head.next",
            "        if self.head: self.head.prev = None",
            "        else: self.tail = None",
            "        print('Dequeue:', val)",
            "        return val",
            "",
            "    def tampil(self):",
            "        ptr, r = self.head, []",
            "        while ptr:",
            "            r.append(str(ptr.data))",
            "            ptr = ptr.next",
            "        print('Queue (Head->Tail):', ' <-> '.join(r))",
            "",
            "# --- Test ---",
            "q = QueueDLL()",
            "for v in ['A','B','C','D']: q.enqueue(v)",
            "q.tampil()",
            "q.dequeue()",
            "q.tampil()",
            "q.enqueue('E')",
            "q.tampil()",
        ],
    },

    # ── Pert 19-22a ─────────────────────────────────────────
    "images/pert19-22a/demo_awal_1.png": {
        "title": "Demo Awal 1 - Binary Tree Sederhana",
        "subtitle": "Pert 19-22a",
        "code": [
            "class TreeNode:",
            "    def __init__(self, data):",
            "        self.data = data",
            "        self.left  = None",
            "        self.right = None",
            "",
            "# Buat tree secara manual:",
            "#        5",
            "#       / \\",
            "#      3   7",
            "#     / \\",
            "#    1   4",
            "",
            "root        = TreeNode(5)",
            "root.left   = TreeNode(3)",
            "root.right  = TreeNode(7)",
            "root.left.left  = TreeNode(1)",
            "root.left.right = TreeNode(4)",
            "",
            "print('Root:', root.data)",
            "print('Anak kiri root:', root.left.data)",
            "print('Anak kanan root:', root.right.data)",
            "print('Anak kiri dari 3:', root.left.left.data)",
            "print('Anak kanan dari 3:', root.left.right.data)",
        ],
    },

    "images/pert19-22a/demo_awal_2.png": {
        "title": "Demo Awal 2 - BST Insert & In-order",
        "subtitle": "Pert 19-22a",
        "code": [
            "class BST:",
            "    def __init__(self):",
            "        self.root = None",
            "",
            "    def _insert(self, node, data):",
            "        if node is None:",
            "            return TreeNode(data)",
            "        if data < node.data:",
            "            node.left = self._insert(node.left, data)",
            "        elif data > node.data:",
            "            node.right = self._insert(node.right, data)",
            "        return node",
            "",
            "    def insert(self, data):",
            "        self.root = self._insert(self.root, data)",
            "",
            "    def _inorder(self, node, result):",
            "        if node:",
            "            self._inorder(node.left, result)",
            "            result.append(str(node.data))",
            "            self._inorder(node.right, result)",
            "",
            "    def inorder(self):",
            "        r = []",
            "        self._inorder(self.root, r)",
            "        print('In-order:', ' '.join(r))",
            "",
            "# --- Test ---",
            "bst = BST()",
            "values = [5, 3, 7, 1, 4]",
            "print('Insert:', ', '.join(map(str, values)))",
            "for v in values: bst.insert(v)",
            "bst.inorder()",
        ],
    },

    "images/pert19-22a/demo_awal_3.png": {
        "title": "Demo Awal 3 - Pre-order Traversal",
        "subtitle": "Pert 19-22a",
        "code": [
            "# Lanjutan class BST dari Demo Awal 2",
            "# Tambahkan method berikut:",
            "",
            "    def _preorder(self, node, result):",
            "        if node:",
            "            result.append(str(node.data))  # Visit",
            "            self._preorder(node.left, result)   # Left",
            "            self._preorder(node.right, result)  # Right",
            "",
            "    def preorder(self):",
            "        r = []",
            "        self._preorder(self.root, r)",
            "        print('Pre-order:', ' '.join(r))",
            "",
            "# --- Test ---",
            "# Insert: 5, 3, 7, 1, 4, 6, 8",
            "#        5",
            "#       / \\",
            "#      3   7",
            "#     / \\ / \\",
            "#    1  4 6   8",
            "",
            "bst = BST()",
            "for v in [5, 3, 7, 1, 4, 6, 8]:",
            "    bst.insert(v)",
            "bst.preorder()",
            "# Output: Pre-order: 5 3 1 4 7 6 8",
        ],
    },

    "images/pert19-22a/demo_awal_4.png": {
        "title": "Demo Awal 4 - Post-order Traversal",
        "subtitle": "Pert 19-22a",
        "code": [
            "# Lanjutan class BST dari Demo Awal 2",
            "# Tambahkan method berikut:",
            "",
            "    def _postorder(self, node, result):",
            "        if node:",
            "            self._postorder(node.left, result)   # Left",
            "            self._postorder(node.right, result)  # Right",
            "            result.append(str(node.data))  # Visit",
            "",
            "    def postorder(self):",
            "        r = []",
            "        self._postorder(self.root, r)",
            "        print('Post-order:', ' '.join(r))",
            "",
            "# --- Test ---",
            "# Tree sama dengan Demo Awal 3:",
            "#        5",
            "#       / \\",
            "#      3   7",
            "#     / \\ / \\",
            "#    1  4 6   8",
            "",
            "bst = BST()",
            "for v in [5, 3, 7, 1, 4, 6, 8]:",
            "    bst.insert(v)",
            "bst.postorder()",
            "# Output: Post-order: 1 4 3 6 8 7 5",
        ],
    },

    # ── Pert 19-22b ─────────────────────────────────────────
    "images/pert19-22b/demo_awal_1.png": {
        "title": "Demo Awal 1 - Hapus Leaf Node",
        "subtitle": "Pert 19-22b",
        "code": [
            "# Menghapus node leaf (tidak punya anak) dari BST",
            "",
            "class BST:",
            "    # ... (insert & inorder dari sebelumnya)",
            "",
            "    def delete(self, data):",
            "        self.root = self._delete(self.root, data)",
            "",
            "    def _delete(self, node, data):",
            "        if node is None:",
            "            return None",
            "        if data < node.data:",
            "            node.left = self._delete(node.left, data)",
            "        elif data > node.data:",
            "            node.right = self._delete(node.right, data)",
            "        else:",
            "            # Kasus 1: Leaf node (tidak punya anak)",
            "            if not node.left and not node.right:",
            "                return None",
            "            # ... (kasus lain ditangani di Demo Awal 2-4)",
            "        return node",
            "",
            "# --- Test ---",
            "bst = BST()",
            "for v in [5, 3, 7, 1, 4, 6, 8]:",
            "    bst.insert(v)",
            "bst.inorder()  # [1, 3, 4, 5, 6, 7, 8]",
            "print('Hapus 1 (leaf)')",
            "bst.delete(1)",
            "bst.inorder()  # [3, 4, 5, 6, 7, 8]",
        ],
    },

    "images/pert19-22b/demo_awal_2.png": {
        "title": "Demo Awal 2 - Hapus Node 1 Anak",
        "subtitle": "Pert 19-22b",
        "code": [
            "# Lanjutan _delete() - tambahkan Kasus 2:",
            "",
            "    def _delete(self, node, data):",
            "        if node is None:",
            "            return None",
            "        if data < node.data:",
            "            node.left = self._delete(node.left, data)",
            "        elif data > node.data:",
            "            node.right = self._delete(node.right, data)",
            "        else:",
            "            # Kasus 1: Leaf",
            "            if not node.left and not node.right:",
            "                return None",
            "            # Kasus 2: Satu anak",
            "            if not node.left:",
            "                return node.right   # ganti dg anak kanan",
            "            if not node.right:",
            "                return node.left    # ganti dg anak kiri",
            "            # Kasus 3: Dua anak (di Demo Awal 3 & 4)",
            "        return node",
            "",
            "# --- Test ---",
            "# Tree setelah hapus 1: [3, 4, 5, 6, 7, 8]",
            "# Node 6 hanya punya anak kanan (7)",
            "print('Hapus 6 (1 anak: 7)')",
            "bst.delete(6)",
            "bst.inorder()  # [3, 4, 5, 7, 8]",
        ],
    },

    "images/pert19-22b/demo_awal_3.png": {
        "title": "Demo Awal 3 - Delete by Copying",
        "subtitle": "Pert 19-22b",
        "code": [
            "# Delete by Copying: ganti dgn Inorder Successor",
            "",
            "    def _min_node(self, node):",
            "        while node.left:",
            "            node = node.left",
            "        return node",
            "",
            "    def _delete(self, node, data):",
            "        if node is None: return None",
            "        if data < node.data:",
            "            node.left = self._delete(node.left, data)",
            "        elif data > node.data:",
            "            node.right = self._delete(node.right, data)",
            "        else:",
            "            if not node.left and not node.right:",
            "                return None",
            "            if not node.left: return node.right",
            "            if not node.right: return node.left",
            "            # Kasus 3: 2 anak - Delete by Copying",
            "            successor = self._min_node(node.right)",
            "            print('Inorder successor dari',",
            "                  data, 'adalah', successor.data)",
            "            node.data = successor.data   # copy nilai",
            "            node.right = self._delete(  # hapus successor",
            "                node.right, successor.data)",
            "        return node",
            "",
            "# --- Test ---",
            "bst = BST()",
            "for v in [5, 3, 7, 1, 4, 6, 8]: bst.insert(v)",
            "print('Sebelum hapus 5:', end=' '); bst.inorder()",
            "print('Hapus 5 (delete by copying)')",
            "bst.delete(5)",
            "print('Sesudah:', end=' '); bst.inorder()",
        ],
    },

    "images/pert19-22b/demo_awal_4.png": {
        "title": "Demo Awal 4 - Delete by Merging",
        "subtitle": "Pert 19-22b",
        "code": [
            "# Delete by Merging: subtree kanan naik,",
            "# subtree kiri jadi anak terkiri subtree kanan",
            "",
            "    def _delete_merge(self, node, data):",
            "        if node is None: return None",
            "        if data < node.data:",
            "            node.left = self._delete_merge(",
            "                node.left, data)",
            "        elif data > node.data:",
            "            node.right = self._delete_merge(",
            "                node.right, data)",
            "        else:",
            "            if not node.left: return node.right",
            "            if not node.right: return node.left",
            "            # Merge: cari terkiri di subtree kanan",
            "            leftmost = node.right",
            "            while leftmost.left:",
            "                leftmost = leftmost.left",
            "            # Pasang subtree kiri ke terkiri",
            "            leftmost.left = node.left",
            "            print('Merge: subtree kanan naik,",
            "                  'subtree kiri jadi anak terkiri')",
            "            return node.right",
            "        return node",
            "",
            "    def delete_merge(self, data):",
            "        self.root = self._delete_merge(self.root, data)",
            "",
            "# --- Test ---",
            "bst = BST()",
            "for v in [5, 3, 7, 1, 4, 6, 8]: bst.insert(v)",
            "bst.delete_merge(5)",
            "bst.inorder()  # [1, 3, 4, 6, 7, 8]",
        ],
    },

    # ── Pert 23-24 ──────────────────────────────────────────
    "images/pert23-24/demo_awal_1.png": {
        "title": "Demo Awal 1 - Adjacency Matrix",
        "subtitle": "Pert 23-24",
        "code": [
            "# Directed Graph dengan 4 verteks",
            "# Edge: 1->2, 1->4, 2->3, 2->4, 4->2, 4->3",
            "",
            "n = 4",
            "matrix = [[0] * (n+1) for _ in range(n+1)]",
            "",
            "def add_edge(u, v):",
            "    matrix[u][v] = 1",
            "",
            "add_edge(1, 2)",
            "add_edge(1, 4)",
            "add_edge(2, 3)",
            "add_edge(2, 4)",
            "add_edge(4, 2)",
            "add_edge(4, 3)",
            "",
            "# Tampilkan adjacency matrix",
            "print('Adjacency Matrix (4 verteks):')",
            "header = '   ' + ''.join(f'[{i}]' for i in range(1, n+1))",
            "print(header)",
            "for i in range(1, n+1):",
            "    row = f'[{i}] '",
            "    for j in range(1, n+1):",
            "        row += f'{matrix[i][j]}  '",
            "    print(row)",
        ],
    },

    "images/pert23-24/demo_awal_2.png": {
        "title": "Demo Awal 2 - Adjacency List",
        "subtitle": "Pert 23-24",
        "code": [
            "# Directed Graph dengan 6 verteks",
            "# Edge: 1->2,3,4  2->4,5  3->6  4->3",
            "",
            "class Graph:",
            "    def __init__(self, n):",
            "        self.adj = {i: [] for i in range(1, n+1)}",
            "",
            "    def add_edge(self, u, v):",
            "        self.adj[u].append(v)",
            "",
            "    def tampil(self):",
            "        print('Adjacency List:')",
            "        for v, neighbors in self.adj.items():",
            "            print(f'  {v}: {neighbors}')",
            "",
            "g = Graph(6)",
            "g.add_edge(1, 2)",
            "g.add_edge(1, 3)",
            "g.add_edge(1, 4)",
            "g.add_edge(2, 4)",
            "g.add_edge(2, 5)",
            "g.add_edge(3, 6)",
            "g.add_edge(4, 3)",
            "g.tampil()",
        ],
    },

    "images/pert23-24/demo_awal_3.png": {
        "title": "Demo Awal 3 - DFS (Depth-First Search)",
        "subtitle": "Pert 23-24",
        "code": [
            "# Lanjutan class Graph dari Demo Awal 2",
            "",
            "    def dfs(self, start):",
            "        visited = set()",
            "        path    = []",
            "        self._dfs_rec(start, visited, path)",
            "        print('DFS dari verteks', start, end=': ')",
            "        print(' -> '.join(map(str, path)))",
            "",
            "    def _dfs_rec(self, v, visited, path):",
            "        visited.add(v)",
            "        path.append(v)",
            "        for neighbor in self.adj[v]:",
            "            if neighbor not in visited:",
            "                self._dfs_rec(neighbor, visited, path)",
            "",
            "# --- Test ---",
            "# Graph: 1->2->4->3->5",
            "g = Graph(5)",
            "g.add_edge(1, 2)",
            "g.add_edge(1, 3)",
            "g.add_edge(2, 4)",
            "g.add_edge(3, 4)",
            "g.add_edge(4, 5)",
            "g.dfs(1)",
            "# Output: DFS dari verteks 1: 1 -> 2 -> 4 -> 3 -> 5",
        ],
    },

    "images/pert23-24/demo_awal_4.png": {
        "title": "Demo Awal 4 - BFS (Breadth-First Search)",
        "subtitle": "Pert 23-24",
        "code": [
            "from collections import deque",
            "",
            "# Lanjutan class Graph dari Demo Awal 2",
            "",
            "    def bfs(self, start):",
            "        visited = set([start])",
            "        queue   = deque([start])",
            "        path    = []",
            "        while queue:",
            "            v = queue.popleft()",
            "            path.append(v)",
            "            for neighbor in self.adj[v]:",
            "                if neighbor not in visited:",
            "                    visited.add(neighbor)",
            "                    queue.append(neighbor)",
            "        print('BFS dari verteks', start, end=': ')",
            "        print(' -> '.join(map(str, path)))",
            "",
            "# --- Test ---",
            "# Graph: 1 terhubung ke 2,3 dst",
            "g = Graph(5)",
            "g.add_edge(1, 2)",
            "g.add_edge(1, 3)",
            "g.add_edge(2, 4)",
            "g.add_edge(3, 4)",
            "g.add_edge(4, 5)",
            "g.bfs(1)",
            "# Output: BFS dari verteks 1: 1 -> 2 -> 3 -> 4 -> 5",
        ],
    },

    # ── Pert 25-26 ──────────────────────────────────────────
    "images/pert25-26/demo_awal_1.png": {
        "title": "Demo Awal 1 - N-Ary Tree (Anak Pertama+Saudara)",
        "subtitle": "Pert 25-26",
        "code": [
            "class NNode:",
            "    def __init__(self, data):",
            "        self.data        = data",
            "        self.first_child = None   # anak pertama",
            "        self.next_sib    = None   # saudara kanan",
            "",
            "def add_child(parent, child):",
            "    if not parent.first_child:",
            "        parent.first_child = child",
            "    else:",
            "        sib = parent.first_child",
            "        while sib.next_sib:",
            "            sib = sib.next_sib",
            "        sib.next_sib = child",
            "",
            "def get_children(node):",
            "    children, ptr = [], node.first_child",
            "    while ptr:",
            "        children.append(ptr.data)",
            "        ptr = ptr.next_sib",
            "    return children",
            "",
            "# --- Test ---",
            "A = NNode('A'); B = NNode('B'); C = NNode('C')",
            "D = NNode('D'); E = NNode('E'); F = NNode('F')",
            "G = NNode('G')",
            "add_child(A, B); add_child(A, C); add_child(A, D)",
            "add_child(B, E); add_child(B, F)",
            "add_child(D, G)",
            "print('Tree: Root=A')",
            "print('  A memiliki anak:', get_children(A))",
            "print('  B memiliki anak:', get_children(B))",
            "print('  D memiliki anak:', get_children(D))",
        ],
    },

    "images/pert25-26/demo_awal_2.png": {
        "title": "Demo Awal 2 - N-Ary Array of Children",
        "subtitle": "Pert 25-26",
        "code": [
            "from collections import deque",
            "",
            "class NNode2:",
            "    def __init__(self, data):",
            "        self.data     = data",
            "        self.children = []   # array of children",
            "",
            "def preorder(node, result=[]):",
            "    if node:",
            "        result.append(node.data)",
            "        for child in node.children:",
            "            preorder(child, result)",
            "    return result",
            "",
            "def level_order(root):",
            "    if not root: return []",
            "    q, result = deque([root]), []",
            "    while q:",
            "        node = q.popleft()",
            "        result.append(node.data)",
            "        for child in node.children:",
            "            q.append(child)",
            "    return result",
            "",
            "# --- Test ---",
            "A = NNode2('A')",
            "B, C, D = NNode2('B'), NNode2('C'), NNode2('D')",
            "E, F, G = NNode2('E'), NNode2('F'), NNode2('G')",
            "A.children = [B, C, D]",
            "B.children = [E, F]",
            "D.children = [G]",
            "print('Pre-order:', ' '.join(preorder(A, [])))",
            "print('Level-order:', ' '.join(level_order(A)))",
        ],
    },

    "images/pert25-26/demo_awal_3.png": {
        "title": "Demo Awal 3 - B-Tree Search",
        "subtitle": "Pert 25-26",
        "code": [
            "# B-Tree Sederhana - Pencarian",
            "# t = minimum degree (order = 2t)",
            "",
            "class BNode:",
            "    def __init__(self):",
            "        self.keys     = []",
            "        self.children = []",
            "        self.is_leaf  = True",
            "",
            "class BTree:",
            "    def __init__(self, t=3):",
            "        self.root = BNode()",
            "        self.t    = t  # min degree (order=5 -> t=3)",
            "",
            "    def search(self, k, node=None):",
            "        node = node or self.root",
            "        i = 0",
            "        while i < len(node.keys) and k > node.keys[i]:",
            "            i += 1",
            "        if i < len(node.keys) and k == node.keys[i]:",
            "            return True, node",
            "        if node.is_leaf:",
            "            return False, None",
            "        return self.search(k, node.children[i])",
            "",
            "    def insert_simple(self, k):",
            "        # Insert langsung ke root (simplified demo)",
            "        self.root.keys.append(k)",
            "        self.root.keys.sort()",
            "",
            "# --- Test ---",
            "bt = BTree(t=3)",
            "for v in [6, 12, 20, 30, 2, 3, 4, 5]:",
            "    bt.insert_simple(v)",
            "print('Insert: 6, 12, 20, 30, 2, 3, 4, 5')",
            "found, _ = bt.search(4)",
            "print('Search 4:', 'ditemukan' if found else 'tidak')",
            "found, _ = bt.search(11)",
            "print('Search 11:', 'ditemukan' if found else 'tidak ditemukan')",
        ],
    },

    "images/pert25-26/demo_awal_4.png": {
        "title": "Demo Awal 4 - B-Tree Split",
        "subtitle": "Pert 25-26",
        "code": [
            "# B-Tree Insert dengan Split",
            "# Ketika leaf penuh (max 2t-1 keys), lakukan split",
            "",
            "def split_child(parent, i, child, t):",
            "    \"\"\"Split child[i] dari parent, t = min degree.\"\"\"",
            "    new_node = BNode()",
            "    new_node.is_leaf = child.is_leaf",
            "    # Pindahkan setengah kanan ke new_node",
            "    new_node.keys = child.keys[t:]",
            "    child.keys    = child.keys[:t-1]",
            "    # Promosikan median ke parent",
            "    median = child.keys[t-1] if len(child.keys)>=t else \\",
            "             new_node.keys[0]",
            "    parent.keys.insert(i, median)",
            "    parent.children.insert(i+1, new_node)",
            "    parent.is_leaf = False",
            "    print(f'Split -> [{child.keys}] | {median}',",
            "          f'| [{new_node.keys}]')",
            "    print(f'Promosikan {median} ke parent')",
            "",
            "# --- Demo Split ---",
            "# Leaf penuh dengan [2, 3, 4, 5] (t=3, max=4 keys)",
            "# Insert 6 -> overflow -> split",
            "leaf   = BNode()",
            "leaf.keys = [2, 3, 4, 5, 6]  # sudah termasuk 6",
            "parent = BNode()",
            "parent.keys = [12, 20]",
            "parent.children = [leaf]",
            "parent.is_leaf = False",
            "print('Insert 6 ke leaf penuh [2|3|4|5]:')",
            "split_child(parent, 0, leaf, t=3)",
            "print('Root baru:', parent.keys)",
        ],
    },
}


# ============================================================
# JALANKAN GENERATOR
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print("Generating demo_awal images...\n")
    for rel_path, info in images_data.items():
        full_path = os.path.join(BASE_DIR, rel_path)
        make_image(
            title=info["title"],
            subtitle=info["subtitle"],
            code_lines=info["code"],
            output_path=full_path,
        )
    print(f"\nSelesai! {len(images_data)} gambar berhasil dibuat.")
