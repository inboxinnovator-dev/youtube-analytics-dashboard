import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/youtube_data.csv")

# Data cleaning
df.fillna(0, inplace=True)

# CTR calculation
df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100

# Save summary report
with open("output/summary_report.txt", "w") as f:
    f.write("YouTube Analytics Summary Report\n")
    f.write("===============================\n\n")
    f.write(df.to_string(index=False))

# Plot CTR
plt.figure()
plt.bar(df["Video_Title"], df["CTR (%)"])
plt.xlabel("Video Title")
plt.ylabel("CTR (%)")
plt.title("CTR by Video")
plt.savefig("output/ctr_plot.png")
plt.close()

# Plot Watch Time
plt.figure()
plt.plot(df["Video_Title"], df["Watch_Time_Minutes"], marker="o")
plt.xlabel("Video Title")
plt.ylabel("Watch Time (Minutes)")
plt.title("Watch Time by Video")
plt.savefig("output/watch_time_plot.png")
plt.close()

print("YouTube analytics dashboard generated successfully!")

