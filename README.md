# BIONIC_READING

A Bionic Reading-inspired text and EPUB converter, available as a **web app** and the original **Python desktop tool**.

## Web app

Open **[Bionic Reading Studio](https://choppa129.github.io/BIONIC_READING/)** after enabling GitHub Pages.

Features:
- Live text conversion in your browser
- Adjustable bold fraction and font size
- Dark mode and copy text
- Download formatted HTML
- Experimental EPUB conversion and download (preserves existing EPUB resources where possible)

### Run locally

Open [index.html](index.html) in a modern browser. No build step or server is needed. EPUB conversion requires internet access to load JSZip from jsDelivr. All entered text and EPUB files are processed locally in the browser.

### Publish with GitHub Pages

Go to **Settings → Pages → Build and deployment**, select **Deploy from a branch**, choose **main** and **/(root)**, then save. GitHub Pages may take a few minutes to publish. The link above will only work once Pages is enabled.

## Original desktop version

The original Python app (`bionic.py`) and Windows executable (`bionic.exe`) remain available. The desktop tool can process EPUB ebooks. Run the executable or Python script, select an EPUB file, then choose the processing action.

原有桌面版保留不变：运行程序，选择 EPUB 文件，点击“处理文件”。网页版可以直接打开 `index.html`，无需安装 Python。

## Notes

This project is an independent Bionic Reading-style implementation, not an official Bionic Reading product. Reading-speed and comprehension benefits are not established for everyone. EPUB conversion is experimental; use a backup copy and test output in your reader. DRM-protected books are not supported.
