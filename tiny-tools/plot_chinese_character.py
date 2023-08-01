import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_chinese_character(character, font_path):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Load the Chinese font
    chinese_font = FontProperties(fname=font_path)

    # Plot the character
    ax.text(0.5, 0.5, character, fontsize=100, fontproperties=chinese_font, ha='center', va='center')

    # Set the aspect ratio and axis limits
    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Hide the axis ticks and labels
    ax.axis('off')

    # Show the plot
    plt.show()

# Example usage:
character_to_plot = "你"  # Replace this with the Chinese character you want to plot
font_path = '/Users/linaliu/books/font/chinesefont/SIMSUN.ttf'  # Replace this with the path to the Chinese font
plot_chinese_character(character_to_plot, font_path)
