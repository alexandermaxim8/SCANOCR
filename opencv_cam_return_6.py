import cv2
import numpy as np
from PIL import Image
from PIL import Image, ImageEnhance, ImageFilter

class Scanner:
    def __init__(self, mode= 'gambar', path_image='test2.jpg'):
        # pilih_mode = 'kamera' agar webcam yang digunakan. 
        # ELSE, akan automatis menjadi frame gambar yang diimport dari lokal file 
        self.pilih_mode=mode
        self.path=path_image
        self.ix, self.iy, self.fx, self.fy, self.drawing = -1, -1, -1, -1, False
        self.simpan_frame=None # untuk capture gambar
        self.current_coordinates= None
        self.frame=None
        # Inisiasi Awal untuk tuning pada variabel trackbar 
        self.canny_lower=80
        self.canny_upper=150
        self.dilation_iter=1
        self.erode_iter=1
        self.sudut=0
        self.brightness_awal = 255
        self.contrast_awal = 127 
        self.hue=10
        self.saturation=10
        self.iterasi=0
        self.trackbar_berubah=False
        ##########################################################
      
    def inisiasi_awal(self):
        if self.pilih_mode == 'kamera':
            # pada Videocapture, webcam dari laptop = 0
            # kalo webcam eksternal = 1 atau 2 atau 3, dst....
            # kalo -1 berarti kamera paling awal bakalan dibuka
            i =0
            while True:
                try:
                    self.cap=cv2.VideoCapture(i)
                    break
                except:
                    i +=1
                    if i >10:
                        break
            # mendapatkan serta mengatur tinggi dan lebar frame kamera
            self.tinggi, self.lebar = int(self.cap.get(4)), int(self.cap.get(3))
            self.lebar = int(self.lebar / 2)
            self.tinggi = int(self.tinggi /2)
        else:
            #image_path berasal dari line paling bawah di kodingan ini,yakni alamat gambar dari Scanner('test2.jpg')
            self.cap = cv2.imread(self.path, cv2.IMREAD_COLOR)
            # mendapatkan serta mengatur tinggi dan lebar frame fotto
            self.tinggi, self.lebar, self.channels = self.cap.shape
            self.lebar = int(self.lebar / 2)
            self.tinggi = int(self.tinggi /2)
        return self.cap

    def trackbar_contour(self):
        cv2.namedWindow('ukuran')
        cv2.moveWindow('ukuran',0,300+60)
        cv2.resizeWindow('ukuran',300, 200)
        cv2.createTrackbar('x_kontur', 'ukuran', self.x_kontur, self.lebar-10, self.track_x_kontur)
        cv2.createTrackbar('y_kontur', 'ukuran', self.y_kontur, self.tinggi-10, self.track_y_kontur)
        cv2.createTrackbar('w_kontur', 'ukuran', self.w_kontur, self.lebar-10, self.track_w_kontur)
        cv2.createTrackbar('h_kontur', 'ukuran', self.h_kontur, self.tinggi-10, self.track_h_kontur)
        cv2.createTrackbar('sudut', 'ukuran',    self.sudut, 360, self.track_sudut)
        ###########################################################################################

    # Function track berfungsi untuk passsing nilai dari pergeseran trackbar 
    # variabel "val" adalah pergeseran trackbar yang nilainya dikirim ke setiap "self.variabel"
    def track_canny_lower(self,val):
        self.canny_lower = val

    def track_canny_upper(self, val):
        self.canny_upper = val

    def track_dilation_iter(self, val):
        self.dilation_iter = val

    def track_erode_iter(self,val):
        self.erode_iter = val

    def track_brightness(self, val):
        self.brightness_awal = val

    def track_contrast(self, val):
        self.contrast_awal = val

    def track_hue(self,val):
        self.hue=val

    def track_saturation(self,val):
        self.saturation=val

    def track_x_kontur(self,val):
        self.x_kontur = val
        
    def track_y_kontur(self, val):
        self.y_kontur = val

    def track_w_kontur(self,val):
        self.w_kontur = val

    def track_h_kontur(self,val):
        self.h_kontur = val

    def track_sudut(self, val):
        self.sudut = val
    #############################################################################################
    
    def trackbar_parameter(self):
        cv2.namedWindow('parameter')
        cv2.moveWindow('parameter',0,0)
        cv2.resizeWindow('parameter',700, 300)
        cv2.createTrackbar('Contrast', 'parameter', 127, 2 * 127, self.track_contrast)
        cv2.createTrackbar('Brightness', 'parameter', 255, 2 * 255, self.track_brightness)
        cv2.createTrackbar('Hue','parameter',self.hue, 20, self.track_hue)
        cv2.createTrackbar('Saturation','parameter',self.saturation, 20, self.track_saturation)
        cv2.createTrackbar('sudut', 'parameter',    self.sudut, 360, self.track_sudut)
    
    def camera_atau_gambar(self):
        if self.pilih_mode == 'kamera':
            ret, self.frame = self.cap.read()
        # ELSE: Untuk gambar dari file lokal
        else:
            self.frame=self.cap
            ret =True
        self.frame = cv2.resize(self.frame, (int(self.lebar), int(self.tinggi)))
        return ret, self.frame

    #Function untuk mengatur Hue dan saturation
    def hsv_tuning(self):
        ret,input=self.camera_atau_gambar()
        frameHSV = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
        frameHSV[:, :, 0] =  frameHSV[:, :, 0]*(self.hue/10)
        frameHSV[:, :, 1] =  frameHSV[:, :, 1]* (self.saturation/10)
        self.tuning=cv2.cvtColor(frameHSV, cv2.COLOR_HSV2BGR)
        return self.tuning

    # Function untuk mengatur brightness dan contrast
    def bright_contrast_tuning(self):
        input=self.hsv_tuning()

        brightness = int((self.brightness_awal - 0) * (255 - (-255)) / (510 - 0) + (-255))
        contrast = int((self.contrast_awal - 0) * (127 - (-127)) / (254 - 0) + (-127))

        if brightness != 0:
            if brightness > 0:
                shadow = brightness
                max = 255
            else:
                shadow = 0
                max = 255 + brightness
            al_pha = (max - shadow) / 255
            ga_mma = shadow
            cal = cv2.addWeighted(input, al_pha, input, 0, ga_mma)
        else:
            cal = input
        if contrast != 0:
            Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
            Gamma = 127 * (1 - Alpha)
            cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)
        
        self.tuning=cal
        return self.tuning

    # Function untuk mendeteksi bagian tepi dari sebuah objek 
    # Untuk sementara gak ada ngaruhnya di frame manapun karena ujung2nya diganti dengan trackbar
    def preprocessing(self):
        '''
        cv2.Canny mendeteksi lebih kompleks dan lebih memakan komputasi dibandingkan cv2.threshold.
        cv2.GaussianBlur agar gambar lebih blur sehingga jumlah kontur makin hemat tapi hasil deteksi lebih jelek
        Pada cv2.threshold, if pixel > thresh, then pixel = maxval, else: pixel = zero (0)
        '''
        input=self.bright_contrast_tuning()
        gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 1) 
        #thresh = cv2.adaptiveThreshold(gray, self.canny_lower, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #ret, thresh =cv2.threshold(src=gray, thresh=self.canny_lower, maxval=self.canny_upper, type=cv2.THRESH_BINARY)
        canny = cv2.Canny(blur, self.canny_lower, self.canny_upper)
        #_, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        kernel = np.ones((5, 5))
        dilation = cv2.dilate(canny, kernel, iterations=self.dilation_iter)
        erode = cv2.erode(dilation, kernel, iterations=self.erode_iter)

        self.preprocessing_frame = erode
        return self.preprocessing_frame
    
    #Function untuk memperlihat kontur kotak merah 
    def contour(self, frame_dari_main=None):
        '''
        cv2.RETR_EXTERNAL = hanya mendeteksi bagian luar/tepi ; cv2.RETR_LIST= dideteksi keselurahan quantitas kontur
        approximae the contur: cv2.CHAIN_APPROX_NONE = keseluruhan garis akan terdeteksi  ; 
        cv2.CHAIN_APPROX_SIMPLE = compress (hanya titik awal dan titik akhir dari garis yang dideteksi)
        ''' 
        if frame_dari_main is None:
            input= self.preprocessing()
            self.contour_frame=self.bright_contrast_tuning()
        else:
            input = frame_dari_main
            input=cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
            self.contour_frame=frame_dari_main

        if self.pilih_mode =='kamera':
            contours,_ = cv2.findContours(input, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            if len(contours)>0:
                contour_terbesar=max(contours, key=cv2.contourArea)
                self.x_kontur, self.y_kontur, self.w_kontur, self.h_kontur= cv2.boundingRect(contour_terbesar)
                # error handling supaya tidak negatif hasilnya
                self.w_kontur = min(self.w_kontur,max(0, self.lebar-self.x_kontur) )
                self.h_kontur = min(self.h_kontur,max(0, self.tinggi-self.y_kontur) )
                self.koordinat_kontur= [self.x_kontur, self.y_kontur, self.w_kontur, self.h_kontur]
            else:
                self.koordinat_kontur=[0,0,0,0]
                return self.koordinat_kontur, self.contour_frame
        # gambar
        else:
            if self.ix != -1 and self.iy != -1 and self.fx != -1 and self.fy != -1:
                self.koordinat_kontur=  [self.ix, self.iy, abs(self.fx-self.ix), abs(self.fy-self.iy)]
                if self.ix >self.fx:
                    self.koordinat_kontur[0]=max(0, self.fx)
                if self.iy >self.fy:
                    self.koordinat_kontur[1]=max(0, self.fy)
                self.x_kontur, self.y_kontur, self.w_kontur, self.h_kontur= self.koordinat_kontur
            # bukan kamera maupun gambar
            else:
                self.koordinat_kontur=[0,0,0,0]
                self.x_kontur, self.y_kontur, self.w_kontur, self.h_kontur =0,0,0,0
                return self.koordinat_kontur, self.contour_frame
        # gambar contur
        x1, y1, x2, y2 = self.x_kontur, self.y_kontur, self.x_kontur + self.w_kontur, self.y_kontur + self.h_kontur 
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=self.sudut, scale=1.0)
        koor = np.array([(x1, y1), (x1, y2), (x2, y2), (x2, y1)], dtype=np.float32)
        koor = cv2.transform(koor.reshape(-1, 1, 2), rotation_matrix)
        koor = koor.squeeze()
        koor = koor.astype(np.int32)
        rotated_rect = cv2.minAreaRect(koor) 
        box = cv2.boxPoints(rotated_rect)     
        box = np.int0(box) 
        cv2.drawContours(self.contour_frame, [box], 0, (0, 0, 250), 2)

        return self.koordinat_kontur, self.contour_frame
        
  

    # Function untuk translasi gambar
    def translasi(self, frame_dari_main=None):
        if frame_dari_main is None:
            input=self.bright_contrast_tuning()
        else:
            input=frame_dari_main
        try:
            x,y,w,h =self.x_kontur,self.y_kontur,self.w_kontur,self.h_kontur
        except:
            x,y,w,h =0,0,self.lebar,self.tinggi
        if w > 0 and h > 0:
            # Mengambil potongan gambar dari koordinat kontur
            self.translasi_frame = input[y:y + h, x:x + w]
            return self.translasi_frame
        else:
            self.translasi_frame=input
            return self.translasi_frame

    # Function untuk merotasi gambar
    def rotasi(self, frame_dari_main=None):
        input=self.translasi()
        pil_image = Image.fromarray(cv2.cvtColor(input, cv2.COLOR_BGR2RGB))
        rotated_pil_image=pil_image.rotate(self.sudut,resample=Image.BICUBIC , expand=True) 
        self.rotasi_frame= cv2.cvtColor(np.array(rotated_pil_image), cv2.COLOR_RGB2BGR)
        return self.rotasi_frame

    # FUnction agar gambar diperbesar hingga memenuhi satu frame, 
    # namun tidak di strecth karena aspect ratio dipertahankan,
    # sehingga bagian  pinggiran yang kosong diisi black pixel
    def resize_full(self, frame_dari_main=None):
        # aspek ratio
        cropped=self.rotasi()
        ratio = cropped.shape[1] / cropped.shape[0]  # shape[1]= lebar; shape[0] = tinggi
        
        # mengatur aspek ratio agar gambar tidak terkena stretch
        if self.lebar / self.tinggi > ratio:
            lebar_2 = int(self.tinggi * ratio)
            tinggi_2 = self.tinggi
        else:
            lebar_2 = self.lebar
            tinggi_2 = int(self.lebar / ratio)
        cropped = cv2.resize(cropped, dsize=(lebar_2, tinggi_2))

        # supaya gambar berada ditengah
        y_mask = self.frame.shape[0] // 2
        x_mask = self.frame.shape[1] // 2

        y_start = y_mask - cropped.shape[0] // 2
        y_end = y_start + cropped.shape[0]

        x_start = x_mask - cropped.shape[1] // 2
        x_end = x_start + cropped.shape[1]

        # Memberikan blank (hitam) frame di bagian tepi
        masking = np.zeros(self.frame.shape, dtype=np.uint8)
        masking[y_start:y_end, x_start:x_end, :] = cropped

        # menghilangkan blackbar di bagian tepi
        gray = cv2.cvtColor(masking,cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
        contours,_= cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
        cnt = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(cnt)
        masking=masking[y:y+h,x:x+w]
        self.masking=masking
        return self.masking
    
    def kertas(self, frame_dari_main=None):
        if frame_dari_main is  None:
            input=self.simpan_frame
        else:
            input=frame_dari_main

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

        thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 199, 5)
        self.kertas_gray=thresh
        return self.kertas_gray
 


    def mouse_event_handler(self, event, x, y, flags, param):
        ix, iy, fx, fy, drawing = self.ix, self.iy, self.fx, self.fy, self.drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
            fx, fy = x, y
        
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                fx, fy = x, y
        
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            fx, fy = x, y
        self.ix, self.iy, self.fx, self.fy, self.drawing = ix, iy, fx, fy, drawing
        self.current_coordinates=(self.ix, self.iy)
    
    def mouse(self):
        cv2.namedWindow('kontur')
        cv2.setMouseCallback('kontur', self.mouse_event_handler)
    

    def run(self):
        # While True agar Video/gambar tetap berjalan trus dan melakukan update parameter secara liveq
          # TRACKBAR 
        # trackbar mengatur contrast, brightness, hue , saturation
        '''
        cv2.namedWindow('parameter')
        cv2.moveWindow('parameter',0,0)
        cv2.resizeWindow('parameter',300, 150)
        cv2.createTrackbar('Contrast', 'parameter', 127, 2 * 127, self.track_contrast)
        cv2.createTrackbar('Brightness', 'parameter', 255, 2 * 255, self.track_brightness)
        cv2.createTrackbar('Hue','parameter',self.hue, 20, self.track_hue)
        cv2.createTrackbar('Saturation','parameter',self.saturation, 20, self.track_saturation)
        #############################################################################
        '''
        #trackbar mengatur frame hitam-putih (canny_lower, canny_upper, dilation, erode)
        cv2.namedWindow('preprocessing')
        cv2.moveWindow('preprocessing', 0,150+30)
        cv2.resizeWindow('preprocessing',300, 150)
        cv2.createTrackbar('canny_lower', 'preprocessing', self.canny_lower, 300, self.track_canny_lower)
        cv2.createTrackbar('canny_upper', 'preprocessing', self.canny_upper, 300, self.track_canny_upper)
        cv2.createTrackbar('dilation', 'preprocessing', self.dilation_iter, 10,   self.track_dilation_iter)
        cv2.createTrackbar('erode', 'preprocessing',   self.erode_iter, 10,       self.track_erode_iter)
        ###########################################################################################
        '''
        # Mengatur Lokasi Tiap frame yang ditampilkan pada While True
        # hasil_tuning
        cv2.namedWindow("hasil_tuning")
        cv2.moveWindow("hasil_tuning", 300,0)
        # preprocessing (frame yang hitam-putih)
        cv2.namedWindow("preprocessing_frame")
        cv2.moveWindow("preprocessing_frame",300+self.lebar,0)
        # frame yang ada kotak merah (kontur)
        cv2.namedWindow("kontur")
        cv2.moveWindow("kontur",300+self.lebar*2,0)
        # frame yang berasal dari translasi, rotasi, dan resize gambar
        cv2.namedWindow("resized_full")
        cv2.moveWindow("resized_full",300+self.lebar*2,self.tinggi+30)
        '''
        self.inisiasi_awal()
        self.mouse()
        self.trackbar_parameter()
        while True:
            # Untuk Webcam
            self.camera_atau_gambar()
            self.contour()
            akhir=self.resize_full()
            if self.simpan_frame is not None:
                self.kertas()

            ###################################################
            # menampilkan frame pada layar 
            #cv2.imshow("hasil_tuning", self.tuning)
            #cv2.imshow("preprocessing_frame", self.preprocessing_frame) 
            #cv2.putText(self.contour_frame, f'Cursor: {self.current_coordinates}', (1, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            #cv2.imshow("pre", self.preprocessing_frame)
            cv2.imshow("kontur", self.contour_frame)
            cv2.imshow("resized_full", akhir)
            if self.simpan_frame is not None:
                cv2.imshow("screenshot_frame", self.simpan_frame)
                cv2.moveWindow("screenshot_frame",0,600-10)

            # tombol 's' untuk capture gambar
            # tombol 'r' untuk remove hasil capture gambar
            # tombol 'q' atau tombol 'esc'==27 untuk quit program
            tombol = cv2.waitKey(1)
            if (tombol == ord("s")):
                self.simpan_frame= akhir
                # Bila ingin save gambar, uncomment line di bawah ini
                #cv2.imwrite("saved_image.png", self.simpan_frame)
                print("berhasil_capture")

            elif(tombol==ord('r')):
                self.simpan_frame=None
                cv2.destroyWindow("screenshot_frame")

            elif (tombol == ord('q')) or (tombol == 27):
                break

        cv2.destroyAllWindows()

#  Scanner('test2.jpg')  kalau mau ganti  gambar yang dipilih disini yak
if __name__ == "__main__":
    image_processor = Scanner()
    image_processor.run()
