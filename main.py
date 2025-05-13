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
    l=0
    
    async def mainactions(e):
        
        if colm1.opacity==0:
            pase1=0
            pase2=0
            pase3=0
            pase4=0
            pase5=0
            pase6=0

            limonada=False
            limonada1=False
            limonada2=False
            limonada3=False
            limonada4=False
            limonada5=False

        tf.value=e.control.value
        

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        y=list(tf.value)
        if len(y)>=8:
            limonada=True
            pase1=1
        else:
            limonada=False
            pase1=1
        page.update()

        if(regex.search(tf.value)== None):
            limonada1=False

        else:
            limonada1=True
 
        lo = any(char.isupper() for char in tf.value)

        if lo:
            limonada2=False
            
        else:
            limonada3=True

        lo3 = any(char.islower() for char in tf.value)
        if lo3:
            limonada3=False
            
        else:
            limonada3=True
        x = re.findall("[0-9].*[0-9]", tf.value)

        if x:
            limonada4=True

        else:
            limonada4=False


        #Animations triggers
        if pase1 == 1:
            colm1.opacity=1
            page.update()
            await asyncio.sleep(0.35)
            if limonada==True:
                colm1.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext.bgcolor=ft.Colors.GREEN_300
                contfthetext.border=ft.border.all(1, ft.Colors.GREEN)
                cont1.bgcolor=ft.Colors.GREEN_100
                cont1.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm1.opacity=1
                page.update()
                
            else:
                if pase1>1:
                    colm1.opacity=0
                    page.update()
                    await asyncio.sleep(0.32)
                    contfthetext.bgcolor=ft.Colors.RED_300
                    contfthetext.border=ft.border.all(1, ft.Colors.RED)
                    cont1.bgcolor=ft.Colors.RED_100
                    cont1.border=ft.border.all(1, ft.Colors.RED)
                    page.update()
                    colm1.opacity=1
                    page.update()
        
        
        


        page.update()

    t=ft.Text(value="pAsWoRd ChEcKeR", 
              size= 70, 
              font_family="Monocraft",)

    tf=ft.TextField(label="",
                    border=ft.InputBorder.OUTLINE,
                    filled=True,
                    width=600,
                    multiline=True,
                    hint_text="Enter your password here",
                    border_radius=10,
                    on_change=mainactions)
    
    t2=ft.Text(value="The password must have a special character",
               size=15, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")

    t3=ft.Text(value="The password does not have any upper case",
               size=15, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")   

    t4=ft.Text(value="The password does not contain at least 2 numbers",size=15, 
               color=ft.colors.BLACK,
               animate_opacity=300,
               font_family="Monocraft")
    
    t5=ft.Text(value="The password does not contain at least 1 lowercase letter",
               size=15, 
               color=ft.colors.BLACK,animate_opacity=300,
               font_family="Monocraft")
    
    t12=ft.Text(value="Your password must be at least 8 characters.",
               size=15, 
               color=ft.colors.BLACK,animate_opacity=300,
               font_family="Monocraft")
    

    contfthetext = ft.Container(content=
                                ft.Text(
                            value="Rule 1",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    contfthetext2 = ft.Container(content=
                                ft.Text(
                            value="Rule 2",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    contfthetext3 = ft.Container(content=
                                ft.Text(
                            value="Rule 3",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    contfthetext4 = ft.Container(content=
                                ft.Text(
                            value="Rule 4",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    contfthetext5 = ft.Container(content=
                                ft.Text(
                            value="Rule 5",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    contfthetext6 = ft.Container(content=
                                ft.Text(
                            value="Rule 6",
                            font_family="Monocraft"
                        ),
                                bgcolor=ft.Colors.RED_300, 
                                animate_opacity=300, 
                                opacity= 1, 
                                width= 600, 
                                alignment=ft.alignment.center, 
                                border= ft.border.all(1, ft.Colors.RED), 
                                border_radius=5)
    
    cont1= ft.Container(content=t12, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 1, 
                        width= 600, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont= ft.Container(content=t2, 
                       bgcolor=ft.Colors.RED_100, 
                       animate_opacity=300, 
                       opacity= 1, 
                       width= 600, 
                       height=50, 
                       alignment=ft.alignment.center, 
                       border= ft.border.all(1, ft.Colors.RED), 
                       border_radius=10)  
    
    cont2= ft.Container(content=t3, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 1, width= 600, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont3= ft.Container(content=t4, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 1, 
                        width= 600, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    cont4= ft.Container(content=t5, 
                        bgcolor=ft.Colors.RED_100, 
                        animate_opacity=300, 
                        opacity= 1, 
                        width= 600, 
                        height=50, 
                        alignment=ft.alignment.center, 
                        border= ft.border.all(1, ft.Colors.RED), 
                        border_radius=10)
    
    colm1= ft.Column(controls=[contfthetext,cont1],spacing=0, animate_opacity=300, opacity= 0)
    colm2= ft.Column(controls=[contfthetext2,cont],spacing=0, animate_opacity=300, opacity= 0)
    colm3= ft.Column(controls=[contfthetext3,cont2],spacing=0, animate_opacity=300, opacity= 0)
    colm4= ft.Column(controls=[contfthetext4,cont3],spacing=0, animate_opacity=300, opacity= 0)
    colm5= ft.Column(controls=[contfthetext5,cont4],spacing=0, animate_opacity=300, opacity= 0)
    # colm6= ft.Column(controls=[contfthetext5,cont5],spacing=0, animate_opacity=300, opacity= 0)

    colm = ft.Column(controls=[colm1, colm2, colm3, colm4, colm5])
    x=page.add(t,tf,colm)


ft.app(target=main, assets_dir="assets")