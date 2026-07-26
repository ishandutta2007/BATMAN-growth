import os
import subprocess

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

def run_git(msg):
    subprocess.run('git add .', shell=True)
    subprocess.run(f'git commit -m "{msg}"', shell=True)
    subprocess.run('git -c http.sslVerify=false push', shell=True)

# Step 1: Emojis
content1 = content.replace('## Features & Calculations', '## ✨ Features & Calculations 📊')
content1 = content1.replace('## Generated Assets', '## 🖼️ Generated Assets 🚀')
content1 = content1.replace('## Usage', '## 💻 Usage 🔧')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content1)
run_git("added emojis")

# Step 2: SEO optimized
content2 = content1.replace('# BATMAN-growth\n', '# BATMAN-growth: Tech Company Engineering Headcount Analysis\n')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content2)
run_git("seo optimised")

# Step 3: Badges to left
badges_left = '<p align="center">\n<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n</p>\n'
content3 = content2.replace('<p align="center">\n  <img src="assets/banner.svg"', badges_left + '<p align="center">\n  <img src="assets/banner.svg"')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content3)
run_git("badges to left added")

# Step 4: Badges to right
badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
content4 = content3.replace('alt="Discord" /></a>', 'alt="Discord" /></a>' + badge_right)
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content4)
run_git("badges to right added")

# Step 5: Star history
star_history = """
## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FBATMAN-growth&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/BATMAN-growth&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content5 = content4 + star_history
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content5)
run_git("star history added")

# Step 6: Fix chartrepos
content6 = content5.replace('chartrepos', 'chart?repos')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content6)
run_git("fixed star plot")

# Step 7: replace awesome
content7 = content6.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(readme_path, 'w', encoding='utf-8') as f: f.write(content7)
run_git("invalid awesome link fixed")

# Final push (redundant but requested)
subprocess.run('git -c http.sslVerify=false push', shell=True)
