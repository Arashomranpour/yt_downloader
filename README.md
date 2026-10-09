<div align="center">

# ▶️ YouTube Downloader

**A tiny command-line script that lists every available stream of a YouTube video and downloads the one you choose.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pytube](https://img.shields.io/badge/pytube-YouTube-FF0000?logo=youtube&logoColor=white)

</div>

---

## ✨ How it works

1. Paste a YouTube link.
2. The script prints all available streams (resolution, format, audio/video) as a numbered list.
3. Enter the number of the stream you want and it is downloaded to the current folder.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/yt_downloader.git
cd yt_downloader
pip install pytube
python yt.py
```

> ⚠️ Download only content you have the right to save, and respect YouTube's Terms of Service. `pytube` can break when YouTube changes its site; update it with `pip install -U pytube` if downloads fail.

## 📁 Project Structure

```
.
└── yt.py     # Interactive downloader
```

## 🛠️ Tech Stack

`Python` · `pytube`
