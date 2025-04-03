import flet as ft
import webbrowser
import random
from datetime import datetime

def main(page: ft.Page):
    page.title = "نظام النقل الذكي"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # بيانات التطبيق
    current_user = None
    rides = []
    drivers = [
        {"name": "محمد أحمد", "car": "تويوتا كامري", "license": "1234"},
        {"name": "أحمد علي", "car": "هيونداي النترا", "license": "5678"}
    ]
    
    # واجهة تسجيل الدخول
    def show_login(e=None):
        page.clean()
        page.add(
            ft.Column([
                ft.Text("تسجيل الدخول", size=30, weight=ft.FontWeight.BOLD),
                ft.Dropdown(
                    label="نوع المستخدم",
                    options=[
                        ft.dropdown.Option("راكب"),
                        ft.dropdown.Option("سائق")
                    ],
                    width=300
                ),
                ft.TextField(label="اسم المستخدم", width=300),
                ft.TextField(label="كلمة المرور", password=True, width=300),
                ft.ElevatedButton("دخول", on_click=login),
                ft.TextButton("تسجيل جديد", on_click=show_register)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
    
    # واجهة التسجيل
    def show_register(e=None):
        page.clean()
        page.add(
            ft.Column([
                ft.Text("تسجيل جديد", size=30, weight=ft.FontWeight.BOLD),
                ft.Dropdown(
                    label="نوع المستخدم",
                    options=[
                        ft.dropdown.Option("راكب"),
                        ft.dropdown.Option("سائق")
                    ],
                    width=300
                ),
                ft.TextField(label="الاسم الكامل", width=300),
                ft.TextField(label="اسم المستخدم", width=300),
                ft.TextField(label="كلمة المرور", password=True, width=300),
                ft.TextField(label="تأكيد كلمة المرور", password=True, width=300),
                ft.TextField(label="رقم الرخصة (للسائقين)", width=300, visible=False),
                ft.ElevatedButton("تسجيل", on_click=register),
                ft.TextButton("العودة", on_click=show_login)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
    
    # لوحة الراكب
    def show_passenger_dashboard():
        page.clean()
        
        # محاكاة موقع السائق
        driver_location = [36.7538, 3.0588]
        
        def update_location():
            driver_location[0] += random.uniform(-0.01, 0.01)
            driver_location[1] += random.uniform(-0.01, 0.01)
            location_text.value = f"موقع السائق: {driver_location[0]:.4f}, {driver_location[1]:.4f}"
            page.update()
        
        location_text = ft.Text(f"موقع السائق: {driver_location[0]:.4f}, {driver_location[1]:.4f}")
        
        page.add(
            ft.Column([
                ft.Text(f"مرحباً بك، {current_user['username']}", size=25),
                ft.Tabs(
                    tabs=[
                        ft.Tab(
                            text="حجز رحلة",
                            content=ft.Column([
                                ft.Dropdown(
                                    label="نقطة الانطلاق",
                                    options=[ft.dropdown.Option(loc) for loc in ["البياضة", "أقدال", "أنفيد"]],
                                    width=300
                                ),
                                ft.Dropdown(
                                    label="نقطة الوصول",
                                    options=[ft.dropdown.Option(loc) for loc in ["البياضة", "أقدال", "أنفيد"]],
                                    width=300
                                ),
                                ft.ElevatedButton("بحث عن سائق", on_click=find_driver)
                            ])
                        ),
                        ft.Tab(
                            text="تتبع الرحلة",
                            content=ft.Column([
                                location_text,
                                ft.ElevatedButton("عرض الخريطة", 
                                    on_click=lambda _: webbrowser.open(f"https://maps.google.com?q={driver_location[0]},{driver_location[1]}"))
                            ])
                        )
                    ]
                ),
                ft.ElevatedButton("تسجيل الخروج", on_click=show_login)
            ])
        )
        
        # تحديث الموقع كل 3 ثواني
        page.update()
        page.run_task(lambda: Clock.schedule_interval(update_location, 3))
    
    # دوال العمليات
    def login(e):
        nonlocal current_user
        current_user = {"type": "راكب", "username": "مستخدم تجريبي"}
        show_passenger_dashboard()
    
    def register(e):
        show_login()
        page.snack_bar = ft.SnackBar(ft.Text("تم التسجيل بنجاح!"))
        page.snack_bar.open = True
        page.update()
    
    def find_driver(e):
        page.snack_bar = ft.SnackBar(ft.Text("جارٍ البحث عن سائق..."))
        page.snack_bar.open = True
        page.update()
    
    # بدء التطبيق بالواجهة الرئيسية
    show_login()

ft.app(target=main, view=ft.WEB_BROWSER)
