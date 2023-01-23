
import pygame,commands,time
WIDTH = 1750
HEIGHT = 1000
clicked = True
pygame.init()
class direct(pygame.sprite.Sprite):
    def __init__(self,text,index = None):
        super().__init__()
        self.image = pygame.font.Font('freesansbold.ttf', 32)
        self.dir = text
        self.index = index
        self.text = self.image.render(text, True, (0,0,0),(255,255,255))
        self.rect = self.text.get_rect()
    def check_mouse(self,path):

        
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if not path:
                result = commands.run('pwd')
                result = result.stdout.decode().replace('\n','')
                try:
                    commands.cd(result+f'/{self.dir}')
                except NotADirectoryError:
                    if self.dir.split('.')[1]:
                        print('hi')
                        commands.run(['python3',self.dir])
                
            else:
                result = ''
                for i in commands.path()[0:self.index+1]:
                    result += i
                commands.cd(result)
        
                

        if pygame.mouse.get_pressed()[0]:
            return False
        else:
            return True
        

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) 
pwd_group = pygame.sprite.Group()
dir_group = pygame.sprite.Group()
commands.cd('/home')
result = commands.path()
print(result)
for i in commands.dirs():
    dir_group.add(direct(i))
well = 0
for i in commands.path():
    pwd_group.add(direct(i,well))
    well += 1

running = True

while running:
    if pygame.mouse.get_pressed()[2]:
            commands.mkdir(input('name'))
    pygame.time.delay(50)
    pwd = commands.run('pwd')
    for text in dir_group:
        if clicked:
            clicked_pre = text.check_mouse(False)
    for text in pwd_group:
        if clicked:
            clicked_pre = text.check_mouse(True)
    clicked = clicked_pre
    dir_group.empty()
    pwd_group.empty()
    for i in commands.dirs():
        dir_group.add(direct(i))
    well = 0
    for i in commands.path():
        pwd_group.add(direct(i,well))
        well += 1
    if not pygame.mouse.get_pressed()[0]:
        clicked = True
    counter_x = 0 
    counter_y = 64
    path_x = 0
    path_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    WIN.fill((0,0,0))
    
    for text in dir_group:
        text.rect.x = counter_x
        text.rect.y = counter_y
        if text.rect.right > WIDTH:
            counter_x = 0
            counter_y += 32
            text.rect.x = counter_x
            text.rect.y = counter_y
        WIN.blit(text.text,text.rect)
        counter_x += text.rect.width+10
    for text in pwd_group:
        text.rect.x = path_x
        text.rect.y = path_y
        WIN.blit(text.text,text.rect)
        path_x += text.rect.width+10
        


    pygame.display.update()

    