# app/turtle_alert.py
import turtle
import textwrap
from pathlib import Path

def show_tip_alert(tip_text=None, tip_file="artifacts/tip_of_day.txt"):
    """
    Display an Engineering Tip of the Day alert window using turtle graphics.
    
    Args:
        tip_text (str): The tip text to display. If None, reads from tip_file.
        tip_file (str): Path to the tip file (relative to project root).
    """
    # Read tip from file if not provided
    if tip_text is None:
        try:
            tip_path = Path(tip_file)
            if tip_path.exists():
                tip_text = tip_path.read_text().strip()
            else:
                tip_text = "No tip available. Generate a new tip first!"
        except Exception as e:
            tip_text = f"Error reading tip: {str(e)}"
    
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("#f0f8ff")  # Alice blue background
    screen.title("🚀 Engineering Tip of the Day")
    screen.setup(width=800, height=600)
    
    # Create a turtle for drawing
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    
    # Draw the alert box border
    def draw_rounded_rect(x, y, width, height, radius=20):
        pen.penup()
        pen.goto(x, y - radius)
        pen.pendown()
        pen.setheading(0)
        pen.circle(radius, 90)
        pen.forward(width - 2 * radius)
        pen.circle(radius, 90)
        pen.forward(height - 2 * radius)
        pen.circle(radius, 90)
        pen.forward(width - 2 * radius)
        pen.circle(radius, 90)
        pen.forward(height - 2 * radius)
    
    # Draw main alert box
    pen.color("#4169e1", "#e6f3ff")  # Royal blue border, light blue fill
    pen.begin_fill()
    draw_rounded_rect(-380, 250, 760, 400)
    pen.end_fill()
    
    # Draw header section
    pen.color("#ff6b35", "#fff5ee")  # Orange border, seashell fill
    pen.begin_fill()
    draw_rounded_rect(-360, 230, 720, 80)
    pen.end_fill()
    
    # Title text
    pen.color("#2c3e50")  # Dark blue-gray
    pen.penup()
    pen.goto(0, 180)
    pen.write("🛠️ ENGINEERING TIP OF THE DAY 🛠️", align="center", 
              font=("Arial", 20, "bold"))
    
    # Subtitle
    pen.goto(0, 150)
    pen.write("Level up your engineering skills!", align="center", 
              font=("Arial", 12, "italic"))
    
    # Wrap the tip text for better display
    wrapped_text = textwrap.fill(tip_text, width=70)
    lines = wrapped_text.split('\n')
    
    # Display the tip content
    pen.color("#2c3e50")
    start_y = 100
    line_height = 25
    
    for i, line in enumerate(lines):
        pen.goto(0, start_y - (i * line_height))
        pen.write(line, align="center", font=("Arial", 14, "normal"))
    
    # Add decorative elements
    pen.color("#ff6b35")
    
    # Left gear icon
    pen.penup()
    pen.goto(-320, 0)
    pen.write("⚙️", align="center", font=("Arial", 40, "normal"))
    
    # Right gear icon
    pen.goto(320, 0)
    pen.write("⚙️", align="center", font=("Arial", 40, "normal"))
    
    # Bottom instruction
    pen.color("#7f8c8d")  # Gray
    pen.goto(0, -200)
    pen.write("Click anywhere to close this alert", align="center", 
              font=("Arial", 12, "italic"))
    
    # Add a close button effect
    def close_alert(x, y):
        screen.bye()
    
    # Make the screen clickable to close
    screen.onclick(close_alert)
    
    # Keep the window open
    screen.mainloop()

def main():
    """Main function to run the turtle alert independently."""
    show_tip_alert()

if __name__ == "__main__":
    main()