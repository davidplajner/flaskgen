# flaskgen 🚀  

**flaskgen** is a lightweight Flask project generator that helps you kickstart new Flask apps in seconds. No more repetitive setup—just run one command and get started with a structured boilerplate.  

## ✨ Features  

- **Pre-configured SQLite3 connection** – Database ready from the start.  
- **CSS reset** – A clean slate for styling.  
- **HTML template with Google Fonts** – Includes Outfit, Caveat, and Fira Code.  
- **Prebuilt home route (`/`)** – Start coding right away.  
- **Reusable utilities**:  
  - `modules.py` – Includes a `uuid_generator`.  
  - `queries.py` – Ready-to-use SQLite3 query functions.  
- **Empty `index.js`** – For adding custom JavaScript when needed.  

## ⚡ Quick Start  

1. Install Cookiecutter if you haven't already:  
   ```bash
   pip install cookiecutter
   ```  

2. Generate a new Flask project using **flaskgen**:  
   ```bash
   cookiecutter https://github.com/davidplajner/flaskgen
   ```  

3. Follow the prompts and start coding! 🎉  

## 📂 Project Structure  

```
your-new-project/
│-- static/
│   ├── css/reset.css
│   ├── js/index.js
│-- templates/
│   ├── base.html
│   ├── index.html
│-- app.py
│-- modules.py
│-- queries.py
│-- config.py
│-- README.md
```

## 📜 License  

MIT – Use it, tweak it, and build amazing things with it. 🚀  
