# Define the symbols in order
symbols = ["∴", "·", "○", "●", "◉", "※", "★", "◆", "▲", "■"]

rows = 10  # number of rows in pyramid

for i in range(rows):
    line = ["∴"]  # start each row with ∴
    
    # Add the inner symbols symmetrically
    for j in range(1, i + 1):
        line.append(symbols[j])          # left side
        line.append(symbols[j - 1])      # mirrored right side

    # Join with the middle dot
    print("   " * (rows - i - 1) + "· ".join(line))
