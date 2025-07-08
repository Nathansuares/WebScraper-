import csv

def save_venues_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return

    fieldnames = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV saved as '{filename}'")
