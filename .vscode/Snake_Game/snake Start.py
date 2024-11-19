#Well Well , So , Yusuf the high-leve-member in the project i wish you good luck my boi , i know you will be more than enought for thisop
import turtle #importing turtle module
import random #importing random module

#creating snake head
snake_head=turtle.Turtle() #set the object
snake_head.speed(0) #set snake's head speed
snake_head.shape("circle") #set snake's head shape 
snake_head.goto(0,0) #set snake's head coordinates
snake_head.penup() #delete the line after moving
snake_head.color("red") #set snake's head color
#-------------------------------------------------

#creating snake body

snake_body=turtle.Turtle() #set the object
snake_body.speed(0) #set the snake's body speed
snake_body.color("red") #set the snake's body color
snake_body.shape("circle") #set the snake's body shape
snake_body.goto(0,0) #set the snake's body coordinates
snake_body.penup() #delete the line after moving
snake_body.shapesize(stretch_wid=1,stretch_len=5) #stretch the widths by muiltiplying 5 x 20 
#-----------------------------------------------------

#creating snake tail

snake_tail=turtle.Turtle() #set the object
snake_tail.speed(0) #set the snake's tail speed
snake_tail.color("red") #set the snake's tail color
snake_tail.shape("circle") #set the snake's tail shape
snake_tail.goto(0,0) #set the snake's tail coordinates
snake_tail.penup() #delete the line after moving