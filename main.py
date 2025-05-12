import flet as ft
import re
import asyncio
def main(page: ft.Page):
    
    page.title= "pAsWoRd ChEcKeR"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 60
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.update()

    page.fonts = {
        "Monocraft" : "Monocraft.ttc"
    }   
    async def mainactions(e):

        tf.value=e.control.value
        y=list(tf.value)
        h= 0
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        lii=0
        page.update()
        if len(y)>=8:
            if cont1.bgcolor!=ft.Colors.GREEN_100:
                cont1.opacity=0
                page.update()
                await asyncio.sleep(0.3)
                cont1.bgcolor=ft.Colors.GREEN_100
                cont1.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                await asyncio.sleep(0.3)
                cont1.opacity=1
                page.update()
            else:   
                cont1.bgcolor=ft.Colors.GREEN_100
                page.update()
                cont1.opacity=1
                page.update()
        else:
            t12.value="The password has to be at least 8 characters long"
            if cont1.bgcolor ==ft.Colors.GREEN_100:
                cont1.opacity=0
                page.update()
                await asyncio.sleep(0.3)
            cont1.bgcolor=ft.Colors.RED_100
            cont1.border=ft.border.all(1, ft.Colors.RED)
            page.update()
            await asyncio.sleep(0.2)
            cont1.opacity=1
            t12.opacity=1
            page.update()

        for f in y:
            print(f)
            ans = ''.join(map(str, y))
            print(ans)
            lo = any(char.isupper() for char in ans)
            lo3 = any(char.islower() for char in ans)

            n=0

            if(regex.search(ans) == None):
                t2.value="The String does not contain a special character"
                cont.opacity=1
                t2.opacity=1
                page.update()
               
            else:
                t2.opacity = 0
                page.update()
                

            lo2=False
            for char in y:
                if char.isdigit():
                    n+=1
                if n>=2:
                    lo2=True

            if y[h]=='h':
                print(f"There is an h in digit {h+1}")
            if y[h]=='l':
                print(f"There is an l in digit {h+1}")  
            if lo == True:
                t3.opacity = 0
                page.update()
                
            else:
                t3.value="The string does not have any upper case"
                cont2.opacity=1
                t3.opacity=1
                page.update()
                
            h+=1
            if lo2 == True:
                t4.opacity = 0
                page.update()
                
            else:
                t4.value= "The string does not contain at least 2 numbers"
                cont3.opacity=1
                t4.opacity=1
                page.update()
                
            if lo3 == True:
                t5.opacity = 0
                page.update()
               
            else:
                t5.value = "The string does not vontain at least 1 lowercase letter"
                cont4.opacity=1
                t5.opacity=1
                page.update()
                
        
        page.update()

    t=ft.Text(value="pAsWoRd ChEcKeR", 
              size= 70, 
              font_family="Monocraft",)

    tf=ft.TextField(label="",
                    border=ft.InputBorder.UNDERLINE,
                    filled=True,
                    hint_text="Enter your password here",
                    on_change=mainactions)
    
    t2=ft.Text(value="",
               size=20, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")
    
    t3=ft.Text(value="",
               size=20, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")   
     
    t4=ft.Text(value="",size=20, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")
    
    t5=ft.Text(value="",
               size=20, 
               color=ft.colors.BLACK,animate_opacity=300,
               font_family="Monocraft")
    
    t12=ft.Text(value="",
               size=20, 
               color=ft.colors.BLACK,animate_opacity=300,
               font_family="Monocraft")
    

    contfthetext = ft.Container(content=ft.Text(value="Rule 1",
                                                font_family="Monocraft"))
    contfthetext = ft.Container(content=ft.Text(value="Rule 1", 
                                                font_family="Monocraft"))
    contfthetext = ft.Container(content=ft.Text(value="Rule 1", 
                                                font_family="Monocraft"))
    contfthetext = ft.Container(content=ft.Text(value="Rule 1", 
                                                font_family="Monocraft"))
    contfthetext = ft.Container(content=ft.Text(value="Rule 1",
                                                font_family="Monocraft"))
    contfthetext = ft.Container(content=ft.Text(value="Rule 1",
                                                font_family="Monocraft"))
    
    cont1= ft.Container(content=t12, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 0, 
                        width= 800, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont= ft.Container(content=t2, 
                       bgcolor=ft.Colors.RED_100, 
                       animate_opacity=300, 
                       opacity= 0, 
                       width= 800, 
                       height=50, 
                       alignment=ft.alignment.center, 
                       border= ft.border.all(1, ft.Colors.RED), 
                       border_radius=10)  
    
    cont2= ft.Container(content=t3, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 0, width= 800, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont3= ft.Container(content=t4, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 0, 
                        width= 800, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont4= ft.Container(content=t5, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 0, 
                        width= 800, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    colm = ft.Column(controls=[cont1, cont, cont2, cont3, cont4])
    page.add(t,tf,colm)


ft.app(target=main, assets_dir="assets")