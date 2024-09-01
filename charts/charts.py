import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"] #Labels for the pie chart slices
    values = [200, 34, 120] #Values for the pie chart slices
    
    fig, ax = plt.subplots() #Create a figure and an axes instance
    ax.pie (values, labels=labels) #Draw pie chart with the given values and labels
    plt.savefig("pie_chart.png") #Save the plot as a PNG file
    plt.close() #Close the current figure to prevent it from being displayed