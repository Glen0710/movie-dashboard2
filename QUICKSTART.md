# Quick Start Guide

## 🚀 Get Your Movie Dashboard Running in 3 Steps

### Step 1: Install Dependencies
Open PowerShell or Command Prompt and navigate to the project folder:
```
cd C:\Users\Glenm\Downloads\movie-dashboard
pip install -r requirements.txt
```

### Step 2: Initialize the Database
Run the database initialization script:
```
python init_db.py
```

This will create `movies.db` and import all your movie data from `movies.csv`.
Expected output:
```
Database initialized successfully!
Total movies inserted: [number of movies]
```

### Step 3: Start the Application
Run the Flask server:
```
python app.py
```

Expected output:
```
* Running on http://127.0.0.1:5000
```

### Step 4: Open in Browser
Go to: **http://localhost:5000**

---

## 📊 What You Can Do

✅ **View Dashboard Stats**
- Total movies count
- Average rating
- Average reviews

✅ **Search & Filter**
- Search movies by name
- Filter by minimum rating
- Filter by year
- Filter by industry (Bollywood, Kollywood, etc.)
- Filter by genre

✅ **Analyze Data**
- Rating distribution chart
- Top industries pie chart
- Top genres bar chart
- Top 5 rated movies

✅ **Browse Movies**
- Interactive movie cards
- Director info
- Genre and industry info
- Rating and review counts

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `app.py` | Flask web server and API endpoints |
| `init_db.py` | Database initialization and CSV import |
| `movies.csv` | Your movie data |
| `templates/index.html` | Dashboard frontend (HTML/CSS/JS) |
| `requirements.txt` | Python package dependencies |
| `README.md` | Full documentation |

---

## 🔧 Troubleshooting

**Port 5000 already in use?**
- Edit `app.py` last line: change `port=5000` to `port=5001`

**"No module named flask"?**
- Run: `pip install -r requirements.txt`

**Need to add more movies?**
- Update `movies.csv` and run: `python init_db.py`

**Want to change styling?**
- Edit `templates/index.html` (the CSS section)

---

## 💡 Tips

- The dashboard auto-loads on first visit
- Search works with partial movie names
- Filters can be combined for powerful searches
- Charts update when you apply filters
- All data is stored locally in `movies.db`

---

**Need help?** Check `README.md` for detailed documentation.

Happy exploring! 🎬🍿
