import turtle #importing turtle module
import random #importing random module
import os #importing os module
import sys
from Menu import Game_Menu
sys.path.insert(0, '/.vscode/Menu/')



wind=turtle.Screen() #activate the function
wind.title(" snake game ") #set the title
wind.bgcolor("black") #set the color
wind.tracer(0) #control the window
wind.setup(width=800,height=600) #set the widths and height of window


class Snake:#create class snake

    def __init__(self):
     #set snake head
     self.snake_head=turtle.Turtle()
     self.snake_head.speed(0) #set snake's head speed
     self.snake_head.shape("circle") #set snake's head shape 
     self.snake_head.goto(0,0) #set snake's head coordinates
     self.snake_head.penup() #delete the line after moving
     self.snake_head.color("red") #set snake's head color
      
     #set snake body
     self.snake_body=turtle.Turtle() #set the object
     self.snake_body.speed(0) #set the snake's body speed
     self.snake_body.color("red") #set the snake's body color
     self.snake_body.shape("circle") #set the snake's body shape
     self.snake_body.goto(2,0) #set the snake's body coordinates
     self.snake_body.penup() #delete the line after moving
    
     #set snake tail
     self.snake_tail=turtle.Turtle() #set the object
     self.snake_tail.speed(0) #set the snake's tail speed
     self.snake_tail.color("red") #set the snake's tail color
     self.snake_tail.shape("circle") #set the snake's tail shape
     self.snake_tail.goto(3,0) #set the snake's tail coordinates
     self.snake_tail.penup() #delete the line after moving

     

    def snake_add_body(self):
       add_body=[]
       for body in add_body:
          new_body=turtle.Turtle()
          new_body.speed(0)
          new_body.color("red")
          new_body.shape("circle")
          new_body.goto(4,0)
          new_body.penup()
          add_body.append(body)

    
    def movement(self):
       self.direction="stop"
       if self.direction=="up":
          self.snake_head.sety(self.snake_head.ycor()+20)
       
       if self.direction=="down":
          self.snake_head.sety(self.snake_head.ycor()-20)

       if self.direction=="left":
          self.snake_head.setx(self.snake_head.xcor()-20)

       if self.direction=="right":
          self.snake_head.setx(self.snake_head.xcor()+20)


    def sn_up(self):
       if self.direction !="down":
          self.direction =="up"
      

    def sn_down(self):
       if self.direction !="up":
          self.direction =="down"


    def sn_right(self):
       if self.direction !="left":
          self.direction =="right"


    def sn_left(self):
       if self.direction !="right":
          self.direction =="left"


    
    def init_movement(self):
       wind.listen()
       wind.onkey(self.sn_up(),"Up")
       wind.onkey(self.sn_down(),"Down")
       wind.onkey(self.sn_right(),"Right")
       wind.onkey(self.sn_left(),"Left")






class Food:#create class food
   
   def food(self):

     self.foodd=turtle.Turtle() #set the object
     self.foodd.shape("circle") #set the shape
     self.foodd.color("blue")  #set the color
     self.foodd.penup()  #delete the line after moving
     self.foodd.goto(0,100) #set coorddinates
     return 1
   
   def super_food(self):
      self.sup_food=turtle.Turtle() #set the object
      self.sup_food.shape("circle") #set the shape
      self.sup_food.color("blue")  #set the color
      self.sup_food.penup()  #delete the line after moving
      self.sup_food.goto(0,100) #set cood=rdinates
      return 3
      






class Game:
   while True:
      def __init__(self):
       self.snake=Snake()
       self.food=Food()
       self.snake.init_movement()

      def play_game(self):
       wind.update()

       self.food.random_food()

       self.snake.init_movement()

       self.snake.movement()

       if self.snake.snake_head.distance(self.food.food()):
          self.snake.snake_add_body()
          self.food.random_food()

       if self.snake.snake_head.distance(self.food.super_food()):
          self.snake

       if (self.snake.snake_head.xcor()>390 or self.snake.snake_head.xcor()<-390 or self.snake.snake_head.ycor()>290 or self.snake.snake_head.ycor()<-290):
            os.path/"Game_menu.py"
            Game_Menu.Menu.quit_message()


         
            
            

        
           
               
               
                   




      
     
      
      






      
      


