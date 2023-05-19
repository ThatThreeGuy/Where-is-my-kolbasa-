from kolbasa_props import *


WHITE = (225, 225, 225)
game_over_music_var = 720

### sfx

bg_music = mixer.music.load('gruppa_krovi.mp3')
mixer.music.set_volume(0.5)

#t_b_c = mixer.music.load('to_be_continued.mp3')

kefteme_sfx = mixer.Sound('kefteme.mp3')

found_sfx = mixer.Sound('found_sfx.mp3')
found_sfx.set_volume(0.25)

dialogue_sfx = mixer.Sound('dialogue_sfx.mp3')
dialogue_sfx.set_volume(0.25)

dialogue_sfx_2 = mixer.Sound('dialogue_sfx_v2.mp3')
dialogue_sfx_2.set_volume(5)

hit_sfx = mixer.Sound('hit_sfx.wav')

sad_sfx = mixer.Sound('spongebob-sad.mp3')

you_should_sfx = mixer.Sound('you_should.mp3')
you_should_sfx.set_volume(0.5)

thunder_sfx = mixer.Sound('thunder.mp3')

thunder_strike = mixer.Sound('thunder_strike.mp3')
#door_break_sfx = mixer.Sound('door_break_sfx.mp3')

ded_sfx = mixer.Sound('game_over.mp3')
ded_sfx.set_volume(0.25)

majestic_ahh = mixer.Sound('majestic_ahh.mp3')
majestic_ahh.set_volume(0.5)

current_dialogue_sfx = dialogue_sfx_2
###
should_do_dialogue_sfx = True
###

bang1_sfx = mixer.Sound('bang1.mp3')
bang2_sfx = mixer.Sound('bang2.mp3')


plr = player('mc_stand_back.png', 250, 200, PLR_SIZE)
shotgun = basicsprite('shotgun_first_person.png', 100, 100, (300, 150))
hand = basicsprite('hand.png', 400, 400, (75, 75))
snipe = basicsprite('snipe.png', 0,0, (50, 50))
background = basicsprite('kitchen_bg.png', 0, 0, WND_SIZE)
dialogue = basicsprite('dlg_prot.png', 0, 0, (WND_SIZE[0], 150))
dialogue_face = basicsprite('face_normal.png', 35, 30, (75, 100))
kolbasa = basicsprite('the_kolbasa_in_question.png', 250, 250, (100, 100))
chefs_table = basicsprite('chef_table.png', 0,0, WND_SIZE)
enter = basicsprite('enter.png', plr.rect.x, plr.rect.y, (175, 175))
lvls_interactable_objs = { 0:{
    (0,400): 'dialogue', (600, 400):'fun dialogue'
    },
    1:{
    (100,201):'fun dialogue', (250, 201):'dialogue'
    },
    1.4:{
    (285, 201):'fun dialogue', (650, 201):'dialogue'
    },
    1.41:{
    (315, 201):'fun dialogue', (650, 201):'dialogue'
    },
    2:
    {
    (575, 201):'fun dialogue', (275, 201):'dialogue'
    },
    2.5:
    {
    (275, 201):'fun dialogue', (650, 201):'dialogue'
    }
}
point_on = None ### На каком интерактивном объекте стоит
locked_door = basicsprite('tutorial_door.png', 200, 0, (300, 500))



dorozh_znak = enm('dorozhniy_znak_battle.png', 250, 250, (300, 300), 30)
low_tier_god = enm('ltg_evil.png', 250, 250, (250, 250), 15)



dorozh_pravila = basicsprite('pravila_dor_dvizh.jpg', 250, 250, (75, 75))
sign_uneffective = basicsprite('uneffective.png', 0,0, (250, 250))

### Рисунки на весь экран
one_pass_after = basicsprite('One_pass_after.png', 0, 0, WND_SIZE)
ded = basicsprite('ded.png', 0,0, WND_SIZE)
fire_writing = basicsprite('fire_writing.png', 0,0, WND_SIZE)
###

