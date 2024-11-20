import turtle #importing turtle module
import random #importing random module


#creating the screen
wind=turtle.Screen() #activate the function
wind.title(" welcome to snake game ") #set the title
wind.bgcolor("black") #set the color
wind.tracer(0) #control the window
wind.setup(width=800,height=600) #set the widths and height of window
#------------------------------------------------------------------

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

#-------------------------------------------------

#creating food 
food=turtle.Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

#----------------------

#create additional body