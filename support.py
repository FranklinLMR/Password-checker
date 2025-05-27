import flet as ft
import re
import asyncio
import flet_video as ftv




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
        lacabra.visible=False
        if colm1.opacity==0:
            pase1=0

            limonada=False
            limonada1=False
            limonada2=False
            limonada3=False
            limonada4=False

        tf.value=e.control.value
        

        regex = re.compile('[@_!#$%^&*()<>?/\|.,}{~:]')

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

            if limonada==True:
                limonada1=True
                pase1=2
        
        

        page.update()

        lo = any(char.isupper() for char in tf.value)

        if lo:

            if limonada1==True:
                limonada2=True
                pase1=3
        else:
            limonada2=False
        


        x = re.findall("[0-9].*[0-9]", tf.value)

        if x:
            if limonada2==True:
                limonada4=True
                pase1=4
        else:
            limonada4=False

        lo3 = any(char.islower() for char in tf.value)
        if lo3:
            
            if limonada4==True:
                limonada3=True
                pase1=5
            
            
        else:
            limonada3=False

        #Animations triggers
        if pase1 >= 1:
            if limonada==True and cont1.bgcolor== ft.Colors.RED_100:
                colm1.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext.bgcolor=ft.Colors.GREEN_300
                contfthetext.border=ft.border.all(1, ft.Colors.GREEN)
                cont1.bgcolor=ft.Colors.GREEN_100
                cont1.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm1.opacity=1
                pase1=2
                page.update()

            elif limonada==True and cont1.bgcolor== ft.Colors.GREEN_100:
                pase1=2
                
            else:
                if limonada == False and cont1.bgcolor== ft.Colors.GREEN_100:
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
        
        if pase1 >= 2:
            if limonada1 == True and cont.bgcolor== ft.Colors.RED_100:
                colm2.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext2.bgcolor=ft.Colors.GREEN_300
                contfthetext2.border=ft.border.all(1, ft.Colors.GREEN)
                cont.bgcolor=ft.Colors.GREEN_100
                cont.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm2.opacity=1
                pase1=3
                page.update()
            
            elif limonada1==True and cont.bgcolor== ft.Colors.GREEN_100:
                pase1=3

            else:
                if limonada1 == False and cont.bgcolor== ft.Colors.GREEN_100:
                    colm2.opacity=0
                    page.update()
                    await asyncio.sleep(0.32)
                    contfthetext2.bgcolor=ft.Colors.RED_300
                    contfthetext2.border=ft.border.all(1, ft.Colors.RED)
                    cont.bgcolor=ft.Colors.RED_100
                    cont.border=ft.border.all(1, ft.Colors.RED)
                    page.update()
                colm2.opacity=1
                page.update()

        if pase1 >= 3:
            if limonada2 == True and cont2.bgcolor== ft.Colors.RED_100:
                colm3.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext3.bgcolor=ft.Colors.GREEN_300
                contfthetext3.border=ft.border.all(1, ft.Colors.GREEN)
                cont2.bgcolor=ft.Colors.GREEN_100
                cont2.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm3.opacity=1
                pase1=4
                page.update()
            
            elif limonada2==True and cont2.bgcolor== ft.Colors.GREEN_100:
                pase1=4

            else:
                if limonada2 == False and cont2.bgcolor== ft.Colors.GREEN_100:
                    colm3.opacity=0
                    page.update()
                    await asyncio.sleep(0.32)
                    contfthetext3.bgcolor=ft.Colors.RED_300
                    contfthetext3.border=ft.border.all(1, ft.Colors.RED)
                    cont2.bgcolor=ft.Colors.RED_100
                    cont2.border=ft.border.all(1, ft.Colors.RED)
                    page.update()
                colm3.opacity=1
                page.update()


        if pase1 >= 4:
            if limonada4 == True and cont3.bgcolor== ft.Colors.RED_100:
                colm4.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext4.bgcolor=ft.Colors.GREEN_300
                contfthetext4.border=ft.border.all(1, ft.Colors.GREEN)
                cont3.bgcolor=ft.Colors.GREEN_100
                cont3.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm4.opacity=1
                pase1=5
                page.update()
            
            elif limonada4==True and cont3.bgcolor== ft.Colors.GREEN_100:
                pase1=5
            
            else:
                if limonada4 == False and cont3.bgcolor== ft.Colors.GREEN_100:
                    colm4.opacity=0
                    page.update()
                    await asyncio.sleep(0.32)
                    contfthetext4.bgcolor=ft.Colors.RED_300
                    contfthetext4.border=ft.border.all(1, ft.Colors.RED)
                    cont3.bgcolor=ft.Colors.RED_100
                    cont3.border=ft.border.all(1, ft.Colors.RED)
                    page.update()
                colm4.opacity=1
                page.update()

        if pase1 >= 5:
            if limonada3 == True and cont4.bgcolor== ft.Colors.RED_100:
                colm5.opacity=0
                page.update()
                await asyncio.sleep(0.32)
                contfthetext5.bgcolor=ft.Colors.GREEN_300
                contfthetext5.border=ft.border.all(1, ft.Colors.GREEN)
                cont4.bgcolor=ft.Colors.GREEN_100
                cont4.border=ft.border.all(1, ft.Colors.GREEN)
                page.update()
                colm5.opacity=1
                pase1=6
                page.update()
            
            else:
                if limonada3 == False and cont4.bgcolor== ft.Colors.GREEN_100:
                    colm5.opacity=0
                    page.update()
                    await asyncio.sleep(0.32)
                    contfthetext5.bgcolor=ft.Colors.RED_300
                    contfthetext5.border=ft.border.all(1, ft.Colors.RED)
                    cont4.bgcolor=ft.Colors.RED_100
                    cont4.border=ft.border.all(1, ft.Colors.RED)
                    page.update()
                colm5.opacity=1
                page.update()


        page.update()

    async def checks(e):
        lacabra.visible=False
        if cont.bgcolor==ft.Colors.GREEN_100 and cont1.bgcolor==ft.Colors.GREEN_100 and cont2.bgcolor ==ft.Colors.GREEN_100 and cont3.bgcolor==ft.Colors.GREEN_100 and cont4.bgcolor==ft.Colors.GREEN_100:
            t.value="Perfect password!"
        else:
            t.value="The password misses requirements"

        page.update()
        await asyncio.sleep(2)
        
        t.value="pAsWoRd ChEcKeR"
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
                    on_change=mainactions,
                    password=True,
                    can_reveal_password=True)
    
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
    
    lacabra=ftv.Video(playlist=[ftv.VideoMedia("assets/Mondongo.mp4")], visible=True, autoplay=True, width=800, height=400, show_controls=False)

    check=ft.ElevatedButton(text="Check password",visible=True, on_click=checks)

    colm1= ft.Column(controls=[
                                contfthetext,
                                cont1
                            ],
                    spacing=0, 
                    animate_opacity=300, 
                    opacity= 0
                )
    
    colm2= ft.Column(controls=[
                                contfthetext2,
                                cont
                            ],
                    spacing=0, 
                    animate_opacity=300, 
                    opacity= 0
                )
    colm3= ft.Column(controls=[
                                contfthetext3,
                                cont2
                            ],
                    spacing=0, 
                    animate_opacity=300, 
                    opacity= 0
                )       
    
    colm4= ft.Column(controls=[
                                contfthetext4,
                                cont3
                            ],
                    spacing=0, 
                    animate_opacity=300, 
                    opacity= 0
                )
    
    colm5= ft.Column(controls=[
                                contfthetext5,
                                cont4
                            ],
                    spacing=0, 
                    animate_opacity=300, 
                    opacity= 0
                )

    colm = ft.Column(controls=[
                                colm1, 
                                colm2, 
                                colm3, 
                                colm4, 
                                colm5
                            ]
                    )
    
    sld=ft.Stack(controls=[colm,lacabra])

    x=page.add(t,tf,check,sld)


ft.app(target=main, assets_dir="assets")