amnesia_pills = basicsprite('amnesia_pills.png', 350, 250, (100, 100))

tbc_sprite = basicsprite('tbc.png', 600, 400, (100, 50))

meteorite = basicsprite('meteorite.png', 0, 0, (200, 200))


mc_face_sprites = [
    transform.scale(image.load('face_normal.png'), (75, 100)), ### 0
    transform.scale(image.load('face_bruh.png'), (75, 100)), ### 1
    transform.scale(image.load('face_cry.png'), (75, 100)), ### 2
    transform.scale(image.load('face_sus.png'), (75, 100)), ### 3
    transform.scale(image.load('face_ugh.png'), (75, 100)), ### 4
]

npc_face_sprites = [
    transform.scale(image.load('dorozhniy_znak.png'), (75, 100)), ### 0
    transform.scale(image.load('ltg_good.jpg'), (75, 100)), ### 1
    transform.scale(image.load('ltg_evil.png'), (75, 100)) ### 2
]


lnings = list()

for i in range(3):
    lning = lightning('lightning1.png', 250, 250, (100, 100), rint(25, 55))
    lning.image = lightning_strikes[0]
    lnings.append(lning)


lnings_lengthy = list()

for i in range(2):
    lning_lengthy = lightning('lightning_lengthy.png', 0,0, (100, 100), 3.5)
    lnings_lengthy.append(lning_lengthy)

#lning = lightning('lightning1.png', 250, 250, (100, 100), 25)
#lning.image = lightning_strikes[0]


def music_control():
    global should_do_dialogue_sfx, current_dialogue_sfx, start, interval
    keys = key.get_pressed()
    new_t = tm()

    current_music_volume = mixer.music.get_volume()

    if keys[K_1] and new_t - start > interval:
        start = tm()
        current_music_volume -= 0.1
        mixer.music.set_volume(current_music_volume)
    if keys[K_2] and new_t - start > interval:
        start = tm()
        current_music_volume += 0.1
        mixer.music.set_volume(current_music_volume)

    if keys[K_6] and new_t - start > interval:
        start = tm()
        if should_do_dialogue_sfx:
            should_do_dialogue_sfx = False
        elif should_do_dialogue_sfx == False:
            should_do_dialogue_sfx = True
    if keys[K_7] and new_t - start > interval:
        start = tm()
        if current_dialogue_sfx == dialogue_sfx:
            current_dialogue_sfx = dialogue_sfx_2
        elif current_dialogue_sfx == dialogue_sfx_2:
            current_dialogue_sfx = dialogue_sfx
    if keys[K_8] and new_t - start > interval:
        start = tm()
        mixer.music.stop()

def dlg(t, face_sprite = mc_face_sprites[0], pos = 'up'):
    global game, should_do_dialogue_sfx
    whole_text = ''
    to_continue = False
    dialogue_face.image = face_sprite
    if pos == 'up':
        dialogue.rect.x = 0
        dialogue.rect.y = 0
        dialogue_face.rect.y = 30
    if pos == 'down':
        dialogue.rect.y = WND_SIZE[1] - 150
        dialogue.rect.x = 0
        dialogue_face.rect.y = 375


    dialogue.render()
    dialogue_face.render()

    fontt = font.SysFont('verdana', 30)
    for i in t:
        music_control()
        if should_do_dialogue_sfx:
            mixer.Sound.play(current_dialogue_sfx)
        whole_text += i
        if pos == 'up':
            if len(whole_text) <= 25:
                wnd.blit(fontt.render(whole_text, True, WHITE), (210, 15))
            if len(whole_text) > 25:
                wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,WHITE), (200, 50))
        if pos == 'down':
            if len(whole_text) <= 25:
                wnd.blit(fontt.render(whole_text, True, WHITE), (210, 375))
            if len(whole_text) > 25:
                wnd.blit(fontt.render(whole_text[25:len(whole_text)], True,WHITE), (200, 410))
        clock.tick(15)
        display.update()
    while to_continue == False:
        music_control()
        for ev in event.get():
            if ev.type == QUIT:
                game = False
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    to_continue = True
        if game == False:
            break
        clock.tick(30)
        display.update()
