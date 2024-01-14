projects = {
    "Web Scraper": "A Python web scraping tool that extracts data from websites.",
    "Chat Application": "A simple chat application using sockets for communication.",
    "Todo List App": "A basic todo list application with CRUD operations.",
    "Weather App": "Get the current weather information using an API.",
    "URL Shortener": "Shorten long URLs and redirect to the original URL.",
    "Calculator": "A basic calculator with a graphical user interface.",
    "Image Downloader": "Download images from a list of URLs.",
    "Text-Based Game": "A simple text-based game using Python.",
    "Instagram Bot": "Automate interactions on Instagram using a Python bot.",
    "PDF Merger": "Merge multiple PDF files into a single PDF.",
}

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Mini Projects</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        .project-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            gap: 20px;
        }

        .project-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            width: 300px;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1>Python Mini Projects by Shirisha Basnet</h1>
    <div class="project-container">
"""

for project, description in projects.items():
    html_content += f"""
        <div class="project-card">
            <h2>{project}</h2>
            <p>{description}</p>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open("python_mini_projects.html", "w") as html_file:
    html_file.write(html_content)
