def pro(cabins,bol,size,clock,ask):
            import pygame
            pygame.init()
            run=True
            door=pygame.image.load("door.png")
            thumbs=int(400/int((cabins/2)/3))
            thumbsup=int(400/(int((cabins/2)/3)+1))
            sprite=int(400/(int((cabins+1/2)/3)))
            cab_up_l=[]
            cab_up_m=[]
            cab_up_r=[]
            cab_down_l=[]
            cab_down_m=[]
            cab_down_r=[]
            A=True
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

            #for i in bol[0]:
             #   i[0],i[1]=i[1],i[0]
                       
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

            #for i in bol[1]:
             #   i[0],i[1]=i[1],i[0]
                       
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

            #for i in bol[2]:
             #   i[0],i[1]=i[1],i[0]
                       
            cabup=cabup1
            cabdown=cabdown1
            print(cabup)
            print(cabdown)
            if ask=='a' or ask=='A':
                    if cabins%2==0:
                        if (cabins/2)%3==0:
                            
                            for i in range(0,int((cabins/2)/3)):
                                cab_up_l.append((thumbs*i,0,thumbs,250))  
                                cab_up_m.append((thumbs*i+450,0,thumbs,250))    
                                cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                cab_down_l.append((thumbs*i,350,thumbs,250))  
                                cab_down_m.append((thumbs*i+450,350,thumbs,250))    
                                cab_down_r.append((thumbs*i+900,350,thumbs,250))
                        else:
                            if (cabins/2)%3==1:
                               
                               for i in range(0,int((cabins/2)/3)+1):
                                   cab_up_l.append((thumbsup*i,0,thumbsup,250))
                                   cab_down_l.append((thumbsup*i,350,thumbsup,250))
                               for i in range(0,int((cabins/2)/3)):
                                   cab_up_m.append((thumbs*i+450,0,thumbs,250))
                                   cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                   cab_down_m.append((thumbs*i+450,350,thumbs,250))
                                   cab_down_r.append((thumbs*i+900,350,thumbs,250))
                            else:
                                
                                for i in range(0,int((cabins/2)/3)+1):
                                    cab_up_l.append((thumbsup*i,0,thumbsup,250))
                                    cab_up_m.append((thumbsup*i+450,0,thumbsup,250))
                                    cab_down_l.append((thumbsup*i,350,thumbsup,250))
                                    cab_down_m.append((thumbsup*i+450,350,thumbsup,250))
                                for i in range(0,int((cabins/2)/3)):    
                                    cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                    cab_down_r.append((thumbs*i+900,350,thumbs,250))
                    else:
                        cab=cabins+1
                        thumb=int(400/int((cab/2)/3))
                        thum=int(400/(int((cab/2)/3)+1))
                        if (cab/2)%3==0:
                            for i in range(0,int((cab/2)/3)):
                                cab_up_l.append((thumb*i,0,thumb,250))  
                                cab_up_m.append((thumb*i+450,0,thumb,250))    
                                cab_up_r.append((thumb*i+900,0,thumb,250))
                                
                        if (cab/2)%3==1:
                           
                            for i in range(0,int((cab/2)/3)+1):
                                cab_up_l.append((thum*i,0,thum,250))
                            for i in range (0,int((cab/2)/3)):
                                cab_up_m.append((thumb*i+450,0,thumb,250))    
                                cab_up_r.append((thumb*i+900,0,thumb,250))
                                
                        if (cab/2)%3==2:
                           
                            for i in range(0,int((cab/2)/3)+1):
                                cab_up_l.append((thum*i,0,thum,250))
                                cab_up_m.append((thum*i+450,0,thum,250)) 
                            for i in range (0,int((cab/2)/3)):
                                    
                                cab_up_r.append((thumb*i+900,0,thumb,250))

                        if int((cabins/2))%3==0:
                            
                            for i in range(0,int((cabins/2)/3)):
                                
                                cab_down_l.append((thumbs*i,350,thumbs,250))  
                                cab_down_m.append((thumbs*i+450,350,thumbs,250))    
                                cab_down_r.append((thumbs*i+900,350,thumbs,250))
                         
                        else:
                            if int((cabins/2))%3==1:
                               for i in range(0,int((cabins/2)/3)+1):
                                   cab_down_l.append((thumbsup*i,350,thumbsup,250))
                               for i in range(0,int((cabins/2)/3)):
                                   cab_down_m.append((thumbs*i+450,350,thumbs,250))
                                   cab_down_r.append((thumbs*i+900,350,thumbs,250))
                            else:
                                for i in range(0,int((cabins/2)/3)+1):
                                    cab_down_l.append((thumbsup*i,350,thumbsup,250))
                                    cab_down_m.append((thumbsup*i+450,350,thumbsup,250))
                                for i in range(0,int((cabins/2)/3)):    
                                    cab_down_r.append((thumbs*i+900,350,thumbs,250))      
                
            else:
                
                if cabins%2==0:
                        if (cabins/2)%3==0:
                            
                            for i in range(0,int((cabins/2)/3)):
                                cab_up_l.append((thumbs*i,0,thumbs,250))  
                                cab_up_m.append((thumbs*i+450,0,thumbs,250))    
                                cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                cab_down_l.append((thumbs*i,350,thumbs,250))  
                                cab_down_m.append((thumbs*i+450,350,thumbs,250))    
                                cab_down_r.append((thumbs*i+900,350,thumbs,250))
                        else:
                            if (cabins/2)%3==1:
                               
                               for i in range(0,int((cabins/2)/3)+1):
                                   cab_up_l.append((thumbsup*i,0,thumbsup,250))
                                   cab_down_l.append((thumbsup*i,350,thumbsup,250))
                               for i in range(0,int((cabins/2)/3)):
                                   cab_up_m.append((thumbs*i+450,0,thumbs,250))
                                   cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                   cab_down_m.append((thumbs*i+450,350,thumbs,250))
                                   cab_down_r.append((thumbs*i+900,350,thumbs,250))
                            else:
                                
                                for i in range(0,int((cabins/2)/3)+1):
                                    cab_up_l.append((thumbsup*i,0,thumbsup,250))
                                    cab_up_m.append((thumbsup*i+450,0,thumbsup,250))
                                    cab_down_l.append((thumbsup*i,350,thumbsup,250))
                                    cab_down_m.append((thumbsup*i+450,350,thumbsup,250))
                                for i in range(0,int((cabins/2)/3)):    
                                    cab_up_r.append((thumbs*i+900,0,thumbs,250))
                                    cab_down_r.append((thumbs*i+900,350,thumbs,250))
                else:
                        cab=cabins+1
                        thumb=int(400/int((cab/2)/3))
                        thum=int(400/(int((cab/2)/3)+1))
                        if (cab/2)%3==0:
                            for i in range(0,int((cab/2)/3)):
                                cab_up_l.append((thumb*i,0,thumb,250))  
                                cab_up_m.append((thumb*i+450,0,thumb,250))    
                                cab_up_r.append((thumb*i+900,0,thumb,250))
                                
                        if (cab/2)%3==1:
                           
                            for i in range(0,int((cab/2)/3)+1):
                                cab_up_l.append((thum*i,0,thum,250))
                            for i in range (0,int((cab/2)/3)):
                                cab_up_m.append((thumb*i+450,0,thumb,250))    
                                cab_up_r.append((thumb*i+900,0,thumb,250))
                                
                        if (cab/2)%3==2:
                           
                            for i in range(0,int((cab/2)/3)+1):
                                cab_up_l.append((thum*i,0,thum,250))
                                cab_up_m.append((thum*i+450,0,thum,250)) 
                            for i in range (0,int((cab/2)/3)):
                                    
                                cab_up_r.append((thumb*i+900,0,thumb,250))

                        if int((cabins/2))%3==0:
                            
                            for i in range(0,int((cabins/2)/3)):
                                
                                cab_down_l.append((thumbs*i,350,thumbs,250))  
                                cab_down_m.append((thumbs*i+450,350,thumbs,250))    
                                cab_down_r.append((thumbs*i+900,350,thumbs,250))
                         
                        else:
                            if int((cabins/2))%3==1:
                               for i in range(0,int((cabins/2)/3)+1):
                                   cab_down_l.append((thumbsup*i,350,thumbsup,250))
                               for i in range(0,int((cabins/2)/3)):
                                   cab_down_m.append((thumbs*i+450,350,thumbs,250))
                                   cab_down_r.append((thumbs*i+900,350,thumbs,250))
                            else:
                                for i in range(0,int((cabins/2)/3)+1):
                                    cab_down_l.append((thumbsup*i,350,thumbsup,250))
                                    cab_down_m.append((thumbsup*i+450,350,thumbsup,250))
                                for i in range(0,int((cabins/2)/3)):    
                                    cab_down_r.append((thumbs*i+900,350,thumbs,250))
            win=pygame.display.set_mode((1300,600))
            def draw():
                font = pygame.font.SysFont('comicsansms', size, True)
                font2 = pygame.font.SysFont('comicsansms', 45, True)
                font3=pygame.font.SysFont('comicsanssms',30,True)
                tex1=font.render("PPL",1,(0,0,255))
                tex=font.render("Cabin",1,(0,0,255))
                text2=font2.render("Passage-Way",1,(128,0,150))
                text3=font3.render("Exit",1,(255,0,0))
                win.fill((0,255,0))
                
                win.blit(text2,(500,260))

                if keyy==0:
                    texto=font3.render("case-1",1,(255,0,0))
                if keyy==1:
                    texto=font3.render("case-2",1,(255,0,0))
                if keyy==2:
                    texto=font3.render("case-3",1,(255,0,0))
                win.blit(texto,(30,255))
                
                if ask == 'a' or ask=='A':
                    win.blit(door,(1265,270))
                    win.blit(text3, (1240,255))
                else:
                    win.blit(door,(-20,270))
                    win.blit(text3, (10,255))
                for j in range(0,len(cab_up_l)):
                    text=font.render(cabup[j][1],1,(255,0,0))
                    text1=font.render(str(cabup[j][0]),1,(255,0,0))
                    win.blit(tex,(cab_up_l[j][0]+20,cab_up_l[j][1]))
                    win.blit(tex1,(cab_up_l[j][0]+20,cab_up_l[j][1]+70))
                    win.blit(text,(cab_up_l[j][0]+20,cab_up_l[j][1]+30))
                    win.blit(text1,(cab_up_l[j][0]+20,cab_up_l[j][1]+110))
                    
                for k in range(0,len(cab_up_m)):
                    text=font.render(cabup[len(cab_up_l)+k][1],1,(255,0,0))
                    text1=font.render(str(cabup[len(cab_up_l)+k][0]),1,(255,0,0))
                    win.blit(tex,(cab_up_m[k][0]+20,cab_up_m[k][1]))
                    win.blit(tex1,(cab_up_m[k][0]+20,cab_up_m[k][1]+70))
                    win.blit(text,(cab_up_m[k][0]+20,cab_up_m[k][1]+30))
                    win.blit(text1,(cab_up_m[k][0]+20,cab_up_m[k][1]+110))
                    
                for m in range(0,len(cab_up_r)):    
                    text=font.render(cabup[j+k+m+2][1],1,(255,0,0))
                    text1=font.render(str(cabup[j+k+m+2][0]),1,(255,0,0))
                    win.blit(tex,(cab_up_r[m][0]+20,cab_up_r[m][1]))
                    win.blit(tex1,(cab_up_r[m][0]+20,cab_up_r[m][1]+70))
                    win.blit(text,(cab_up_r[m][0]+20,cab_up_r[m][1]+30))
                    win.blit(text1,(cab_up_r[m][0]+20,cab_up_r[m][1]+110))
                for n in range(0,len(cab_down_l)):
                    text=font.render(cabdown[n][1],1,(255,0,0))
                    text1=font.render(str(cabdown[n][0]),1,(255,0,0))
                    win.blit(tex,(cab_down_l[n][0]+20,cab_down_l[n][1]))
                    win.blit(tex1,(cab_down_l[n][0]+20,cab_down_l[n][1]+70))
                    win.blit(text,(cab_down_l[n][0]+20,cab_down_l[n][1]+30))
                    win.blit(text1,(cab_down_l[n][0]+20,cab_down_l[n][1]+110))
                for o in range(0,len(cab_down_m)):
                    text=font.render(cabdown[len(cab_down_l)+o][1],1,(255,0,0))
                    text1=font.render(str(cabdown[len(cab_down_l)+o][0]),1,(255,0,0))
                    win.blit(tex,(cab_down_m[o][0]+20,cab_down_m[o][1]))
                    win.blit(tex1,(cab_down_m[o][0]+20,cab_down_m[o][1]+70))
                    win.blit(text,(cab_down_m[o][0]+20,cab_down_m[o][1]+30))
                    win.blit(text1,(cab_down_m[o][0]+20,cab_down_m[o][1]+110))
                for p in range(0,len(cab_down_r)):
                    text=font.render(cabdown[n+o+p+2][1],1,(255,0,0))
                    text1=font.render(str(cabdown[n+o+p+2][0]),1,(255,0,0))
                    win.blit(tex,(cab_down_r[p][0]+20,cab_down_r[p][1]))
                    win.blit(tex1,(cab_down_r[p][0]+20,cab_down_r[p][1]+70))
                    win.blit(text,(cab_down_r[p][0]+20,cab_down_r[p][1]+30))
                    win.blit(text1,(cab_down_r[p][0]+20,cab_down_r[p][1]+110))
                for i in range(0,len(cab_up_l)):
                    pygame.draw.rect(win,(255,0,0),cab_up_l[i],4)
                for i in range(0,len(cab_up_m)):
                    pygame.draw.rect(win,(255,0,0),cab_up_m[i],4)
                for i in range(0,len(cab_up_r)):
                    pygame.draw.rect(win,(255,0,0),cab_up_r[i],4)
                for i in range(0,len(cab_down_l)):
                    pygame.draw.rect(win,(255,0,0),cab_down_l[i],4)
                for i in range(0,len(cab_down_m)):
                    pygame.draw.rect(win,(255,0,0),cab_down_m[i],4)
                for i in range(0,len(cab_down_r)):    
                    pygame.draw.rect(win,(255,0,0),cab_down_r[i],4)
                pygame.draw.rect(win,(0,0,255),(0,250,1300,100),4)
                pygame.draw.rect(win,(0,0,255),(400,0,50,600),4)
                pygame.draw.rect(win,(0,0,255),(850,0,50,600),4)
                pygame.display.update()
            keyy=0
            while run:
                clock.tick(150)
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