#### DLG
def enter_control(): ### це пздц
    keys = key.get_pressed()
    if keys[K_RETURN] and plr.rect.collidepoint(point_on):
        if lvls_interactable_objs[plr.level_on][point_on] == 'dialogue': ### для сужетных диалогов
            plr.talk += 0.5
        if lvls_interactable_objs[plr.level_on][point_on] == 'fun dialogue': ### для диалогов-пасхалок (так же удобно как есть пиццу вилкой и ножом когда вилка и нож горят)
            if plr.level_on == 0:
                dlg('Всегда знал что никто не любит ходить на лево', mc_face_sprites[4])
            elif plr.level_on == 1:
                dlg('Полностью раздолбанная дверь')
                dlg('Чем больше я смотрю на неё, тем больше понимаю')
                dlg('Что может дробовик был не лучшим решением')
                dlg('Но эх,  мне ли не все равно')
                dlg('Нас чуть четыре раза не посадили за невыплату налогов')
                dlg('Так что я думаю что сломанная дверь - не так уж и плохо')
            elif plr.level_on == 1.4:
                dlg('Аче ты перестал говорить в капсе')
                dlg('Мне лень', npc_face_sprites[0])
                dlg('Пон')
                plr.level_on = 1.41
            elif plr.level_on == 1.41:
                dlg('А кто ты вообще')
                dlg('всм', npc_face_sprites[0])
                dlg('Типо, что ты')
                dlg('Робот правительства', npc_face_sprites[0])
                dlg('Многое объясняет')
                dlg('Разве?', npc_face_sprites[0])
            elif plr.level_on == 2:
                dlg('Вот же она, заветная вывеска')
                dlg('Осталось не много.!')
                dlg('Но сюжет не позволяет', mc_face_sprites[2])
                mixer.Sound.play(sad_sfx)
                sl(0.7)
                dlg('Я обязан сразиться с ещё одним глупым персонажем', mc_face_sprites[2])
                mixer.Sound.play(sad_sfx)
                sl(0.2)
                mixer.Sound.play(sad_sfx)
                sl(0.2)
                mixer.Sound.play(sad_sfx)
                sl(0.7)
            elif plr.level_on == 2.5:
                dlg('Хей, ты!', npc_face_sprites[1], 'down')
                dlg('Да, я веган', mc_face_sprites[4])
                dlg('Ух ты, круто!', npc_face_sprites[1], 'down')

            
            del lvls_interactable_objs[plr.level_on][point_on]  
                  
        
    
