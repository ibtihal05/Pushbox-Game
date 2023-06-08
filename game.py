from operator import imod
from time import sleep
import pygame
import pytmx
import pyscroll
from player import Player
from box import Box
import search

class Game :
    def __init__(self,carte, nb_box, x, y):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption("sokopuzzle - aventure")
        
        #charger la carte tmx
        tmx_data = pytmx.util_pygame.load_pygame(carte)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layyer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        #generer un joueur 
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        
        #generer les caisses
        # box_position = tmx_data.get_object_by_name("box1")
        # self.box = Box(box_position.x, box_position.y)
        self.box=[]
        box="box"
        i=1
        k=0
        while i<=nb_box :
            box_position = tmx_data.get_object_by_name(box+str(i))
            self.box.append( Box(box_position.x, box_position.y) )
            k=k+1
            i=i+1

        #definir une liste de collision
        self.walls=[]
        for obj in  tmx_data.objects :
            if obj.type=="collision"  :
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layyer, default_layer=1)
        self.group.add(self.player)
        self.group.add(self.box)

    
    def simulation(self,board) :
        initial_node = search.create_initial_node(board)
        goalNode, num_steps = search.Search.A(initial_node, heuristic=3)
        if goalNode:
            print (f"Optimal Solution found after {num_steps} steps")
            solution = goalNode.getSolution()
            for node in solution :
                self.player.move(node)
                Box.move(self.box, node)

                self.group.update()
                self.group.draw(self.screen)
            
                pygame.display.flip()
                sleep(1)
            return len(solution)-1

                
                  
        else:
            print ("Optimal solution not found") 
            return 0
    


