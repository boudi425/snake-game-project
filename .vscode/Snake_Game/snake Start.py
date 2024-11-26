import turtle #importing turtle module
import random #importing random module
import os #importing os module
import sys #importing sys module




wind=turtle.Screen() #activate the function
wind.title(" welcome to snake game ") #set the title
wind.bgcolor("black") #set the color
wind.tracer(0) #control the window
wind.setup(width=800,height=600) #set the widths and height of window


class Snake:#create class snake

    def snake_main(self): 
     #set snake head
     snake_head=turtle.Turtle() #set the object
     snake_head.speed(0) #set snake's head speed
     snake_head.shape("circle") #set snake's head shape 
     snake_head.goto(0,0) #set snake's head coordinates
     snake_head.penup() #delete the line after moving
     snake_head.color("red") #set snake's head color
      
     #set snake body
     snake_body=turtle.Turtle() #set the object
     snake_body.speed(0) #set the snake's body speed
     snake_body.color("red") #set the snake's body color
     snake_body.shape("circle") #set the snake's body shape
     snake_body.goto(2,0) #set the snake's body coordinates
     snake_body.penup() #delete the line after moving
     snake_body.shapesize(stretch_wid=1,stretch_len=5) #stretch the widths by muiltiplying 5 x 20 
     #set snake tail
     snake_tail=turtle.Turtle() #set the object
     snake_tail.speed(0) #set the snake's tail speed
     snake_tail.color("red") #set the snake's tail color
     snake_tail.shape("circle") #set the snake's tail shape
     snake_tail.goto(3,0) #set the snake's tail coordinates
     snake_tail.penup() #delete the line after moving

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
       
class Food:#create class food
   
   def food(self): #set the food

    food=turtle.Turtle() #set the object
    food.shape("circle") #set the shape
    food.color("blue")  #set the color
    food.penup()  #delete the line after moving
    food.goto(0,100) #set cood=rdinates
    return 1
   
   def super_food(self):
      sup_food=turtle.Turtle() #set the object
      sup_food.shape("circle") #set the shape
      sup_food.color("blue")  #set the color
      sup_food.penup()  #delete the line after moving
      sup_food.goto(0,100) #set cood=rdinates
      return 3
      

class Game:
   while True:
      wind.update()
