# AI YouTube-to-Blog Generator

Turn a YouTube video into a clean, structured blog post with AI—paste a link, wait a bit, and get an editable article that reads like a human wrote it.

## Why This Exists

Writing from scratch is hard and time-consuming. This project jumpstarts the process by transcribing speech and shaping it into a readable blog with headings, sections, and a conclusion.

## Features

- **Instant Blog Creation**  
  Paste a video URL and get a coherent, sectioned article with introduction, body, and conclusion.  
- **Accurate Transcription**  
  Speech-to-text via Faster-Whisper for reliable English transcripts.  
- **Structured Output**  
  Blog generation with an instruction-tuned model (FLAN-T5) for clear sections and flow.  
- **Responsive UI**  
  Simple, mobile-friendly interface built with TailwindCSS and Django templates.  
- **User Accounts**  
  Signup/login flow and a clean result page that hides raw transcripts by default.

## Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/ai-youtube-blog-generator.git
   cd ai-youtube-blog-generator
   ```

2. **Set up a virtual environment**  
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Use the app**  
   Open your browser at `http://127.0.0.1:8000`, paste a YouTube URL, and generate your blog!

> **Tip:** If a video is restricted, try a public video with clear English speech under 30 minutes.

## How It Works

1. **Audio Download**  
   Downloads audio from the provided YouTube URL.  
2. **Transcription**  
   Converts speech to text with Faster-Whisper, optimized for CPU use.  
3. **Blog Generation**  
   Transforms the transcript into a structured article with headings and a conclusion using FLAN-T5.

## Tech Stack

- **Backend:** Django, Python  
- **AI:** Faster-Whisper (speech-to-text), Hugging Face Transformers (FLAN-T5)  
- **Frontend:** Django templates, TailwindCSS, minimal JavaScript  
- **Utilities:** PyTubeFix for audio extraction

## Project Structure

```
ai-youtube-blog-generator/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── myproject/           # Django settings, URLs, WSGI/ASGI
├── blogapp/             # Views, models, utils (ASR + blog generation), URLs
└── templates/           # base.html, index.html, result.html, auth pages
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy blogging! 🎉