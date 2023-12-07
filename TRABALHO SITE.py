from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

i=Tk()
i.geometry('800x900')
i.resizable(False,False)

email_e = None
senha_e = None

email_p = None
senha_p = None

def shop():
    shop=Toplevel(i)
    shop.title('SHOP')
    shop.geometry('800x900')
    shop.resizable(0,0)
    shop['bg']='white'

    #frame menu
    frame=Frame(shop, bg='grey', height=90, width=800)
    frame.pack()
    
    frame1=Frame(shop, bg='white', height=86, width=796)
    frame1.place(x=2, y=2)

    login=Button(shop,text='LOGIN',width=10,bd=1,
            height=2,bg='white', fg='black')
    login.place(x=110,y=23)

    cart2_img = PhotoImage(file='cart.png')
    cart2=Button(shop,bd=0,image=cart_img)
    cart2.place(x=205,y=32)

    #logo
    img_shop=Image.open('paradigma_logo.png')
    photo_shop = ImageTk.PhotoImage(img_shop)
    label_img_shop=Label(shop,image=photo_shop,bg='white')
    label_img_shop.image=photo_shop
    label_img_shop.place(x=20, y=15)

    #trending, coleções, categorias
    frame2=Frame(shop, bg='grey', height=30, width=784)
    frame2.place(x=10,y=100)
    
    frame3=Frame(shop, bg='white', height=30, width=780)
    frame3.place(x=12,y=102)
    
    custom_font=font.Font(size=8,weight='bold')#fonte
    
    trending=Label(shop,text='TRENDING',bg='white',font=custom_font)
    trending.place(x=20,y=106)

    colecoes=Label(shop,text='COLEÇÕES',bg='white',font=custom_font)
    colecoes.place(x=80,y=106)

    categorias=Label(shop,text='CATEGORIAS',bg='white',font=custom_font)
    categorias.place(x=145,y=106)

    #pesquisa
    pesquisa=Entry(shop,bg='white')
    pesquisa.place(x=660,y=106)
    
    pesquisa_img=Image.open('pesquisa.png')
    photo_pesquisa=ImageTk.PhotoImage(pesquisa_img)
    label_pesquisa_img=Label(shop,image=photo_pesquisa,bg='white')
    label_pesquisa_img.image=photo_pesquisa
    label_pesquisa_img.place(x=615,y=102)
    
    #vitrine1
    vitrine_img=Image.open('vitrine1.png')
    photo_vitrine = ImageTk.PhotoImage(vitrine_img)
    label_vitrine_img=Label(shop,image=photo_vitrine,bg='grey')
    label_vitrine_img.image=photo_vitrine
    label_vitrine_img.place(x=10, y=130)

    #frame carrossel
    frame_c=Frame(shop,bg='grey',height=5,width=5)
    frame_c.place(x=390,y=420)
    
    frame_c1=Frame(shop,bg='grey',height=5,width=5)
    frame_c1.place(x=400,y=420)

    frame_c2=Frame(shop,bg='grey',height=5,width=5)
    frame_c2.place(x=410,y=420)

    frame_c3=Frame(shop,bg='white',height=3,width=3)
    frame_c3.place(x=391,y=421)

    #vitrine2
    vitrine2_img=Image.open('vitrine2.png')
    photo_vitrine2 = ImageTk.PhotoImage(vitrine2_img)
    label_vitrine2_img=Label(shop,image=photo_vitrine2,bg='grey')
    label_vitrine2_img.image=photo_vitrine2
    label_vitrine2_img.place(x=10, y=438)

    #frame vitrine2
    frame_vit=Frame(shop,bg='grey',height=303,width=2)
    frame_vit.place(x=275,y=438)

    frame_vit2=Frame(shop,bg='grey',height=303,width=2)
    frame_vit2.place(x=520,y=438)

    #vitrine3
    vitrine3_img=Image.open('vitrine3.png')
    photo_vitrine3 = ImageTk.PhotoImage(vitrine3_img)
    label_vitrine3_img=Label(shop,image=photo_vitrine3,bg='grey')
    label_vitrine3_img.image=photo_vitrine3
    label_vitrine3_img.place(x=10, y=738)

    #frame vitrine3
    frame_vit3=Frame(shop,bg='grey',height=303,width=2)
    frame_vit3.place(x=275,y=738)

    frame_vit4=Frame(shop,bg='grey',height=303,width=2)
    frame_vit4.place(x=520,y=738)

