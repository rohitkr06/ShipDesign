def main(lc,bc,ask,cabins,bol):
            import pygame
            import project2
            pygame.init()
            run=True
            cabup1=[]
            cabdown1=[]
            cabup2=[]
            cabdown2=[]
            cabup3=[]
            cabdown3=[]
            if len(bol[0])%2==0:
                for i in range(0,int(len(bol[0])/2)):
                    cabup1.append(bol[0][i])
                for j in range(i+1,len(bol[0])):
                    cabdown1.append(bol[0][j])
            else:
                for i in range(0,int(len(bol[0])/2)+1):
                    cabup1.append(bol[0][i])
                for j in range(i+1,len(bol[0])):
                    cabdown1.append(bol[0][j])

            for i in bol[0]:
                i[0],i[1]=i[1],i[0]
                       
            if len(bol[1])%2==0:
                for i in range(0,int(len(bol[1])/2)):
                    cabup2.append(bol[1][i])
                for j in range(i+1,len(bol[1])):
                    cabdown2.append(bol[1][j])
            else:
                for i in range(0,int(len(bol[1])/2)+1):
                    cabup2.append(bol[1][i])
                for j in range(i+1,len(bol[1])):
                    cabdown2.append(bol[1][j])

            for i in bol[1]:
                i[0],i[1]=i[1],i[0]
                       
            if len(bol[2])%2==0:
                for i in range(0,int(len(bol[2])/2)):
                    cabup3.append(bol[2][i])
                for j in range(i+1,len(bol[2])):
                    cabdown3.append(bol[2][j])
            else:
                for i in range(0,int(len(bol[2])/2)+1):
                    cabup3.append(bol[2][i])
                for j in range(i+1,len(bol[2])):
                    cabdown3.append(bol[2][j])

            for i in bol[2]:
                i[0],i[1]=i[1],i[0]
                       
            cabup=cabup1
            cabdown=cabdown1
            door=pygame.image.load("door.png")
            breadth=200
            
            c=None
            cabi_up=[]
            cabi_down=[]
            cola=int(1000/(int(cabins/2)))
            pepsi=int(1000/(int(cabins/2)+1))
            peps=int(1000/(int(cabins/2)))
            
            u=0
            d=0
            d1=0
            ahead=False
            back=False
            if ask=="a" or ask=="A":
                ahead=True
                cabup.reverse()
                cabdown.reverse()
            elif ask=="b" or ask=="B":
                back=True
            def geteven(cab):
                if cab%2==0:
                    c=0
                else:
                    c=1
                return c
            if geteven(cabins)==0:
                
                for i in range(0,round(cabins/2)):
                    
                        cabi_up.append((cola*i,0,cola,200))
                    
                for j in range (0,round(cabins/2)):
                        cabi_down.append((cola*j,300,cola,200))
            if geteven(cabins)==1:
                  
                  for i in range(0,int(cabins/2)+1):
                    
                        cabi_up.append((pepsi*i,0,pepsi,200))
                    
                  for j in range (0,(int(cabins/2))):
                        cabi_down.append((peps*j,300,peps,200))

              

            win=pygame.display.set_mode((1000,500))
            clock=pygame.time.Clock()

            if cabins>=4 and cabins<=8:
                size=19
            elif cabins>=8 and cabins<=10:
                size=16
            elif cabins>=10 and cabins<=14:
                size=14
            elif cabins>14:
                size=12
            elif cabins>16:
                size=8
            else:
                size=30
            ################################################_______________________________________________#############################################
            if lc>25:
                project2.pro(cabins,bol,size,clock,ask)



                
            else:
                        if lc>15 and lc<=25:
                            if geteven(cabins)==0:    
                                if ask=='b' or ask=="B":
                                    cabi_up_l=[]
                                    cabi_up_r=[]
                                    cabi_do_l=[]
                                    cabi_do_r=[]

                                    if cabins%4==0:
                                        cour=int(450/int(cabins/4))
                                        
                                        for i in range(0,int(cabins/4)):
                                            
                                                cabi_up_r.append((cour*i+550,0,cour,200))
                                                cabi_do_r.append((cour*i+550,300,cour,200))
                                    else:
                                        cour=int(450/(int(cabins/4)+1))
                                        
                                        for i in range(0,int(cabins/4)+1):
                                                cabi_up_r.append((cour*i+550,0,cour,200))
                                                cabi_do_r.append((cour*i+550,300,cour,200))
                                    coul=int(450/int(cabins/4))            
                                    for i in range(0,int(cabins/4)):
                                                cabi_up_l.append((coul*i,0,coul,200))
                                                cabi_do_l.append((coul*i,300,coul,200))
                                    
                                else:
                                    cabi_up_l=[]
                                    cabi_up_r=[]
                                    cabi_do_l=[]
                                    cabi_do_r=[]

                                    if cabins%4==0:
                                        coul=int(450/int(cabins/4))
                                        
                                        for i in range(0,int(cabins/4)):
                                            
                                                cabi_up_l.append((coul*i,0,coul,200))
                                                cabi_do_l.append((coul*i,300,coul,200))
                                    else:
                                        coul=int(450/(int(cabins/4)+1))
                                        
                                        for i in range(0,int(cabins/4)+1):
                                                cabi_up_l.append((coul*i,0,coul,200))
                                                cabi_do_l.append((coul*i,300,coul,200))
                                    cour=int(450/int(cabins/4))            
                                    for i in range(0,int(cabins/4)):
                                                cabi_up_r.append((cour*i+550,0,cour,200))
                                                cabi_do_r.append((cour*i+550,300,cour,200))
                            else:
                                if ask=="a" or ask=='A':
                                    cabi_up_l=[]
                                    cabi_up_r=[]
                                    cabi_do_l=[]
                                    cabi_do_r=[]
                                    if len(cabdown)%2==0:
                                        codl=int(450/int(len(cabdown)/2))
                                        codr=int(450/int(len(cabdown)/2))
                                        for i in range(0,int(len(cabdown)/2)):
                                            cabi_do_l.append((codl*i,300,codl,200))
                                        for i in range(0,int(len(cabdown)/2)):
                                            cabi_do_r.append((codr*i+550,300,codr,200))
                                    else:
                                        codl=int(450/int(len(cabdown)/2+1))
                                        codr=int(450/int(len(cabdown)/2))
                                        for i in range(0,int(len(cabdown)/2+1)):
                                            cabi_do_l.append((codl*i,300,codl,200))
                                        for i in range(0,int(len(cabdown)/2)):
                                                       cabi_do_r.append((codr*i+550,300,codr,200))    
                                    if len(cabup)%2==0:
                                        coul=int(450/int(len(cabup)/2))
                                        cour=int(450/int(len(cabup)/2))
                                        for i in range(0,int(len(cabup)/2)):
                                                       cabi_up_l.append((coul*i,0,coul,200))
                                        for i in range(0,int(len(cabup)/2)):
                                                       cabi_up_r.append((cour*i+550,0,cour,200))
                                    else:
                                        coul=int(450/(int(len(cabup)/2)+1))
                                        cour=int(450/int(len(cabup)/2))
                                        for i in range(0,int(len(cabup)/2)+1):
                                            cabi_up_l.append((coul*i,0,coul,200))
                                        for i in range(0,int(len(cabup)/2)):
                                                       cabi_up_r.append((cour*i+550,0,cour,200))    
                                if ask=='b' or ask=='B':
                                    cabi_up_l=[]
                                    cabi_up_r=[]
                                    cabi_do_l=[]
                                    cabi_do_r=[]
                                    if len(cabup)%2==0:
                                        cour=int(450/int(len(cabup)/2))
                                        coul=int(450/int(len(cabup)/2))
                                        for i in range(0,int(len(cabup)/2)):
                                                       cabi_up_l.append((coul*i,0,coul,200))
                                        for i in range(0,int(len(cabup)/2)):
                                                       cabi_up_r.append((cour*i+550,0,cour,200))
                                    else:
                                        cour=int(450/(int(len(cabup)/2)+1))
                                        coul=int(450/int(len(cabup)/2))
                                        for i in range(0,int(len(cabup)/2)):
                                            cabi_up_l.append((coul*i,0,coul,200))
                                        for i in range(0,int(len(cabup)/2)+1):
                                                       cabi_up_r.append((cour*i+550,0,cour,200))
                                    if len(cabdown)%2==0:
                                        codl=int(450/int(len(cabdown)/2))
                                        codr=int(450/int(len(cabdown)/2))
                                        for i in range(0,int(len(cabdown)/2)):
                                            cabi_do_l.append((codl*i,300,codl,200))
                                        for i in range(0,int(len(cabdown)/2)):
                                            cabi_do_r.append((codr*i+550,300,codr,200))
                                    else:
                                        codr=int(450/int(len(cabdown)/2+1))
                                        codl=int(450/int(len(cabdown)/2))
                                        for i in range(0,int(len(cabdown)/2)):
                                            cabi_do_l.append((codl*i,300,codl,200))
                                        for i in range(0,int(len(cabdown)/2+1)):
                                            cabi_do_r.append((codr*i+550,300,codr,200))    

                        if lc>15 and lc<=25:        
                                def draw():
                                    font = pygame.font.SysFont('comicsansms', size, True)
                                    font2=pygame.font.SysFont('comicsanssms',55,True)
                                    font3=pygame.font.SysFont('comicsanssms',30,True)
                                    win.fill((0,255,0))
                                    text2=font2.render("Passage-Way",1,(128,0,150))
                                    win.blit(text2,(300,230))
                                    if keyy==0:
                                        texto=font3.render("case-1",1,(255,0,0))
                                    if keyy==1:
                                        texto=font3.render("case-2",1,(255,0,0))
                                    if keyy==2:
                                        texto=font3.render("case-3",1,(255,0,0))
                                    win.blit(texto,(30,215))    
                                    if back:
                                        text3=font3.render("Exit",1,(255,0,0))
                                        win.blit(text3,(10,205))
                                        win.blit(door,(-20,215))
                                    
                                    else:
                                        text3=font3.render("Exit",1,(255,0,0))
                                        win.blit(text3,(940,205))
                                        win.blit(door,(970,215))
                                    pygame.draw.rect(win,(255,0,0),(0,400/2,1000,round(0.2*500)),4)
                                    if geteven(cabins)==0:
                                       if ask=='a' or ask=='A': 
                                            if cabins%4==0:
                                                for i in range(0,round(cabins/4)):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    text=font.render(cabdown[i][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+110))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+70))
                                                    
                                                for j in range(0,round(cabins/4)):
                                                    text=font.render(cabup[j+i+1][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+110))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+70))
                                                    text=font.render(cabdown[j+i+1][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+110))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+70))
                                                for i in range(0,int(cabins/4)):
                                                    
                                                    pygame.draw.rect(win,(255,0,0),cabi_up_l[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_l[i],4)
                                                    
                                            else:
                                                
                                                for i in range(0,int(cabins/4)+1):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    text=font.render(cabdown[i][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+110))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+70))
                                                for j in range(0,int(cabins/4)):
                                                    text=font.render(cabup[j+i+1][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+110))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+70))
                                                    text=font.render(cabdown[j+i+1][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+110))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+70))    
                                                for i in range(0,int(cabins/4)+1):
                                                    pygame.draw.rect(win,(255,0,0),cabi_up_l[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_l[i],4)
                                            for i in range(0,int(cabins/4)):
                                                    
                                                    pygame.draw.rect(win,(255,0,0),cabi_up_r[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_r[i],4)
                                       else:
                                            if cabins%4==0:
                                                for i in range(0,round(cabins/4)):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    text=font.render(cabdown[i][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(255,0,0))
                                                    win.blit(text,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+110))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+70))
                                                    
                                                for j in range(0,round(cabins/4)):
                                                    text=font.render(cabup[j+i+1][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+110))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(coul/2)-size*2,cabi_up_r[j][1]+70))
                                                    text=font.render(cabdown[j+i+1][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(255,0,0))
                                                    win.blit(text,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+110))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(coul/2)-size*2,cabi_do_r[j][1]+70))
                                                   
                                                for i in range(0,int(cabins/4)):

                                                    pygame.draw.rect(win,(255,0,0),cabi_up_r[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_r[i],4)
                                                
                                            else:
                                                for i in range(0,int(cabins/4)):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    text=font.render(cabdown[i][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(255,0,0))
                                                    win.blit(text,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+110))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(coul/2)-size*2,cabi_do_l[i][1]+70))
                                                for j in range(0,int(cabins/4)+1):
                                                    text=font.render(cabup[j+i+1][1],1,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabup[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(0,0,255))
                                                    win.blit(text,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+110))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+70))
                                                    text=font.render(cabdown[j+i+1][1],2,(255,0,0))
                                                    tex=font.render("Cabin Name",1,(0,0,255))
                                                    text1=font.render(str(cabdown[j+i+1][0]),1,(255,0,0))
                                                    tex1=font.render("PPL",1,(255,0,0))
                                                    win.blit(text,(cabi_do_r[j][0]+int(cour/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(cour/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(cour/2)-size*2,cabi_do_r[j][1]+110))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(cour/2)-size*2,cabi_do_r[j][1]+70))  
                                                for i in range(0,int(cabins/4)+1):
                                                    
                                                    pygame.draw.rect(win,(255,0,0),cabi_up_r[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_r[i],4)
                                            for i in range(0,int(cabins/4)):        
                                                    pygame.draw.rect(win,(255,0,0),cabi_up_l[i],4)
                                                    pygame.draw.rect(win,(255,0,0),cabi_do_l[i],4)
                                    else:
                                        if ask=="a" or ask=='A':
                                            tex=font.render("Cabin Name",1,(0,0,255))
                                            tex1=font.render("PPL",1,(0,0,255))
                                            if len(cabup)%2==0:
                                                for i in range(0,int(len(cabup)/2)):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                            else:
                                                for i in range(0,int(len(cabup)/2)+1):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                            for j in range(0,int(len(cabup)/2)):
                                                    text=font.render(cabup[j+i+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[j+i+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+70))
                                                    win.blit(text,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+110))
                                                    
                                            if len(cabdown)%2==0:
                                                
                                                for i in range(0,int(len(cabdown)/2)):
                                                    text=font.render(cabdown[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+70))
                                                    win.blit(text, (cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+110))
                                            else:
                                                for i in range(0,int(len(cabdown)/2)+1):
                                                    text=font.render(cabdown[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+70))
                                                    win.blit(text, (cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+110))
                                            for j in range(0,int(len(cabdown)/2)):
                                                    text=font.render(cabdown[j+i+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[j+i+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+70))
                                                    win.blit(text, (cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+110))

                                                    
                                            for i in range(0,len(cabi_up_l)):
                                                 pygame.draw.rect(win,(255,0,0),cabi_up_l[i],4)
                                            for i in range(0,len(cabi_up_r)):
                                                 pygame.draw.rect(win,(255,0,0),cabi_up_r[i],4)
                                            for i in range(0,len(cabi_do_l)):
                                                pygame.draw.rect(win,(255,0,0),cabi_do_l[i],4)
                                            for i in range(0,len(cabi_do_r)):
                                                pygame.draw.rect(win,(255,0,0),cabi_do_r[i],4)
                                
                                        else:
                                            tex=font.render("Cabin Name",1,(0,0,255))
                                            tex1=font.render("PPL",1,(0,0,255))
                                            for i in range(0,int(len(cabup)/2)):
                                                    text=font.render(cabup[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]))
                                                    win.blit(tex1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+70))
                                                    win.blit(text,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+30))
                                                    win.blit(text1,(cabi_up_l[i][0]+int(coul/2)-size*2,cabi_up_l[i][1]+110))
                                            if len(cabup)%2==0:
                                                for j in range(0,int(len(cabup)/2)):
                                                    text=font.render(cabup[i+j+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[i+j+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+70))
                                                    win.blit(text,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+110))
                                            else:
                                                for j in range(0,int(len(cabup)/2)+1):
                                                    text=font.render(cabup[i+j+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabup[i+j+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]))
                                                    win.blit(tex1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+70))
                                                    win.blit(text,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+30))
                                                    win.blit(text1,(cabi_up_r[j][0]+int(cour/2)-size*2,cabi_up_r[j][1]+110))
                                            
                                            for i in range(0,int(len(cabdown)/2)):
                                                    text=font.render(cabdown[i][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]))
                                                    win.blit(tex1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+70))
                                                    win.blit(text, (cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+30))
                                                    win.blit(text1,(cabi_do_l[i][0]+int(codl/2)-size*2,cabi_do_l[i][1]+110))       
                                            if len(cabdown)%2==0:
                                                
                                                for j in range(0,int(len(cabdown)/2)):
                                                    text=font.render(cabdown[i+j+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[i+j+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+70))
                                                    win.blit(text, (cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+110))
                                            else:
                                                for j in range(0,int(len(cabdown)/2)+1):
                                                    text=font.render(cabdown[i+j+1][1],1,(255,0,0))
                                                    text1=font.render(str(cabdown[i+j+1][0]),1,(255,0,0))
                                                    win.blit(tex,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]))
                                                    win.blit(tex1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+70))
                                                    win.blit(text, (cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+30))
                                                    win.blit(text1,(cabi_do_r[j][0]+int(codr/2)-size*2,cabi_do_r[j][1]+110))
                                            
                                             
                                            
                                            for i in range(0,len(cabi_up_l)):
                                                 pygame.draw.rect(win,(255,0,0),cabi_up_l[i],4)
                                            for i in range(0,len(cabi_up_r)):
                                                 pygame.draw.rect(win,(255,0,0),cabi_up_r[i],4)
                                            for i in range(0,len(cabi_do_l)):
                                                pygame.draw.rect(win,(255,0,0),cabi_do_l[i],4)
                                            for i in range(0,len(cabi_do_r)):
                                                pygame.draw.rect(win,(255,0,0),cabi_do_r[i],4)
                                    pygame.draw.rect(win,(255,0,0),((450,0,round(0.2*500),1000)),3)   
                                    pygame.display.update()        


                        ####################################____________________________________________________###############################
                        else:
                                def draw():
                                    font = pygame.font.SysFont('comicsansms', size, True)
                                    font2=pygame.font.SysFont('comicsanssms',55,True)
                                    font3=pygame.font.SysFont('comicsanssms',30,True)
                                    win.fill((0,255,0))
                                    #win.blit(flooru,(0,0))
                                    #win.blit(floord,(0,300))
                                    text2=font2.render("Passage-Way",1,(128,0,150))
                                    win.blit(text2,(300,230))
                                    if keyy==0:
                                        texto=font3.render("case-1",1,(255,0,0))
                                    if keyy==1:
                                        texto=font3.render("case-2",1,(255,0,0))
                                    if keyy==2:
                                        texto=font3.render("case-3",1,(255,0,0))
                                    win.blit(texto,(30,215))    
                                    pygame.draw.rect(win,(255,0,0),(0,400/2,1000,round(0.2*500)),4)
                                    if back:
                                        text3=font3.render("Exit",1,(255,0,0))
                                        win.blit(text3,(10,205))
                                        win.blit(door,(-20,215))
                                    
                                    else:
                                        text3=font3.render("Exit",1,(255,0,0))
                                        win.blit(text3,(940,205))
                                        win.blit(door,(970,215))
                                    if geteven(cabins)==0:
                                        for i in range(0,round(cabins/2)):
                                            text=font.render(cabup[i][1],1,(255,0,0))
                                            tex=font.render("Cabin Name",1,(0,0,255))
                                            text1=font.render(str(cabup[i][0]),1,(255,0,0))
                                            tex1=font.render("PPL",1,(0,0,255))
                                            win.blit(text,(cabi_up[i][0]+int(cola/2)-size*2,cabi_up[i][1]+30))
                                            win.blit(tex,(cabi_up[i][0]+int(cola/2)-size*2,cabi_up[i][1]))
                                            win.blit(text1,(cabi_up[i][0]+int(cola/2)-size*2,cabi_up[i][1]+110))
                                            win.blit(tex1,(cabi_up[i][0]+int(cola/2)-size*2,cabi_up[i][1]+70))
                                            text=font.render(cabdown[i][1],2,(255,0,0))
                                            tex=font.render("Cabin Name",1,(0,0,255))
                                            text1=font.render(str(cabdown[i][0]),1,(255,0,0))
                                            tex1=font.render("PPL",1,(255,0,0))
                                            win.blit(text,(cabi_down[i][0]+int(cola/2)-size*2,cabi_down[i][1]+30))
                                            win.blit(tex,(cabi_down[i][0]+int(cola/2)-size*2,cabi_down[i][1]))
                                            win.blit(text1,(cabi_down[i][0]+int(cola/2)-size*2,cabi_down[i][1]+110))
                                            win.blit(tex1,(cabi_down[i][0]+int(cola/2)-size*2,cabi_down[i][1]+70))
                                            pygame.draw.rect(win,(255,0,0),cabi_up[i],4)
                                            pygame.draw.rect(win,(255,0,0),cabi_down[i],4)
                                    if geteven(cabins)==1:        
                                        for j in range(0,int(cabins/2+1)):
                                            text=font.render(cabup[j][1],1,(255,0,0))
                                            tex=font.render("Cabin Name",1,(0,0,255))
                                            text1=font.render(str(cabup[j][0]),1,(255,0,0))
                                            tex1=font.render("PPL",1,(0,0,255))
                                            win.blit(text,(cabi_up[j][0]+int(pepsi/2)-size*2,cabi_up[j][1]+30))
                                            win.blit(tex,(cabi_up[j][0]+int(pepsi/2)-size*2,cabi_up[j][1]))
                                            win.blit(text1,(cabi_up[j][0]+int(pepsi/2)-size*2,cabi_up[j][1]+110))
                                            win.blit(tex1,(cabi_up[j][0]+int(pepsi/2)-size*2,cabi_up[j][1]+70))
                                            pygame.draw.rect(win,(255,0,0),cabi_up[j],4)
                                            if j<int(cabins/2):
                                                text=font.render(cabdown[j][1],1,(255,0,0))
                                                tex=font.render("Cabin Name",1,(0,0,255))
                                                text1=font.render(str(cabdown[j][0]),1,(255,0,0))
                                                tex1=font.render("PPL",1,(0,0,255))
                                                win.blit(text,(cabi_down[j][0]+int(peps/2)-size*2,cabi_down[j][1]+30))
                                                win.blit(tex,(cabi_down[j][0]+int(peps/2)-size*2,cabi_down[j][1]))
                                                win.blit(text1,(cabi_down[j][0]+int(peps/2)-size*2,cabi_down[j][1]+110))
                                                win.blit(tex1,(cabi_down[j][0]+int(peps/2)-size*2,cabi_down[j][1]+70))
                                                pygame.draw.rect(win,(255,0,0),cabi_down[j],4)
                                    pygame.display.update()
                        keyy=0
                        while run:
                            
                            clock.tick(150)
                            keys=pygame.key.get_pressed()
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    run=False
                                if event.type==pygame.KEYDOWN:
                                    if  event.key==pygame.K_RIGHT and keyy<2:
                                       keyy+=1
                                    if  event.key==pygame.K_LEFT and keyy>0:
                                       keyy-=1  
                            if keyy==0:
                                cabup=cabup1
                                cabdown=cabdown1
                            if keyy==1:
                                cabup=cabup2
                                cabdown=cabdown2
                            if keyy==2:
                                cabup=cabup3
                                cabdown=cabdown3
                            draw()
                        pygame.quit()








