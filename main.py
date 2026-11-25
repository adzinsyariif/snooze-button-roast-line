import os

LINE = "You ring at 6 AM on Saturday like a toddler with a kazoo at a funeral — loud, proud, and dead wrong about the occasion."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