def edit_email():
    global email_e
    global email_p

    email_p_value = email_p.get()
    email_e_value = email_e.get()

    if(email_p_value==''):
        MessageBox.showinfo('STATUS','TODOS OS CAMPOS SÃO OBRIGATÓRIOS!')
    else:
        conexao=mysql.connect(host='localhost',
                              user='root',
                              passwd='',
                              database='cadastro_loja')
        x=conexao.cursor()
        x.execute('update cliente set email = %s where email = %s',(email_p.get(),email_e.get()))
        x.execute('commit')
        MessageBox.showinfo('STATUS','EMAIL ALTERADO COM SUCESSO!')
        x.close()

def edit_senha():
    global senha_e
    global senha_p

    senha_p_value = senha_p.get()
    senha_e_value = senha_e.get()

    if(senha_p_value==''):
        MessageBox.showinfo('STATUS','TODOS OS CAMPOS SÃO OBRIGATÓRIOS!')
    else:
        conexao=mysql.connect(host='localhost',
                              user='root',
                              passwd='',
                              database='cadastro_loja')
        x=conexao.cursor()
        x.execute('update cliente set senha = %s where senha = %s',(senha_p.get(),senha_e.get()))
        x.execute('commit')
        MessageBox.showinfo('STATUS','SENHA ALTERADA COM SUCESSO!')
        x.close()

def delete():
    global email_e
    
    email_e_value = email_e.get()
   
    conexao=mysql.connect(host='localhost',
                          user='root',
                          passwd='',
                          database='cadastro_loja')
    x=conexao.cursor()
    x.execute('delete from cliente where email = "'+email_e.get()+'"')
    x.execute('commit')
    MessageBox.showinfo('STATUS','CONTA DELETADA COM SUCESSO!')
    x.close()


def perfil():
    global email_e, senha_e
    global email_p, senha_p
    perfil=Toplevel(i)
    perfil.title('MEU PERFIL')
    perfil.geometry('800x900')
    perfil.resizable(0,0)
    perfil['bg']='grey'

    #fundo
    img_fundo=Image.open('menuprincipal.png')
    photo_fundo=ImageTk.PhotoImage(img_fundo)
    label_img_fundo=Label(perfil,image=photo_fundo,bg='white')
    label_img_fundo.image=photo_fundo
    label_img_fundo.place(x=-15,y=-60)

    #frame perfil
    frame_perfil=Frame(perfil,bg='white',height=400,width=400)
    frame_perfil.place(x=200,y=200)

    #logo
    img_logo_perfil=Image.open('paradigma_logo.png')
    photo_logo_perfil=ImageTk.PhotoImage(img_logo_perfil)
    label_img_logo_perfil=Label(perfil,image=photo_logo_perfil,bg='white')
    label_img_logo_perfil.image=photo_logo_perfil
    label_img_logo_perfil.place(x=365,y=210)
    
    #meu perfil logo
    img_perfil=Image.open('perfil2.png')
    photo_perfil=ImageTk.PhotoImage(img_perfil)
    label_img_perfil=Label(perfil,image=photo_perfil,bg='white')
    label_img_perfil.image=photo_perfil
    label_img_perfil.place(x=422,y=290)

    #frame linha
    frame_perfil=Frame(perfil,bg='black',height=30,width=2)
    frame_perfil.place(x=405,y=285)

    #meu perfil
    custom_font=font.Font(size=10,weight='bold')
    
    meu_perfil_l=Label(perfil,text='PERFIL',bg='white',font=custom_font)
    meu_perfil_l.place(x=340,y=290)

    #email
    email_l=Label(perfil,text='E-mail:',bg='white')
    email_l.place(x=260,y=380)

    email_p=Entry(perfil)
    email_p.place(x=320,y=380)

    #editar email
    editar=Button(perfil,text='EDITAR EMAIL',width=13,bd=1,
            height=2,bg='white', fg='black',command=edit_email)
    editar.place(x=465,y=370)

    #senha
    senha_l=Label(perfil,text='Senha:',bg='white')
    senha_l.place(x=260,y=470)

    senha_p=Entry(perfil)
    senha_p.place(x=320,y=470)

    #editar senha
    editar=Button(perfil,text='EDITAR SENHA',width=13,bd=1,
            height=2,bg='white', fg='black',command=edit_senha)
    editar.place(x=465,y=460)

    #excluir conta
    excluir=Button(perfil,text='EXCLUIR CONTA',width=15,bd=1,
            height=2,bg='#8C031C', fg='white',command=delete)
    excluir.place(x=345,y=540)

