import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from random import randint

class RideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام النقل الذكي")
        self.root.geometry("800x700")
        
        # بيانات التطبيق
        self.current_user = None
        self.rides = []
        self.drivers = []
        self.bookings = []
        
        # واجهة تسجيل الدخول
        self.create_login_screen()
    
    def create_login_screen(self):
        """واجهة تسجيل الدخول"""
        self.clear_screen()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        
        title = tk.Label(frame, text="تسجيل الدخول", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        
        # نوع المستخدم
        user_type_label = tk.Label(frame, text="نوع المستخدم:")
        user_type_label.pack()
        
        self.user_type = ttk.Combobox(frame, values=["راكب", "سائق"], state="readonly")
        self.user_type.pack(pady=5)
        
        # اسم المستخدم
        username_label = tk.Label(frame, text="اسم المستخدم:")
        username_label.pack()
        
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack(pady=5)
        
        # كلمة المرور
        password_label = tk.Label(frame, text="كلمة المرور:")
        password_label.pack()
        
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack(pady=5)
        
        # زر الدخول
        login_btn = tk.Button(
            frame,
            text="دخول",
            command=self.login,
            width=15,
            font=("Arial", 12)
        )
        login_btn.pack(pady=20)
        
        # تسجيل جديد
        register_btn = tk.Button(
            frame,
            text="تسجيل جديد",
            command=self.show_registration,
            width=15,
            font=("Arial", 10)
        )
        register_btn.pack(pady=5)
    
    def show_registration(self):
        """عرض واجهة التسجيل"""
        self.clear_screen()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        
        title = tk.Label(frame, text="تسجيل جديد", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        
        # نوع المستخدم
        user_type_label = tk.Label(frame, text="نوع المستخدم:")
        user_type_label.pack()
        
        self.reg_user_type = ttk.Combobox(frame, values=["راكب", "سائق"], state="readonly")
        self.reg_user_type.pack(pady=5)
        
        # الاسم الكامل
        name_label = tk.Label(frame, text="الاسم الكامل:")
        name_label.pack()
        
        self.reg_name_entry = tk.Entry(frame)
        self.reg_name_entry.pack(pady=5)
        
        # اسم المستخدم
        username_label = tk.Label(frame, text="اسم المستخدم:")
        username_label.pack()
        
        self.reg_username_entry = tk.Entry(frame)
        self.reg_username_entry.pack(pady=5)
        
        # كلمة المرور
        password_label = tk.Label(frame, text="كلمة المرور:")
        password_label.pack()
        
        self.reg_password_entry = tk.Entry(frame, show="*")
        self.reg_password_entry.pack(pady=5)
        
        # تأكيد كلمة المرور
        confirm_label = tk.Label(frame, text="تأكيد كلمة المرور:")
        confirm_label.pack()
        
        self.reg_confirm_entry = tk.Entry(frame, show="*")
        self.reg_confirm_entry.pack(pady=5)
        
        # معلومات إضافية للسائقين
        self.driver_frame = tk.Frame(frame)
        
        license_label = tk.Label(self.driver_frame, text="رقم رخصة القيادة:")
        license_label.pack()
        
        self.license_entry = tk.Entry(self.driver_frame)
        self.license_entry.pack(pady=5)
        
        # زر التسجيل
        register_btn = tk.Button(
            frame,
            text="تسجيل",
            command=self.register,
            width=15,
            font=("Arial", 12)
        )
        register_btn.pack(pady=20)
        
        # زر الرجوع
        back_btn = tk.Button(
            frame,
            text="رجوع",
            command=self.create_login_screen,
            width=15,
            font=("Arial", 10)
        )
        back_btn.pack(pady=5)
        
        # إظهار/إخفاء حقول السائق
        self.reg_user_type.bind("<<ComboboxSelected>>", self.toggle_driver_fields)
    
    def toggle_driver_fields(self, event):
        """إظهار أو إخفاء حقول السائق"""
        if self.reg_user_type.get() == "سائق":
            self.driver_frame.pack(pady=10)
        else:
            self.driver_frame.pack_forget()
    
    def register(self):
        """تسجيل مستخدم جديد"""
        # التحقق من البيانات
        if not all([
            self.reg_user_type.get(),
            self.reg_name_entry.get(),
            self.reg_username_entry.get(),
            self.reg_password_entry.get(),
            self.reg_confirm_entry.get()
        ]):
            messagebox.showerror("خطأ", "جميع الحقول مطلوبة")
            return
        
        if self.reg_password_entry.get() != self.reg_confirm_entry.get():
            messagebox.showerror("خطأ", "كلمة المرور غير متطابقة")
            return
        
        if self.reg_user_type.get() == "سائق" and not self.license_entry.get():
            messagebox.showerror("خطأ", "رقم رخصة القيادة مطلوب للسائقين")
            return
        
        # تخزين بيانات المستخدم
        user_data = {
            "type": self.reg_user_type.get(),
            "name": self.reg_name_entry.get(),
            "username": self.reg_username_entry.get(),
            "password": self.reg_password_entry.get(),
        }
        
        if user_data["type"] == "سائق":
            user_data["license"] = self.license_entry.get()
            self.drivers.append(user_data)
        
        messagebox.showinfo("نجاح", "تم التسجيل بنجاح")
        self.create_login_screen()
    
    def login(self):
        """تسجيل الدخول"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type.get()
        
        # هنا يجب التحقق من قاعدة البيانات
        # هذا مثال فقط للاختبار
        if username and password and user_type:
            self.current_user = {
                "type": user_type,
                "username": username
            }
            
            if user_type == "راكب":
                self.show_passenger_dashboard()
            else:
                self.show_driver_dashboard()
        else:
            messagebox.showerror("خطأ", "الرجاء إدخال جميع البيانات")
    
    def show_passenger_dashboard(self):
        """لوحة تحكم الراكب"""
        self.clear_screen()
        
        # شريط العنوان
        header = tk.Frame(self.root, bg="#333", padx=10, pady=10)
        header.pack(fill="x")
        
        welcome = tk.Label(
            header,
            text=f"مرحباً بك، {self.current_user['username']}",
            fg="white",
            bg="#333",
            font=("Arial", 12)
        )
        welcome.pack(side="right")
        
        logout_btn = tk.Button(
            header,
            text="تسجيل الخروج",
            command=self.create_login_screen,
            bg="#ff4444",
            fg="white"
        )
        logout_btn.pack(side="left")
        
        # تبويبات لوحة التحكم
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # تبويب حجز رحلة
        book_frame = tk.Frame(notebook)
        notebook.add(book_frame, text="حجز رحلة جديدة")
        
        # حقول حجز الرحلة
        tk.Label(book_frame, text="نقطة الانطلاق:").pack()
        self.start_point = ttk.Combobox(book_frame, values=["البياضة", "أقدال", "أنفيد", "الماجة", "أماس"])
        self.start_point.pack(pady=5)
        
        tk.Label(book_frame, text="نقطة الوصول:").pack()
        self.end_point = ttk.Combobox(book_frame, values=["البياضة", "أقدال", "أنفيد", "الماجة", "أماس"])
        self.end_point.pack(pady=5)
        
        tk.Label(book_frame, text="وقت الرحلة:").pack()
        self.ride_time = ttk.Combobox(book_frame, values=["الآن", "08:00", "12:00", "16:00", "20:00"])
        self.ride_time.pack(pady=5)
        
        book_btn = tk.Button(
            book_frame,
            text="بحث عن سائق",
            command=self.find_driver,
            width=15,
            font=("Arial", 12)
        )
        book_btn.pack(pady=20)
        
        # تبويب الرحلات الحالية
        current_frame = tk.Frame(notebook)
        notebook.add(current_frame, text="رحلاتي الحالية")
        
        self.current_rides_tree = ttk.Treeview(current_frame, columns=("id", "driver", "from", "to", "time", "status"))
        self.current_rides_tree.heading("#0", text="رقم الرحلة")
        self.current_rides_tree.heading("id", text="رقم الرحلة")
        self.current_rides_tree.heading("driver", text="السائق")
        self.current_rides_tree.heading("from", text="من")
        self.current_rides_tree.heading("to", text="إلى")
        self.current_rides_tree.heading("time", text="الوقت")
        self.current_rides_tree.heading("status", text="الحالة")
        
        self.current_rides_tree.column("#0", width=0, stretch=tk.NO)
        self.current_rides_tree.column("id", width=80)
        self.current_rides_tree.column("driver", width=120)
        self.current_rides_tree.column("from", width=100)
        self.current_rides_tree.column("to", width=100)
        self.current_rides_tree.column("time", width=80)
        self.current_rides_tree.column("status", width=100)
        
        self.current_rides_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        # تبويب سجل الرحلات
        history_frame = tk.Frame(notebook)
        notebook.add(history_frame, text="سجل الرحلات")
        
        self.history_tree = ttk.Treeview(history_frame, columns=("id", "driver", "from", "to", "time", "date"))
        self.history_tree.heading("#0", text="رقم الرحلة")
        self.history_tree.heading("id", text="رقم الرحلة")
        self.history_tree.heading("driver", text="السائق")
        self.history_tree.heading("from", text="من")
        self.history_tree.heading("to", text="إلى")
        self.history_tree.heading("time", text="الوقت")
        self.history_tree.heading("date", text="التاريخ")
        
        self.history_tree.column("#0", width=0, stretch=tk.NO)
        self.history_tree.column("id", width=80)
        self.history_tree.column("driver", width=120)
        self.history_tree.column("from", width=100)
        self.history_tree.column("to", width=100)
        self.history_tree.column("time", width=80)
        self.history_tree.column("date", width=100)
        
        self.history_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        # إضافة بيانات تجريبية
        self.add_sample_rides()
    
    def show_driver_dashboard(self):
        """لوحة تحكم السائق"""
        self.clear_screen()
        
        # شريط العنوان
        header = tk.Frame(self.root, bg="#333", padx=10, pady=10)
        header.pack(fill="x")
        
        welcome = tk.Label(
            header,
            text=f"مرحباً بك، السائق {self.current_user['username']}",
            fg="white",
            bg="#333",
            font=("Arial", 12)
        )
        welcome.pack(side="right")
        
        logout_btn = tk.Button(
            header,
            text="تسجيل الخروج",
            command=self.create_login_screen,
            bg="#ff4444",
            fg="white"
        )
        logout_btn.pack(side="left")
        
        # تبويبات لوحة التحكم
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # تبويب الرحلات المتاحة
        available_frame = tk.Frame(notebook)
        notebook.add(available_frame, text="الرحلات المتاحة")
        
        self.available_rides_tree = ttk.Treeview(available_frame, columns=("id", "passenger", "from", "to", "time"))
        self.available_rides_tree.heading("#0", text="رقم الرحلة")
        self.available_rides_tree.heading("id", text="رقم الرحلة")
        self.available_rides_tree.heading("passenger", text="الراكب")
        self.available_rides_tree.heading("from", text="من")
        self.available_rides_tree.heading("to", text="إلى")
        self.available_rides_tree.heading("time", text="الوقت")
        
        self.available_rides_tree.column("#0", width=0, stretch=tk.NO)
        self.available_rides_tree.column("id", width=80)
        self.available_rides_tree.column("passenger", width=120)
        self.available_rides_tree.column("from", width=100)
        self.available_rides_tree.column("to", width=100)
        self.available_rides_tree.column("time", width=80)
        
        self.available_rides_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        accept_btn = tk.Button(
            available_frame,
            text="قبول الرحلة",
            command=self.accept_ride,
            width=15,
            font=("Arial", 12)
        )
        accept_btn.pack(pady=10)
        
        # تبويب الرحلات الجارية
        active_frame = tk.Frame(notebook)
        notebook.add(active_frame, text="رحلاتي الجارية")
        
        self.active_rides_tree = ttk.Treeview(active_frame, columns=("id", "passenger", "from", "to", "time", "status"))
        self.active_rides_tree.heading("#0", text="رقم الرحلة")
        self.active_rides_tree.heading("id", text="رقم الرحلة")
        self.active_rides_tree.heading("passenger", text="الراكب")
        self.active_rides_tree.heading("from", text="من")
        self.active_rides_tree.heading("to", text="إلى")
        self.active_rides_tree.heading("time", text="الوقت")
        self.active_rides_tree.heading("status", text="الحالة")
        
        self.active_rides_tree.column("#0", width=0, stretch=tk.NO)
        self.active_rides_tree.column("id", width=80)
        self.active_rides_tree.column("passenger", width=120)
        self.active_rides_tree.column("from", width=100)
        self.active_rides_tree.column("to", width=100)
        self.active_rides_tree.column("time", width=80)
        self.active_rides_tree.column("status", width=100)
        
        self.active_rides_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        complete_btn = tk.Button(
            active_frame,
            text="إنهاء الرحلة",
            command=self.complete_ride,
            width=15,
            font=("Arial", 12)
        )
        complete_btn.pack(pady=10)
        
        # تبويب سجل الرحلات
        history_frame = tk.Frame(notebook)
        notebook.add(history_frame, text="سجل الرحلات")
        
        self.driver_history_tree = ttk.Treeview(history_frame, columns=("id", "passenger", "from", "to", "time", "date"))
        self.driver_history_tree.heading("#0", text="رقم الرحلة")
        self.driver_history_tree.heading("id", text="رقم الرحلة")
        self.driver_history_tree.heading("passenger", text="الراكب")
        self.driver_history_tree.heading("from", text="من")
        self.driver_history_tree.heading("to", text="إلى")
        self.driver_history_tree.heading("time", text="الوقت")
        self.driver_history_tree.heading("date", text="التاريخ")
        
        self.driver_history_tree.column("#0", width=0, stretch=tk.NO)
        self.driver_history_tree.column("id", width=80)
        self.driver_history_tree.column("passenger", width=120)
        self.driver_history_tree.column("from", width=100)
        self.driver_history_tree.column("to", width=100)
        self.driver_history_tree.column("time", width=80)
        self.driver_history_tree.column("date", width=100)
        
        self.driver_history_tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        # إضافة بيانات تجريبية
        self.add_sample_driver_data()
    
    def add_sample_rides(self):
        """إضافة بيانات تجريبية للراكب"""
        sample_rides = [
            ("R1001", "سائق 1", "البياضة", "أقدال", "08:00", "قيد الانتظار"),
            ("R1002", "سائق 2", "أنفيد", "الماجة", "12:00", "تم القبول"),
            ("R1003", "سائق 3", "أماس", "فيلاج الوتة", "16:00", "مكتملة")
        ]
        
        for ride in sample_rides:
            self.current_rides_tree.insert("", "end", values=ride)
        
        sample_history = [
            ("RH001", "سائق 1", "البياضة", "أقدال", "08:00", "2023-05-01"),
            ("RH002", "سائق 2", "أنفيد", "الماجة", "12:00", "2023-05-02"),
            ("RH003", "سائق 3", "أماس", "فيلاج الوتة", "16:00", "2023-05-03")
        ]
        
        for ride in sample_history:
            self.history_tree.insert("", "end", values=ride)
    
    def add_sample_driver_data(self):
        """إضافة بيانات تجريبية للسائق"""
        sample_available = [
            ("R2001", "راكب 1", "البياضة", "أقدال", "08:00"),
            ("R2002", "راكب 2", "أنفيد", "الماجة", "12:00"),
            ("R2003", "راكب 3", "أماس", "فيلاج الوتة", "16:00")
        ]
        
        for ride in sample_available:
            self.available_rides_tree.insert("", "end", values=ride)
        
        sample_active = [
            ("R2004", "راكب 4", "قصر الواتة", "البياضة", "09:00", "قيد التنفيذ"),
            ("R2005", "راكب 5", "الماجة", "أنفيد", "13:00", "قيد التنفيذ")
        ]
        
        for ride in sample_active:
            self.active_rides_tree.insert("", "end", values=ride)
        
        sample_history = [
            ("RH201", "راكب 1", "البياضة", "أقدال", "08:00", "2023-05-01"),
            ("RH202", "راكب 2", "أنفيد", "الماجة", "12:00", "2023-05-02"),
            ("RH203", "راكب 3", "أماس", "فيلاج الوتة", "16:00", "2023-05-03")
        ]
        
        for ride in sample_history:
            self.driver_history_tree.insert("", "end", values=ride)
    
    def find_driver(self):
        """البحث عن سائق"""
        start = self.start_point.get()
        end = self.end_point.get()
        time = self.ride_time.get()
        
        if not all([start, end, time]):
            messagebox.showerror("خطأ", "الرجاء إدخال جميع بيانات الرحلة")
            return
        
        # في التطبيق الحقيقي، هنا يتم البحث في قاعدة البيانات عن سائقين متاحين
        messagebox.showinfo("نجاح", f"تم طلب الرحلة من {start} إلى {end} في الساعة {time}\nسيتم إعلامك عند العثور على سائق")
    
    def accept_ride(self):
        """قبول رحلة من قبل السائق"""
        selected = self.available_rides_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "الرجاء اختيار رحلة")
            return
        
        ride = self.available_rides_tree.item(selected[0], "values")
        messagebox.showinfo("تم", f"تم قبول الرحلة {ride[0]}")
    
    def complete_ride(self):
        """إنهاء رحلة من قبل السائق"""
        selected = self.active_rides_tree.selection()
        if not selected:
            messagebox.showerror("خطأ", "الرجاء اختيار رحلة")
            return
        
        ride = self.active_rides_tree.item(selected[0], "values")
        messagebox.showinfo("تم", f"تم إنهاء الرحلة {ride[0]}")
    
    def clear_screen(self):
        """مسح جميع العناصر من الشاشة"""
        for widget in self.root.winfo_children():
            widget.destroy()

# تشغيل التطبيق
if __name__ == "__main__":
    root = tk.Tk()
    app = RideApp(root)
    root.mainloop()

    import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import random
from threading import Thread
import time

class RideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام النقل الذكي - تتبع السائق")
        self.root.geometry("800x600")
        
        # بيانات السائق الوهمية
        self.driver_location = (36.7538, 3.0588)  # إحداثيات الجزائر العاصمة
        self.driver_info = {
            "name": "محمد أحمد",
            "car": "تويوتا كامري 2020",
            "plate": "د ب 1234"
        }
        
        self.create_tracking_interface()
        self.simulate_driver_movement()
    
    def create_tracking_interface(self):
        """إنشاء واجهة تتبع السائق"""
        self.clear_screen()
        
        # عنوان الواجهة
        title = tk.Label(
            self.root,
            text="تتبع موقع السائق",
            font=("Arial", 18, "bold"),
            pady=20
        )
        title.pack()
        
        # إطار الخريطة (سيتم فتحها في المتصفح)
        map_frame = tk.Frame(self.root, padx=10, pady=10)
        map_frame.pack(fill="both", expand=True)
        
        # زر عرض الخريطة
        show_map_btn = tk.Button(
            map_frame,
            text="عرض الخريطة في المتصفح",
            command=self.show_map_in_browser,
            font=("Arial", 14),
            width=25,
            height=2
        )
        show_map_btn.pack(pady=20)
        
        # معلومات السائق
        info_frame = tk.Frame(self.root, padx=10, pady=10)
        info_frame.pack()
        
        tk.Label(
            info_frame,
            text="معلومات السائق:",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        tk.Label(
            info_frame,
            text=f"الاسم: {self.driver_info['name']}",
            font=("Arial", 12)
        ).grid(row=1, column=0, sticky="w")
        
        tk.Label(
            info_frame,
            text=f"المركبة: {self.driver_info['car']}",
            font=("Arial", 12)
        ).grid(row=2, column=0, sticky="w")
        
        tk.Label(
            info_frame,
            text=f"لوحة المركبة: {self.driver_info['plate']}",
            font=("Arial", 12)
        ).grid(row=3, column=0, sticky="w")
        
        # إحداثيات الموقع
        self.location_label = tk.Label(
            info_frame,
            text=f"الإحداثيات: {self.driver_location[0]:.4f}, {self.driver_location[1]:.4f}",
            font=("Arial", 12)
        )
        self.location_label.grid(row=4, column=0, sticky="w", pady=10)
        
        # زر التحديث
        refresh_btn = tk.Button(
            self.root,
            text="تحديث الموقع",
            command=self.update_driver_location,
            font=("Arial", 12),
            width=15
        )
        refresh_btn.pack(pady=10)
    
    def show_map_in_browser(self):
        """فتح الخريطة في متصفح الويب باستخدام Google Maps"""
        lat, lon = self.driver_location
        url = f"https://www.google.com/maps?q={lat},{lon}"
        webbrowser.open(url)
    
    def update_driver_location(self):
        """تحديث موقع السائق (وهمي للعرض)"""
        self.location_label.config(
            text=f"الإحداثيات: {self.driver_location[0]:.4f}, {self.driver_location[1]:.4f}"
        )
        messagebox.showinfo("تم", "تم تحديث موقع السائق")
    
    def simulate_driver_movement(self):
        """محاكاة حركة السائق (لأغراض العرض فقط)"""
        def movement_thread():
            while True:
                # تغيير الإحداثيات بشكل عشوائي
                new_lat = self.driver_location[0] + random.uniform(-0.01, 0.01)
                new_lon = self.driver_location[1] + random.uniform(-0.01, 0.01)
                self.driver_location = (new_lat, new_lon)
                time.sleep(5)
        
        Thread(target=movement_thread, daemon=True).start()
    
    def clear_screen(self):
        """مسح جميع العناصر من الشاشة"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RideApp(root)
    root.mainloop()

    import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import random
from threading import Thread
import time
import winsound  # لإصدار صوت الإشعار (لنظام ويندوز)

class RideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام النقل الذكي - التتبع المباشر")
        self.root.geometry("900x650")
        
        # بيانات الرحلة
        self.ride_started = False
        self.driver_location = (36.7538, 3.0588)
        self.driver_info = {
            "name": "محمد أحمد",
            "car": "تويوتا كامري 2020",
            "plate": "د ب 1234",
            "from": "البياضة",
            "to": "أقدال"
        }
        
        self.create_main_interface()
        self.simulate_driver_movement()
    
    def create_main_interface(self):
        """إنشاء الواجهة الرئيسية"""
        self.clear_screen()
        
        # قسم معلومات الرحلة
        ride_frame = tk.Frame(self.root, padx=10, pady=10, relief=tk.RIDGE, borderwidth=1)
        ride_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(
            ride_frame,
            text="تفاصيل الرحلة",
            font=("Arial", 14, "bold")
        ).pack(pady=5)
        
        # معلومات الرحلة
        tk.Label(
            ride_frame,
            text=f"من: {self.driver_info['from']}",
            font=("Arial", 12)
        ).pack(anchor="w")
        
        tk.Label(
            ride_frame,
            text=f"إلى: {self.driver_info['to']}",
            font=("Arial", 12)
        ).pack(anchor="w")
        
        # حالة الرحلة
        self.ride_status = tk.Label(
            ride_frame,
            text="حالة الرحلة: في انتظار انطلاق السائق" if not self.ride_started else "حالة الرحلة: السائق في طريقه إليك",
            font=("Arial", 12, "bold"),
            fg="red" if not self.ride_started else "green"
        )
        self.ride_status.pack(pady=10)
        
        # قسم تتبع السائق
        track_frame = tk.Frame(self.root, padx=10, pady=10)
        track_frame.pack(fill="both", expand=True)
        
        # زر عرض الخريطة
        map_btn = tk.Button(
            track_frame,
            text="فتح الخريطة للتتبع",
            command=self.show_map,
            font=("Arial", 12),
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white"
        )
        map_btn.grid(row=0, column=0, padx=10, pady=10)
        
        # زر محاكاة انطلاق السائق (للتجربة)
        start_btn = tk.Button(
            track_frame,
            text="محاكاة انطلاق السائق",
            command=self.simulate_driver_start,
            font=("Arial", 12),
            width=20,
            height=2,
            bg="#2196F3",
            fg="white"
        )
        start_btn.grid(row=0, column=1, padx=10, pady=10)
        
        # معلومات السائق
        driver_frame = tk.Frame(self.root, padx=10, pady=10, relief=tk.RIDGE, borderwidth=1)
        driver_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(
            driver_frame,
            text="معلومات السائق",
            font=("Arial", 14, "bold")
        ).pack(pady=5)
        
        tk.Label(
            driver_frame,
            text=f"الاسم: {self.driver_info['name']}",
            font=("Arial", 12)
        ).pack(anchor="w")
        
        tk.Label(
            driver_frame,
            text=f"المركبة: {self.driver_info['car']}",
            font=("Arial", 12)
        ).pack(anchor="w")
        
        tk.Label(
            driver_frame,
            text=f"رقم اللوحة: {self.driver_info['plate']}",
            font=("Arial", 12)
        ).pack(anchor="w")
        
        # إحداثيات الموقع
        self.location_label = tk.Label(
            driver_frame,
            text=f"الإحداثيات الحالية: {self.driver_location[0]:.6f}, {self.driver_location[1]:.6f}",
            font=("Arial", 11)
        )
        self.location_label.pack(pady=10)
    
    def show_map(self):
        """فتح الخريطة في المتصفح"""
        lat, lon = self.driver_location
        url = f"https://www.google.com/maps?q={lat},{lon}"
        webbrowser.open(url)
    
    def simulate_driver_start(self):
        """محاكاة انطلاق السائق (للتجربة)"""
        if not self.ride_started:
            self.ride_started = True
            self.show_notification(
                title="انطلاق السائق",
                message=f"انطلق السائق {self.driver_info['name']} من {self.driver_info['from']} إلى {self.driver_info['to']}"
            )
            self.update_ride_status()
    
    def show_notification(self, title, message):
        """عرض إشعار للمستخدم"""
        # عرض نافذة الرسالة
        messagebox.showinfo(title, message)
        
        # تشغيل صوت الإشعار (لنظام ويندوز)
        try:
            winsound.Beep(1000, 500)  # صوت نغمة
        except:
            pass  # إذا لم يكن نظام ويندوز
        
        # يمكن هنا إضافة إرسال إشعار للجوال إذا كان التطبيق متصلاً بخدمة ويب
    
    def update_ride_status(self):
        """تحديث حالة الرحلة"""
        if self.ride_started:
            self.ride_status.config(
                text="حالة الرحلة: السائق في طريقه إليك",
                fg="green"
            )
        else:
            self.ride_status.config(
                text="حالة الرحلة: في انتظار انطلاق السائق",
                fg="red"
            )
    
    def simulate_driver_movement(self):
        """محاكاة حركة السائق"""
        def movement_thread():
            while True:
                if self.ride_started:
                    # تغيير الإحداثيات بشكل عشوائي عند انطلاق السائق
                    new_lat = self.driver_location[0] + random.uniform(-0.01, 0.01)
                    new_lon = self.driver_location[1] + random.uniform(-0.01, 0.01)
                    self.driver_location = (new_lat, new_lon)
                    
                    # تحديث الواجهة
                    self.location_label.config(
                        text=f"الإحداثيات الحالية: {self.driver_location[0]:.6f}, {self.driver_location[1]:.6f}"
                    )      
                time.sleep(3)
        
        Thread(target=movement_thread, daemon=True).start()
    
    def clear_screen(self):
        """مسح جميع العناصر من الشاشة"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RideApp(root)
    root.mainloop()
