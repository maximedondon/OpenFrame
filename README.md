# OpenFrame for Cinema 4D

**OpenFrame** is a lightweight, professional grayscalegorilla Social Frame plugin alternative for Cinema 4D (optimized for C4D 2026+) that overlays social media aspect ratio guides directly in your viewport.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![C4D](https://img.shields.io/badge/Cinema%204D-2026%2B-orange.svg)
![Language](https://img.shields.io/badge/language-Python-yellow.svg)

---

## Features

- **Standard Social Ratios**: One-click toggles for:
  - `1:1` (Square - Instagram/Post)
  - `4:5` (Portrait - Instagram Feed)
  - `9:16` (Stories/Reels/TikTok)
  - `16:9` (Widescreen)
- **Custom Ratios**: Input your own width/height values for specific delivery formats.
- **Smart Display**: Guides only appear when you are looking through the camera containing the tag, keeping your editor view clean.
- **Color Customization**: Pick any color for your guides to ensure visibility against your scene.
- **2D Overlay**: Clean, screen-space drawing that respects your camera's safe frames.

## Installation

1. **Download** the `OpenFrame` folder.
2. **Locate your Plugins folder**:
   - Open Cinema 4D.
   - Go to `Edit` > `Preferences...`.
   - Click the `Open Preferences Folder...` button at the bottom.
   - Navigate to the `plugins` folder.
3. **Copy** the `OpenFrame` folder into that directory.
4. **Restart** Cinema 4D.

## Usage

1. **Add the Tag**: Right-click on any **Camera** object in your Object Manager.
2. Navigate to **Tags** > **Extensions** > **OpenFrame** (or use the Shift+C commander and type "Open Frame").
3. **Select Ratios**: In the Tag attributes, check the boxes for the ratios you want to visualize.
4. **Customize**: Adjust the color or enter a custom ratio if needed.

## Project Structure

```text
OpenFrame/
├── OpenFrame.pyp      # Main plugin logic
├── res/               # Resource files (UI, Icons, Strings)
│   ├── description/   # UI Layout definitions
│   ├── strings_en-US/ # English translations
│   ├── strings_fr-FR/ # French translations
│   └── icon.png       # Plugin icon
└── README.md          # This file
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
