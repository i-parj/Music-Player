# Music-Player
Minimalist Python Music Player. High performance meets clean code. This project handles local audio files with ease, featuring play/pause/skip functionality and a dynamic queue system. Built using Tkinter. Fork it, tweak the UI, and make your desktop sound better.

# 🎵 PyAudio: Zen Music Player

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Experience music without the bloat.** > A lightweight, resource-efficient, and distraction-free audio interface built purely in Python.

---

## 📖 Overview

**PyAudio** is a desktop-native music player designed for audiophiles who value simplicity and performance. While modern players consume gigabytes of RAM just to play a track, PyAudio utilizes the robust **Pygame Mixer engine** to deliver high-fidelity playback with a near-zero memory footprint.

Wrapped in a classic, industrial-style **Tkinter GUI**, it offers a retro-terminal aesthetic while providing all the essential controls you need to manage your local library.

## ✨ Key Features

* **🚀 Zero-Latency Playback:** Powered by the Pygame audio core for instant load times and lag-free audio processing.
* **📂 Batch Library Import:** Smart directory parsing allows you to import entire folders of MP3s in seconds.
* **🎚️ Precision Audio Control:** Real-time volume modulation with a high-resolution slider (0-100% gain).
* **📜 Dynamic Playlist Management:** Visual scrollable tracklist with active state highlighting.
* **⏯️ Full Transport Controls:** Play, Pause, Resume, and Stop functionality with error handling.
* **💻 Cross-Platform Native:** Runs seamlessly on Windows, macOS, and Linux without complex dependencies.

## 🛠️ Tech Stack

* **Core Logic:** Python 3.x
* **GUI Framework:** Tkinter (Standard Library)
* **Audio Engine:** Pygame Mixer
* **OS Integration:** Native OS file dialogs

## 🚀 Getting Started

### Prerequisites

You need Python installed. This project relies on the powerful `pygame` library.

```bash
pip install pygame
