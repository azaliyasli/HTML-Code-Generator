import base64
from msConnection import conn, cursor

# Pull data
cursor.execute("SELECT title, description, photo_url, photo_file FROM photos")
rows = cursor.fetchall()

# Columns' names
columns = [desc[0] for desc in cursor.description]

# Create dictionary 
projects = [dict(zip(columns, row)) for row in rows]

cursor.close()
conn.close()

#Create HTML 
html = ""

html += f'''
  <html>
  <head>
  <title>Page Title</title>
  </head>
  <body>
  <div>
'''

for project in projects:
    img_html = ""

    if project["photo_url"]:
        img_html = f'<img src="{project["photo_url"]}" alt="Photo" width="300">'
    elif project["photo_file"]:
        base64_img = base64.b64encode(project["photo_file"]).decode("utf-8")
        img_html = f'<img src="data:image/jpeg;base64,{base64_img}" alt="Photo" width="300">'
    
    html += f'''
    <div class="card">
        <h2>{project["title"]}</h2>
        <p>{project["description"]}</p>
        {img_html}
    </div>
    '''

html += f'''
  </div>
  </body>
  </html>
'''

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML başarıyla oluşturuldu!")