import pygame
import random

pygame.init()

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

largeur_ecran = 800
hauteur_ecran = 600
taille_case = 20

# Création de la fenêtre de jeu
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Snake Game")

# Initialisation du serpent
serpent = [(largeur_ecran // 2, hauteur_ecran // 2)]
direction = random.choice(["gauche", "droite", "haut", "bas"])

clock = pygame.time.Clock()

def jeu_snake():
    global serpent, direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Gestion des mouvements du serpent en réponse aux touches
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "droite":
                    direction = "gauche"
                elif event.key == pygame.K_RIGHT and direction != "gauche":
                    direction = "droite"
                elif event.key == pygame.K_UP and direction != "bas":
                    direction = "haut"
                elif event.key == pygame.K_DOWN and direction != "haut":
                    direction = "bas"

        # Mouvements du serpent
        if direction == "gauche":
            serpent.insert(0, (serpent[0][0] - taille_case, serpent[0][1]))
        elif direction == "droite":
            serpent.insert(0, (serpent[0][0] + taille_case, serpent[0][1]))
        elif direction == "haut":
            serpent.insert(0, (serpent[0][0], serpent[0][1] - taille_case))
        elif direction == "bas":
            serpent.insert(0, (serpent[0][0], serpent[0][1] + taille_case))

        # Supprimer la queue du serpent si la longueur dépasse 1
        if len(serpent) > 1:
            serpent.pop()

        ecran.fill(NOIR)

        for partie in serpent:
            pygame.draw.rect(ecran, VERT, (partie[0], partie[1], taille_case, taille_case))

        pygame.display.update()
        clock.tick(10)  # Contrôle de la vitesse du jeu

jeu_snake()
