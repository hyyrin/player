import os
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def get_mp3_info(file_path):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        title = audio['title'][0] if 'title' in audio else 'Unknown Title'
        artist = audio['artist'][0] if 'artist' in audio else 'Unknown Artist'
        
        # 提取嵌入的封面圖片
        try:
            id3 = ID3(file_path)
            for tag in id3.values():
                if isinstance(tag, APIC):
                    img_data = tag.data
                    img_path = os.path.join(os.path.dirname(file_path), title + '.jpg')
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)
                    return title, artist, img_path
        except Exception as e:
            print(f"Error extracting image from {file_path}: {e}")
        
        return title, artist, 'default.jpg'
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 'Unknown Title', 'Unknown Artist', 'default.jpg'

def save_to_htmll(mp3_info_list, html_file):
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write("<html><body><ul>\n")
        for info in mp3_info_list:
            src, title, artist, img = info
            f.write(f"<li>{{ src: '{src}', name: '{title}', artist: '{artist}', img: '{img}' }}</li>\n")
        f.write("</ul></body></html>\n")

def save_to_html(mp3_info, filename="post1.html"):
    head_content = ""
    tail_content = ""
    body_content = ""
    html_content = ""
    upd_body = ""
    with open("head.html", "r") as head:
        head_content = head.read()
    with open("body.html", "r") as body:
        body_content = body.read()
    with open("../tail.html", "r") as tail:
        tail_content = tail.read()
    html_content += head_content
    upd_body += body_content
    for info in mp3_info:
        src, title, artist, img = info
        #upd_body += f"{{ src : 'a/{title}.mp3', name: '{title}', artist: '{artist}', img: 'a/{title}.jpg' }},\n"
    #upd_body += f"{{ src: 'mp3/{num}.mp3', name: '{title}', artist: '', img: 'img/{num}.jpg' }},\n"
   
    html_content += upd_body
    html_content += tail_content
    with open(filename, "w") as file:
        file.write(html_content)
    with open("body.html", "w") as body:
        body.write(upd_body)

def main():
    folder_path = 'b'
    #html_file = 'output.html'
    mp3_info_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):
            file_path = os.path.join(folder_path, filename)
            title, artist, img_path = get_mp3_info(file_path)
            mp3_info_list.append((file_path, title, artist, img_path))

    save_to_html(mp3_info_list)

if __name__ == "__main__":
    main()