while game:
    
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if ev.type == MOUSEBUTTONDOWN and gamemode == 'shotgun' and shotgun_reload_time <= 0 or plr.no_shotgun: ### На стейджи с дробовиком
            shotgun.image = shotguns_anims[1]
            shotgun_reload_time = 20
            #### Аудио шалунство
            if plr.no_shotgun == False:
                mixer.Sound.play(bang1_sfx)
            ####
            if plr.level_on == 0:
                if Rect.colliderect(locked_door.rect, snipe.rect):
                    dlg('Бум')
                    #mixer.Sound.play(door_break_sfx)
                    plr.level_on = 0.5
                elif tutorial_missed_shots == 0:
                    dlg('Ладно.. с кем не бывает',mc_face_sprites[1])
                    tutorial_missed_shots += 1
                elif tutorial_missed_shots == 1:
                    dlg('...', mc_face_sprites[1])
                    tutorial_missed_shots += 1
                elif tutorial_missed_shots == 2:
                    dlg('Ещё раз промажешь я закрою игру', mc_face_sprites[1])
                    tutorial_missed_shots += 1
                elif tutorial_missed_shots == 3:
                    dlg('Доигрался')
                    game = False
            elif plr.level_on == 1:
                if Rect.colliderect(dorozh_znak.rect, snipe.rect):
                    if dorozh_pravila.is_on_screen == False:
                        sign_uneffective.is_on_screen = False
                        dorozh_znak.hp -= 1
                        mixer.Sound.play(hit_sfx)
                        #print(dorozh_znak.hp)
                        dorozh_znak.cd_change_pos_var -= 1
                        if dorozh_znak.hp == 29:
                            dlg('Что за?!', mc_face_sprites[3])
                            dlg('НАНОМАШИНЫ, ЩЕНОК', npc_face_sprites[0], 'down')
                            dlg('ОНИ СТАНОВЯТСЯ ТВЕРЖЕ ПРИ ФИЗИЧЕСКОЙ ТРАВМЕ!!!!', npc_face_sprites[0], 'down')
                            dlg('это я где-то слышал...')
                            dlg('Но, я человек упорный, сдаваться не собираюсь')
                            dlg('ок', npc_face_sprites[0], 'down')
                        elif dorozh_znak.hp == 23:
                            dlg('Чёрт, а ты крепкий орешек.', mc_face_sprites[1])
                            dlg('ДОРОЖНЫЙ ЗНАК.', npc_face_sprites[0], 'down')
                            dlg('что?')
                            dlg('Я ДОРОЖНЫЙ ЗНАК, А НЕ ОРЕШЕК', npc_face_sprites[0], 'down')
                            dlg('Это была метафора..', mc_face_sprites[4])
                        elif dorozh_znak.hp == 16:
                            dlg('Слушай, тебе не кажется что этот боссфайт немного скучный?')
                            dlg('Есть такое', npc_face_sprites[0], 'down')
                            dlg('Так может тогда чё-то сделаешь?')
                            dlg('Найс идея', npc_face_sprites[0], 'down')
                            dorozh_pravila.is_on_screen = True
                            dorozh_pravila.rect.x = rint(250, 500)
                            dorozh_pravila.rect.y = rint(250, 500)

                    ### Игнор
                        elif dorozh_znak.hp in dorozh_znak_when_invinc:
                            dorozh_pravila.is_on_screen = True
                            dorozh_pravila.rect.x = rint(250, 450)
                            dorozh_pravila.rect.y = rint(250, 450)
                        elif dorozh_znak.hp == 0:
                            dlg('Тч', npc_face_sprites[0], 'down')
                            dlg('ЛАДНО, проходи', npc_face_sprites[0], 'down')
                            dlg('Заняло тебе достаточно времени', mc_face_sprites[1])
                            gamemode = 'basic'
                            background.image = transform.scale(image.load('city_1.png'), WND_SIZE)
                            plr.rect.x = 230
                            plr.rect.y = 200
                            plr.level_on = 1.4
                if Rect.colliderect(dorozh_pravila.rect, snipe.rect) and dorozh_pravila.is_on_screen:
                    dorozh_pravila.is_on_screen = False
            elif plr.level_on == 2:
                if Rect.colliderect(low_tier_god.rect, snipe.rect) and plr.no_shotgun == False:
                    low_tier_god.hp -= 1
                    if low_tier_god.hp == 14:
                        dlg('Тщетная попытка', npc_face_sprites[2], 'down')
                        dlg('Тебе это больше не понадобится', npc_face_sprites[2], 'down')
                        dlg('Всм-')
                        mixer.Sound.play(thunder_strike)
                        dlg('ааа моя рука')
                        dlg('мне очееень больнооо')
                        plr.no_shotgun = True
                        dlg('*Чёрт. Он откинул дробовик из моей руки*')
                        dlg('*Мне придется попытаться прожить без него*')
                        dlg('Тебе кто-то говорил про сегодняшний шторм?', npc_face_sprites[2], 'down')
                if Rect.colliderect(hand.rect, amnesia_pills.rect) and low_tier_god.phase == 4:
                    low_tier_god.phase = 5
                    dlg('Ух ты!')
                    dlg('Комически неожиданные таблетки с амнезией!')
                    dlg('как раз что надо!')
                    #plr.no_shotgun = False
    #wnd.fill(WHITE)
    music_control()
    if gamemode == 'basic':
        enter.is_on_screen = False
        background.render()
        plr.control()
        plr.render()

        try:
            for pos in lvls_interactable_objs[plr.level_on]:
                if plr.collpoint(pos[0], pos[1]):
                    enter.rect.x = plr.rect.x
                    enter.is_on_screen = True
                    point_on = pos
        except:
            pass

        if enter.is_on_screen:
            try:
                enter_control()
            except:
                pass
            enter.render()

        if plr.level_on == 0.9: ### Сетап к plr.level_on 1
            PLR_SIZE = (70, 90)
            plr.image = transform.scale(image.load('mc_stand.png'), PLR_SIZE)
            plr.rect = plr.image.get_rect()

            ### Меняю размеры спрайтов на поменьше
            plr.size_change(PLR_SIZE)


            background.image = transform.scale(image.load('city_1.png'), WND_SIZE)
            plr.rect.x = 0
            plr.rect.y = 200
            plr.level_on = 1
            plr.talk = 3

        elif plr.level_on == 1.9: #### Сетап к plr.level_on 2
            ### Интро
            mixer.Sound.play(sad_sfx)
            one_pass_after.render()
            display.update()
            sl(2)


            PLR_SIZE = (70, 90)
            plr.image = transform.scale(image.load('mc_stand.png'), PLR_SIZE)
            plr.rect = plr.image.get_rect()

            ### Меняю размеры спрайтов на поменьше
            plr.size_change(PLR_SIZE)





            background.image = transform.scale(image.load('city_2.png'), WND_SIZE)
            plr.rect.x = 0
            plr.rect.y = 200
            plr.level_on = 2
            plr.talk = 5.5
        
        elif plr.level_on == 2.9:
            PLR_SIZE = (70, 90)
            plr.image = transform.scale(image.load('mc_stand.png'), PLR_SIZE)
            plr.rect = plr.image.get_rect()

            ### Меняю размеры спрайтов на поменьше
            plr.size_change(PLR_SIZE)





            background.image = transform.scale(image.load('city_3.png'), WND_SIZE)
            plr.rect.x = 100
            plr.rect.y = 200
            plr.level_on = 2
            plr.talk = 8

            plr.render()
            background.render()


        


        

        

        if plr.talk == 1:
            plr.image = plr_stand_back
            plr.render()
            dlg('...')
            dlg('Грохочет гром..')
            dlg('Сверкает молния в ночи..')
            dlg('А на холмеееее')
            mixer.Sound.play(sad_sfx)
            sl(0.7)
            dlg('...', mc_face_sprites[1])
            dlg('У меня нет колбасы', mc_face_sprites[2])
            chefs_table.render()
            dlg('Кто бы мог подумать', mc_face_sprites[2])
            chefs_table.render()
            dlg('Но если я вот таким отдам заказ', mc_face_sprites[0], 'down')
            dlg('То не увижу своих кровью и потом заработаных денек', mc_face_sprites[4], 'down')
            dlg('...', mc_face_sprites[4], 'down')
            dlg('Ладно, жить ещё на что-то надо.', mc_face_sprites[4], 'down')
            mixer.music.play()
            dlg('В путь')
            plr.talk += 0.5
        elif plr.talk == 2:
            dlg('...')
            dlg('Ватафак', mc_face_sprites[3])
            dlg('Дверь не открывается')
            dlg('Опять пранк?')
            dlg('Тч')
            dlg('Это может быть и смешно')
            dlg('Но я ещё не видел ничего смешнее дробовика 7-го калибра')
            wnd.fill(GRAY)
            locked_door.render()
            dlg('Главное не промазать')
            gamemode = 'shotgun'
            plr.talk += 0.5
        elif plr.talk == 3:
            dlg('Мясная вроде впереди по курсу')
            dlg('Надо поспешить, не хочу долго задерживаться')
            plr.talk += 0.5
        elif plr.talk == 4:
            mixer.Sound.play(found_sfx)
            sl(1)
            dlg('ХЕЙ ТЫ', npc_face_sprites[0], 'down')
            dlg('?', mc_face_sprites[3])
            dlg('ДА, ТЫ', npc_face_sprites[0], 'down')
            dlg('Я?', mc_face_sprites[3])
            dlg('ДА', npc_face_sprites[0], 'down')
            dlg('Точно я?')
            dlg('ТЫ ШИЗИК? КОГО-ТО ЕЩЁ ВИДЕШЬ НА ЭТОЙ БОГОМ ЗАБЫТОЙ УЛИЦЕ?????>???', npc_face_sprites[0], 'down')
            dlg('Ну нет')
            dlg('ТАК СЛУШАЙ СЮДА ЩЕНОК', npc_face_sprites[0], 'down')
            dlg('ЧТОБЫ ПРОЙТИ ДАЛЬШЕ ДО МЯСНОЙ', npc_face_sprites[0], 'down')
            dlg('ТЕБЕ ПРИДЕТСЯ ПЕРЕЙТИ ЭТОТ ПЕШЕХОДНЫЙ ПЕРЕХОД', npc_face_sprites[0], 'down')
            dlg('НО ВОТ В ЧЕМ ЗАГВОЗДКА', npc_face_sprites[0], 'down')
            dlg('СВЕТОФОР НЕ РАБОТАЕТ', npc_face_sprites[0], 'down')
            dlg('ПОЭТОМУ Я БУДУ ТЕБЕ ГОВОРИТЬ КОГДА ТЫ МОЖЕШЬ ИДТИ', npc_face_sprites[0], 'down')
            dlg('А КОГДА НЕТ', npc_face_sprites[0], 'down')
            dlg('Разве я не могу просто перейти на другой пешех. переход?')
            dlg('ТЫ ЧТО ТУТ САМЫЙ УМНЫЙ?!?!?!', npc_face_sprites[0], 'down')
            dlg('Типо того')
            gamemode = 'shotgun'
            background.image = image.load('dorozhniy_znak_battle_bg.png')  
            plr.talk += 0.5
        elif plr.talk == 5:
            dlg('Что же, это был комически не обязательный враг')
            dlg('Но битв требуют наши сердца')
            dlg('Так что по зову высокой в небе звезды')
            dlg('Я иду в путь')
            plr.talk += 0.5
            plr.level_on = 1.9
        elif plr.talk == 6:
            dlg('Хей ты!', npc_face_sprites[1], 'down')
            dlg('о боже..', mc_face_sprites[1])
            dlg('Ты же знал что жизнь прекрасна?', npc_face_sprites[1], 'down')
            dlg('И ты должен наслаждаться каждой секундой?', npc_face_sprites[1], 'down')
            dlg('Ведь она единственная и не повторимая', npc_face_sprites[1], 'down')
            dlg('Поэтому веганство - лучший способ жизни', npc_face_sprites[1], 'down')
            dlg('Слушай, чел, у меня нет сейчас времени', mc_face_sprites[1])
            dlg('Чего, друг, ты куда-то спешишь?', npc_face_sprites[1], 'down')
            dlg('да.')
            dlg('И куда же, друг?', npc_face_sprites[1], 'down')
            dlg('Мне нужно купить колбасы')
            dlg('... (ОСТОРОЖНО ГРОМКО)', npc_face_sprites[1], 'down')
            mixer.Sound.play(you_should_sfx)
            sl(6)
            dlg('...', npc_face_sprites[2], 'down')
            mixer.Sound.play(thunder_sfx)
            dlg('Ты - отвратителен', npc_face_sprites[2], 'down')
            dlg('Твоё мнение - ужасно', npc_face_sprites[2], 'down')
            dlg('Дед мороз - не настоящий', npc_face_sprites[2], 'down')
            dlg('Твой кот - страдает от лигмы', npc_face_sprites[2], 'down')
            dlg('Твой костюм - блевотный', npc_face_sprites[2], 'down')
            dlg('Я могу найти сироп, стоящий больше чем ты', npc_face_sprites[2], 'down')
            dlg('Воу воу воу воу воу хей хей хей хей', mc_face_sprites[3])
            dlg('Тише, тише')
            dlg('Я просто должен закончить заказ на работе')
            dlg('К черту твою работу', npc_face_sprites[2], 'down')
            dlg('Я должен освободить этот мир от людей как ты', npc_face_sprites[2], 'down')
            plr.talk += 0.5
            gamemode = 'shotgun'
            background.image = transform.scale(image.load('ltg_bg.jpg'), WND_SIZE)
        elif plr.talk == 7:
            dlg('Наконец-то...')
            dlg('Я вне слов')
            dlg('Щас заплачу', mc_face_sprites[2])
            plr.talk += 0.5
            plr.level_on = 2.9
        elif plr.talk == 8:
            dlg('О боже')
            dlg('Оно прекрасно', mc_face_sprites[2])
            dlg('Сейчас же из ниоткуда не произойдёт великий катаклизм?')
            mixer.music.stop()
            t_b_c = mixer.music.load('to_be_continued.mp3')
            mixer.music.play()
            dlg('Стоп')
            dlg('Что это за музыка?')
            sl(5)
            dlg('О НЕТ')
            sl(5)
            dlg('НЕТНЕТНЕТНЕТНЕТНЕТЕНЕТ-')
            sl(5)
            dlg('ТОЛЬКО НЕ ЭТО')
            sl(5)
            dlg('БОЖЕ СПАСИ')
            sl(5)
            dlg('НЕЕЕТ')
            sl(5)
            dlg('НУ ПОЖАЛУЙСТА')
            sl(8)
            dlg('НЕЕЕЕЕ-', mc_face_sprites[0], 'down')
            sl(0.2)
            background.render()
            plr.render()
            meteorite.render()
            tbc_sprite.render()

            display.update()
            sl(10)
            
            dlg('Спасибо за игру!')
            dlg('')
            plr.talk = 10

            


    
    elif gamemode == 'shotgun':
        print(low_tier_god.phase, plr.level_on)
        music_control()
        if plr.level_on == 0: ###Фон и спрайты на экране
            wnd.fill(GRAY)
            locked_door.render()
        elif plr.level_on == 0.5:
            wnd.fill(GRAY)
            locked_door.image = image.load('tutorial_door_open.png')
            locked_door.render()
            dlg('Ух... запах свободы', mc_face_sprites[0], 'down')
            mixer.Sound.play(kefteme_sfx)
            dlg('Кефтеме', mc_face_sprites[0], 'down')
            plr.level_on = 0.9
            gamemode = 'basic'
        
        elif plr.level_on == 1:
            background.render()
            dorozh_znak.render()
            if dorozh_pravila.is_on_screen:
                dorozh_pravila.render()
                sign_uneffective.render()
                sign_uneffective.rect.x = shotgun.rect.x
                sign_uneffective.rect.y = shotgun.rect.y - 200
            if dorozh_znak.hp < dorozh_znak.max_hp and dorozh_znak.cd_change_pos <= 0:
                dorozh_znak.rect.x = rint(0, 600)
                dorozh_znak.rect.y = rint(0, 500)
                dorozh_znak.cd_change_pos = dorozh_znak.cd_change_pos_var
            elif dorozh_znak.hp < dorozh_znak.max_hp and dorozh_znak.cd_change_pos > 0:
                dorozh_znak.cd_change_pos -= 1
        
        elif plr.level_on == 2:
            background.render()
            low_tier_god.render()
            if plr.no_shotgun:
                ### Фаза 1
                if low_tier_god.phase == 1:
                    total_cd = 0
                    for i in lnings:                   
                        if i.set_up == False:
                            if lnings[lnings.index(i)] == lnings[0]:
                                i.strike_setup(hand.rect.x, hand.rect.y)
                            else:
                                i.strike_setup(rint(0, 600), rint(0,600), 0)
                        elif i.set_up and game != False:
                            gamemode = i.strike(lightning_strikes, hand.rect, sad_sfx)
                            
                        i.render()
                        total_cd += i.full_strike_cd
                    if total_cd/len(lnings) <= 27: ### Если становятся слишком быстрыми, меняется на вторую фазу
                        low_tier_god.phase = 2
                        lnings[0].full_strike_cd = 40
                #### Фаза 2
                elif low_tier_god.phase == 2:
                    if lnings[0].set_up == False:
                        lnings[0].strike_setup(hand.rect.x, hand.rect.y)
                    elif lnings[0].set_up and game != False:
                        gamemode = lnings[0].strike(lightning_strikes, hand.rect, sad_sfx)

                    lnings[0].render()


                    if lnings_lengthy[0].set_up == False:
                        lnings_lengthy[0].strike_setup(0, hand.rect.y, 0)
                    elif lnings_lengthy[0].set_up and game != False:
                        gamemode = lnings_lengthy[0].strike_lengthy_horiz(hand.rect, sad_sfx)
                    lnings_lengthy[0].render()
                    if lnings_lengthy[0].strike_cd > 9: ### Закончить
                        low_tier_god.phase = 3
                        lnings_lengthy[0].strike_cd -= 3
                ### Фаза 3
                elif low_tier_god.phase == 3:
                    if lnings_lengthy[0].set_up == False:
                        lnings_lengthy[0].strike_setup(0, hand.rect.y, -65)
                    if lnings_lengthy[1].set_up == False:
                        lnings_lengthy[1].strike_setup(0, hand.rect.y, 70)

                    for i in lnings_lengthy:
                        if i.set_up and game != False:
                            gamemode = i.strike_lengthy_horiz(hand.rect, sad_sfx)
                        i.render()

                    if (lnings_lengthy[0].strike_cd + lnings_lengthy[1].strike_cd) / 2 >= 6.5:
                        low_tier_god.phase = 4
                ### Фаза 4 (Таблетки с амнезией)
                elif low_tier_god.phase == 4:
                    amnesia_pills.render()

                elif low_tier_god.phase == 5:
                    low_tier_god.phase = 6
                
                elif low_tier_god.phase == 6:
                    fire_writing.render()
                    mixer.Sound.play(majestic_ahh)
                    display.update()
                    sl(5)
                    mixer.stop()
                    plr.level_on = 2.5
                    gamemode = 'basic'
                    plr.no_shotgun = False
                    background.image = transform.scale(image.load('city_2.png'), WND_SIZE)

                    
                
                

        
        if shotgun_reload_time == 0:
            shotgun.image = shotguns_anims[0]
        m_x, m_y = mouse.get_pos()
        snipe.rect.x = m_x - 25
        snipe.rect.y = m_y -25 
        if plr.no_shotgun == False:
            snipe.render()
            shotgun.render()
            shotgun.rect.x = m_x
            shotgun.rect.y = m_y + 25
            #shotgun_wait = 120
            if shotgun_reload_time > 0:
                shotgun_reload_time -= 1
        else:
            hand.render()
            hand.rect.x = m_x - 37
            hand.rect.y = m_y - 37
    elif gamemode == 'dead':
        if game_over_music_var >= 720:
            mixer.Sound.play(ded_sfx)
            game_over_music_var = 0
        ded.render()
        game_over_music_var += 1
    
    clock.tick(60)
    display.update()

