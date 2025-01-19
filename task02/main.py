import turtle as t
import math

def draw_pythagoras_tree(t, length, angle, level):
    if level == 0:
        return

    t.forward(length)

    start_position = t.position()
    start_heading = t.heading()

    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, level - 1)

    t.setposition(start_position)
    t.setheading(start_heading)

    t.right(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, level - 1)

    t.setposition(start_position)
    t.setheading(start_heading)


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
    length = 200  # Довжина стовбура
    angle = 45  # Кут розгалуження

    screen = t.Screen()
    screen.setup(width=800, height=800)
    screen.title("Фрактал 'Дерево Піфагора'")

    # Налаштування черепахи
    turtle = t.Turtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.left(90)

    draw_pythagoras_tree(turtle, length, angle, level)

    turtle.hideturtle()
    screen.mainloop()
