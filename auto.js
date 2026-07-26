const fs = require('fs');
const { execSync } = require('child_process');

function run(cmd) {
    try {
        execSync(cmd, {stdio: 'inherit'});
    } catch(e) {
        console.error(e);
    }
}

let content = fs.readFileSync('README.md', 'utf8');

// 1. Emojis
content = content.replace('## Features & Calculations', '## ✨ Features & Calculations 📊');
content = content.replace('## Generated Assets', '## 🖼️ Generated Assets');
content = content.replace('## Usage', '## 🚀 Usage');
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "added emojis" && git -c http.sslVerify=false push');

// 2. SEO
content = content.replace('# BATMAN-growth', '# BATMAN-growth: Tech Company Engineering Headcount Analysis');
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "seo optimised" && git -c http.sslVerify=false push');

// 3. Badges left
let left = `<p align="center">\n<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n`;
content = content.replace('<p align="center">\n  <img', left + '  <img');
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "badges to left added" && git -c http.sslVerify=false push');

// 4. Badges right
let right = `<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>`;
content = content.replace('alt="Discord" /></a>', 'alt="Discord" /></a>' + right);
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "badges to right added" && git -c http.sslVerify=false push');

// 5. Star history
let star = `\n## ⭐️ Star History\n<div align="center">\n<a href="https://www.star-history.com/?repos=ishandutta2007%2FBATMAN-growth&type=date&legend=bottom-right">\n<picture>\n<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&theme=dark&legend=bottom-right" />\n<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right" />\n<img alt="Star History Chart" src="https://api.star-history.com/chartrepos=ishandutta2007/BATMAN-growth&type=date&legend=bottom-right" />\n</picture>\n</a>\n</div>\n`;
content = content + star;
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "star history added" && git -c http.sslVerify=false push');

// 6. Fix chartrepos
content = content.replace(/chartrepos/g, 'chart?repos');
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "fixed star plot" && git -c http.sslVerify=false push');

// 7. Fix awesome
content = content.replace(/https:\/\/github.com\/sindresorhus\/awesome/g, 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome');
fs.writeFileSync('README.md', content);
run('git add . && git commit -m "invalid awesome link fixed" && git -c http.sslVerify=false push');