def cadastro():
    global email_e, senha_e

    if(email_e.get()=='' or senha_e.get()==''):
        MessageBox.showinfo('STATUS','TODOS OS CAMPOS SÃO OBRIGATÓRIOS!')
    else:
        conexao=mysql.connect(host='localhost',
                              user='root',
                              passwd='',
                              database='cadastro_loja')
        x=conexao.cursor()
        x.execute('insert into cliente values(%s,%s)',(email_e.get(),senha_e.get()))
        x.execute('commit')
        MessageBox.showinfo('STATUS','CADASTRO CONCLUÍDO COM SUCESSO!')
        x.close()

def login():
    global email_e, senha_e
    login=Toplevel(i)
    login.title('LOGIN')
    login.geometry('800x900')
    login.resizable(0,0)
    login['bg']='grey'

    #fundo
    img_fundo=Image.open('menuprincipal.png')
    photo_fundo=ImageTk.PhotoImage(img_fundo)
    label_img_fundo=Label(login,image=photo_fundo,bg='white')
    label_img_fundo.image=photo_fundo
    label_img_fundo.place(x=-15,y=-60)

    #frame login
    frame_login=Frame(login,bg='white',height=300,width=400)
    frame_login.place(x=200,y=250)

    #logo
    img_logo_login=Image.open('paradigma_logo.png')
    photo_logo_login=ImageTk.PhotoImage(img_logo_login)
    label_img_logo_login=Label(login,image=photo_logo_login,bg='white')
    label_img_logo_login.image=photo_logo_login
    label_img_logo_login.place(x=365,y=260)
    
    #email
    email_l=Label(login,text='E-mail:',bg='white')
    email_l.place(x=300,y=370)

    email_e=Entry(login)
    email_e.place(x=360,y=370)

    #senha
    senha_l=Label(login,text='Senha:',bg='white')
    senha_l.place(x=300,y=420)

    senha_e=Entry(login)
    senha_e.place(x=360,y=420)

    #login
    login_b=Button(login,text='LOGIN',width=10,bd=1,
            height=2,bg='white', fg='black')
    login_b.place(x=300,y=470)

    #cadastrar
    cad_b=Button(login,text='CADASTRAR-SE',width=15,bd=1,
            height=2,bg='#8C031C', fg='white',command=cadastro)
    cad_b.place(x=400,y=470)

#menu principal
img_menu=Image.open('menuprincipal.png')
photo_menu=ImageTk.PhotoImage(img_menu)
label_img_menu=Label(i,image=photo_menu,bg='white')
label_img_menu.image=photo_menu
label_img_menu.place(x=-15,y=10)

#frame menu
frame_m=Frame(i,bg='white',height=90,width=800)
frame_m.place(x=0,y=0)

#logo
img_logo=Image.open('paradigma_logo.png')
photo_logo=ImageTk.PhotoImage(img_logo)
label_img_logo=Label(i,image=photo_logo,bg='white')
label_img_logo.image=photo_logo
label_img_logo.place(x=358,y=23)

#botao carrinho
cart_img = PhotoImage(file='cart.png')
cart=Button(i,bd=0,image=cart_img)
cart.place(x=685,y=35)

#botao shop
shop=Button(i,text='SHOP',width=10,bd=1,
            height=2,bg='white', fg='black',command=shop)
shop.place(x=263,y=29)

#botao login
login=Button(i,text='LOGIN',width=10,bd=1,
            height=2,bg='white', fg='black',command=login)
login.place(x=460,y=29)

#botao perfil
meu_perfil_img = PhotoImage(file='perfil.png')
meu_perfil=Button(i,bd=0,image=meu_perfil_img,command=perfil)
meu_perfil.place(x=735,y=36)

i.mainloop()
