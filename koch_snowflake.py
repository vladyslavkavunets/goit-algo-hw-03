import turtle
import math

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def koch_snowflake(order, size=300):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Сніжинка Коха - Рівень рекурсії: {order}")
    screen.setup(width=800, height=600)
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.pensize(1)
    
    t.penup()
    t.goto(-size/2, size/(2*math.sqrt(3)))
    t.pendown()
    
    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)
    
    screen.exitonclick()

def main():
    print("Фрактал 'Сніжинка Коха'")
    print("=" * 30)
    
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (0-6): "))
            if order < 0:
                print("Рівень рекурсії не може бути від'ємним!")
                continue
            break
        except ValueError:
            print("Введіть ціле число!")
    
    print(f"Малюємо сніжинку з рівнем рекурсії {order}...")
    koch_snowflake(order)

if __name__ == "__main__":
    main()