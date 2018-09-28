import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("percent-bachelors-degrees-women-usa.csv", index_col="Year")

x = df.index.values #the x axis values never change
plt.figure(figsize=(14, 14))


for major in df.columns:
    y = df[major].values #the y axis values do change

    y_pos = df[major].values[-1] - 0.5
    if major == "Foreign Language":
         y_pos += 1
    elif major == "English":
         y_pos -= 1
    elif major == "Communications and Journalism":
         y_pos += 1
    elif major == "Agriculture":
         y_pos += 2
    elif major == "Business":
         y_pos -= 1
    elif major == "Architecture":
         y_pos -= 1
    elif major == "Computer Science":
         y_pos += 1
    elif major == "Engineering":
         y_pos -= 1
    plt.text(2011.5, y_pos, major, fontsize=12)
    plt.plot(x, y, lw=1.5) #lw sets the line width in points


plt.savefig("percent-bachelors-degrees-women-usa1.png",
bbox_inches="tight")


