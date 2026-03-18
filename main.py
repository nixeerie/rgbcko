from flask import Flask, render_template, request, redirect, url_for
from colors import color_palette
import re

app = Flask(__name__)

# Store gradient history in memory (in production, use a database)
gradient_history = []

def validate_color(color):
    """Validate if color is a valid hex code or color name"""
    if not color or color.strip() == "":
        return False, "Barva nesmí být prázdná"

    color = color.strip()

    # Check if it's a valid hex code (case insensitive)
    hex_pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.match(hex_pattern, color):
        return True, color.upper()

    # Check if it's a color name from our palette (case insensitive)
    color_upper = color.upper()
    for palette_color in color_palette:
        if palette_color['name'].upper() == color_upper:
            return True, palette_color['hex']

    # If it contains invalid characters for hex but looks like it might be intended as hex
    if color.startswith('#') and len(color) == 7:
        return False, f"Neplatné hex znaky v '{color}'. Použijte jen 0-9, A-F (např. #FF0000)."

    # If it looks like a hex code but wrong length
    if color.startswith('#'):
        return False, f"Hex kód musí mít formát #RRGGBB (6 znaků po #). Zadáno: '{color}'."

    # General invalid color message
    return False, f"Neplatná barva: '{color}'. Použijte hex kód (#FF0000) nebo název barvy z palety."

@app.route("/", methods=["GET", "POST"])
def index():
    colors = ["#FF0000", "#008000", "#0000FF"]  # Default colors
    errors = {}

    if request.method == "POST":
        # Get colors from form
        color1 = request.form.get("color1", "").strip()
        color2 = request.form.get("color2", "").strip()
        color3 = request.form.get("color3", "").strip()

        # Validate each color
        valid1, result1 = validate_color(color1)
        valid2, result2 = validate_color(color2)
        valid3, result3 = validate_color(color3)

        if not valid1:
            errors['color1'] = result1
        if not valid2:
            errors['color2'] = result2
        if not valid3:
            errors['color3'] = result3

        if not errors:
            colors = [result1, result2, result3]

            # Add to history if not already there
            if colors not in gradient_history:
                gradient_history.append(colors.copy())

            # Keep only last 10 gradients
            if len(gradient_history) > 10:
                gradient_history.pop(0)
        else:
            # Keep original colors if there are errors
            colors = [color1 or "#FF0000", color2 or "#008000", color3 or "#0000FF"]

    return render_template("index.html", colors=colors, history=gradient_history, color_list=color_palette, errors=errors)

@app.route("/clear_history")
def clear_history():
    global gradient_history
    gradient_history = []
    return redirect(url_for("index"))

@app.route("/load/<int:index>")
def load_gradient(index):
    if 0 <= index < len(gradient_history):
        colors = gradient_history[index]
        return render_template("index.html", colors=colors, history=gradient_history, color_list=color_palette, errors={})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)