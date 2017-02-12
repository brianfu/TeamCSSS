import pygame

def bullet_collisions(bullet_list, entity_list, character):
    for bullet in bullet_list:
        for entity in entity_list:
            if bullet.char_bullet and entity.rect.colliderect(bullet):
                entity.Hitpoints += -50
                if entity.Hitpoints == 0:
                    entity.Dead = True
                #print("Enemy Hit")
                if bullet in bullet_list:
                    bullet_list.remove(bullet)
        if not bullet.char_bullet and character.rect.colliderect(bullet):
            character.Hitpoints += -50
            if character.Hitpoints == 0:
                character.Dead = True
            #print("Char Hit")
            bullet_list.remove(bullet)
