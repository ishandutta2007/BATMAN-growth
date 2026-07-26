$readme = "README.md"
$content = [System.IO.File]::ReadAllText($readme)

# Step 1: Emojis
$content = $content.Replace("## Features & Calculations", "## ✨ Features & Calculations 📊")
$content = $content.Replace("## Generated Assets", "## 🖼️ Generated Assets")
$content = $content.Replace("## Usage", "## 🚀 Usage")
$content = $content.Replace("- **Engineer Subset", "👩‍💻 **Engineer Subset")
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "added emojis"
git -c http.sslVerify=false push

# Step 2: SEO optimized
$content = $content.Replace("# BATMAN-growth", "# BATMAN-growth: Tech Company Engineering Headcount Analysis")
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "seo optimised"
git -c http.sslVerify=false push

# Step 3: Badges left
$badges_left = "<p align=`"center`">`n<a href=`"https://github.com/ishandutta2007/Awesome-Awesome-Awesome`"><img src=`"https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github`" alt=`"Awesome`"/></a><a href=`"https://discord.gg/jc4xtF58Ve`"><img src=`"https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white`" alt=`"Discord`" /></a>`n"
$content = $content.Replace("<p align=`"center`">`n  <img", $badges_left + "  <img")
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "badges to left added"
git -c http.sslVerify=false push

# Step 4: Badges right
$badge_right = "<a href=`"https://github.com/ishandutta2007`"><img alt=`"GitHub followers`" src=`"https://img.shields.io/github/followers/ishandutta2007?label=Follow`" /></a>"
$content = $content.Replace("alt=`"Discord`" /></a>", "alt=`"Discord`" /></a>" + $badge_right)
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "badges to right added"
git -c http.sslVerify=false push

# Step 5: Star history
$star_history = "`n`n## ⭐️ Star History`n<div align=`"center`">`n<a href=`"https://www.star-history.com/?repos=ishandutta2007%2FBATMAN-growth&type=date&legend=bottom-right`">`n<picture>`n<source media=`"(prefers-color-scheme: dark)`" srcset=`"https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&theme=dark&legend=bottom-right`" />`n<source media=`"(prefers-color-scheme: light)`" srcset=`"https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right`" />`n<img alt=`"Star History Chart`" src=`"https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right`" />`n</picture>`n</a>`n</div>`n"
$content = $content + $star_history
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "star history added"
git -c http.sslVerify=false push

# Step 6: fix chartrepos
$content = $content.Replace("chartrepos", "chart?repos")
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "fixed star plot"
git -c http.sslVerify=false push

# Step 7: invalid awesome link fixed
$content = $content.Replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
[System.IO.File]::WriteAllText($readme, $content)
git add .
git commit -m "invalid awesome link fixed"
git -c http.sslVerify=false push
