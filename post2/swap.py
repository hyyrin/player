def swap_lines(file_content, a, b):
    # 將內容按行分割
    lines = file_content.split('\n')

    # 確保a和b在有效範圍內
    if 0 <= a < len(lines) and 0 <= b < len(lines):
        # 對調第a行和第b行
        lines[a], lines[b] = lines[b], lines[a]

    # 將列表重新合併為一個字符串
    swapped_content = '\n'.join(lines)
    return swapped_content

html_content = ""
with open("body.html", "r") as body:
    html_content = body.read()

a ,b= input("請輸入兩個整數，以空白做間隔：").split()
a = int(a) - 1
b = int(b) - 1

swapped_content = swap_lines(html_content, a, b)
head_content = ""
tail_content = ""
with open("body.html", "w") as body:
    body.write(swapped_content)
with open("head.html", "r") as head:
        head_content = head.read()
with open("tail.html", "r") as tail:
    tail_content = tail.read()
total_content = head_content + swapped_content + tail_content
with open("index.html", "w") as file:
     file.write(total_content)
