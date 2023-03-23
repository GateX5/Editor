from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QTextEdit, QLabel, QLineEdit, QButtonGroup,QListWidget,QLayout,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import ImageFilter
from PIL.ImageQt import ImageQt
from PIL import Image
from PIL.ImageFilter import(BLUR, CONTOUR,DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask) 
import os

app = QApplication([])
my_win = QWidget()
my_win.resize(700,500)
my_win.setWindowTitle("Editor")
bt = QPushButton("Folderi")
imazh = QLabel("imazhi")
x = QListWidget()

bt_1 = QPushButton('left')
bt_2 = QPushButton("right")
bt_3= QPushButton('mirror')
bt_4 = QPushButton("sharp")
bt_5 = QPushButton('B&W')


rresht = QHBoxLayout()
k1 = QVBoxLayout()
k2 = QVBoxLayout()
k1.addWidget(bt)
k1.addWidget(x)
k2.addWidget(imazh,95)


r_bt = QHBoxLayout()
r_bt.addWidget(bt_1)
r_bt.addWidget(bt_2)
r_bt.addWidget(bt_3)
r_bt.addWidget(bt_4)
r_bt.addWidget(bt_5)
k2.addLayout(r_bt)

rresht.addLayout(k1,20)
rresht.addLayout(k2,80)
my_win.setLayout(rresht)

direktor=""

def filtri (dokument,parashtes):
    result = []
    for emri in dokument:
        for ext in parashtes:
            if emri.endswith(ext):
                result.append(emri)
    return result

def zgjill():
    global direktor
    direktor = QFileDialog.getExistingDirectory()

def list():
    parashtes = [".jpg",".png",".bmp",".gif",".jpeg"]
    zgjill()
    emrat = filtri(os.listdir(direktor),parashtes)
    x.clear

    for emri in emrat:
        x.addItem(emri)

bt.clicked.connect(list)

class procesim_imazhi():
    def __init__(self):
        self.imazh = None
        self.dir = None
        self.emri = None
        self.ruaj_dir = 'modifikim'
    
    def ng_imazh (self,dir,emri):
        self.dir = dir
        self.emri = emri
        imazhi_path = os.path.join(dir, emri)
        self.imazh = Image.open(imazhi_path)

    def show_images(self,path):
        imazh.hide()
        piximazh = QPixmap(path)
        gj , i = imazh.width(), imazh.height()
        piximazh = piximazh.scaled (gj, i, Qt.KeepAspectRatio)
        imazh.setPixmap(piximazh)
        imazh.show()
    
    def bardh_e_zi(self):
        self.imazh = self.imazh.convert("L")
        self.ruaj_Imazhin()
        imazhi_path = os.path.join(self.dir ,self.ruaj_dir,self.emri)
        self.show_images(imazhi_path)

    def majtas(self):
        self.imazh = self.imazh.transpose(Image.ROTATE_90)
        self.ruaj_Imazhin()
        imazhi_path = os.path.join(self.dir ,self.ruaj_dir,self.emri)
        self.show_images(imazhi_path)

    def djathtas(self):
        self.imazh = self.imazh.transpose(Image.ROTATE_270)
        self.ruaj_Imazhin()
        imazhi_path = os.path.join(self.dir ,self.ruaj_dir,self.emri)
        self.show_images(imazhi_path)

    def flip(self):
        self.imazh = self.imazh.transpose(Image.FLIP_LEFT_RIGHT)
        self.ruaj_Imazhin()
        imazhi_path = os.path.join(self.dir ,self.ruaj_dir,self.emri)
        self.show_images(imazhi_path)

    def sharp(self):
        self.imazh = self.imazh.filter(SHARPEN)
        self.ruaj_Imazhin()
        imazhi_path = os.path.join(self.dir ,self.ruaj_dir,self.emri)
        self.show_images(imazhi_path)

    def ruaj_Imazhin(self):
        path = os.path.join(self.dir, self.ruaj_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        imazhi_path = os.path.join(path, self.emri)
        self.imazh.save(imazhi_path)
   
imazh_i_zgjellur = procesim_imazhi()

def open_imazh():
    if x.currentRow() >= 0:
        emri = x.currentItem().text()
        imazh_i_zgjellur.ng_imazh(direktor,emri)
        imazhi_path = os.path.join(imazh_i_zgjellur.dir, imazh_i_zgjellur.emri)
        imazh_i_zgjellur.show_images(imazhi_path)
x.currentRowChanged.connect(open_imazh)
bt_1.clicked.connect(imazh_i_zgjellur.majtas)
bt_2.clicked.connect(imazh_i_zgjellur.djathtas)
bt_3.clicked.connect(imazh_i_zgjellur.flip)
bt_4.clicked.connect(imazh_i_zgjellur.sharp)
bt_5.clicked.connect(imazh_i_zgjellur.bardh_e_zi)


my_win.show()
app.exec()