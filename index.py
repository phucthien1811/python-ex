# Đọc file input
with open("testfile.txt", "r", encoding="utf-8") as f:
    data = f.read()          # đọc toàn bộ nội dung
    words = data.splitlines()  # tách thành danh sách các từ (theo dòng)

# Ghép các từ thành 1 câu
sentence = " ".join(words)

# Ghi ra file output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(sentence)
