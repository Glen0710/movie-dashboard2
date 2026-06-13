# Movie Rating Dashboard

A beautiful, interactive movie rating dashboard built with Flask (Python), SQLite, and HTML/CSS/JavaScript.

## Features

✨ **Interactive Dashboard**
- Real-time statistics and metrics
- Beautiful responsive UI with gradient backgrounds
- Advanced filtering and search capabilities

📊 **Analytics & Charts**
- Rating distribution visualization
- Top industries breakdown
- Genre analysis
- Top-rated movies list
- Average ratings and review counts

🔍 **Search & Filter**
- Search movies by name
- Filter by minimum rating
- Filter by year of release
- Filter by film industry (Bollywood, Kollywood, etc.)
- Filter by genre

## Project Structure

```
movie-dashboard/
├── app.py              # Flask backend application
├── init_db.py          # Database initialization script
├── requirements.txt    # Python dependencies
├── movies.db          # SQLite database (created after running init_db.py)
├── movies.csv         # Your movie data
└── templates/
    └── index.html     # Frontend dashboard
```

## Installation & Setup

### 1. Prerequisites
- Python 3.7+
- pip (Python package manager)

### 2. Install Dependencies

Navigate to the project directory and install required packages:

```bash
cd movie-dashboard
pip install -r requirements.txt
```

### 3. Initialize Database

Copy your `movies.csv` file to the `movie-dashboard` folder, then run:

```bash
python init_db.py
```

This will:
- Create SQLite database (`movies.db`)
- Load all movie data from CSV
- Create indexes for faster queries
- Clean and parse the data properly

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

The dashboard will be available at: **http://localhost:5000**

## Usage

### Main Features

1. **Dashboard Overview**
   - View total number of movies
   - Check average rating across all movies
   - See average number of reviews per movie

2. **Search**
   - Type a movie name in the search box and press Enter
   - Results update in real-time

3. **Filters**
   - Set minimum rating threshold
   - Filter by release year
   - Select specific industry (Bollywood, Kollywood, etc.)
   - Choose genre (Drama, Comedy, etc.)
   - Click "Apply Filters" to update results

4. **Charts & Analytics**
   - **Rating Distribution**: Bar chart showing how many movies fall in each rating range
   - **Top Industries**: Pie chart showing movie distribution by film industry
   - **Top Genres**: Bar chart with average ratings by genre
   - **Top 5 Movies**: List of highest-rated movies with ratings

5. **Movie Cards**
   - Browse all movies in an attractive card layout
   - See rating, year, industry, director, and genres
   - Hover over cards for interactive effects

## API Endpoints

The Flask backend provides these endpoints:

- `GET /` - Main dashboard page
- `GET /api/movies` - Get all movies
- `GET /api/stats` - Get dashboard statistics
- `GET /api/search?q=<query>` - Search movies by name
- `GET /api/filter` - Filter movies with parameters:
  - `min_rating` - Minimum rating (0-10)
  - `year` - Release year
  - `industry` - Film industry
  - `genre` - Genre name
- `GET /api/genres` - Get all available genres
- `GET /api/industries` - Get all available industries

## Data Processing

The `init_db.py` script handles:
- ✅ CSV parsing and data cleaning
- ✅ Converting rating strings to floats
- ✅ Parsing watch duration (e.g., "2 hours 27 minutes" → 147 minutes)
- ✅ Cleaning box office numbers (e.g., "$138,288.00" → 138288)
- ✅ Handling missing values gracefully
- ✅ Creating database indexes for performance

## Customization

### Change Port
In `app.py`, modify the last line:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change 5000 to desired port
```

### Database Location
In both `app.py` and `init_db.py`, change:
```python
DATABASE = 'movies.db'  # Change path as needed
```

### Styling
Edit `templates/index.html` to customize:
- Colors (gradient backgrounds)
- Chart configurations
- Card layouts
- Responsive breakpoints

## Troubleshooting

**Issue: "No module named 'flask'"**
- Run: `pip install -r requirements.txt`

**Issue: Database not found**
- Make sure you ran: `python init_db.py`
- Ensure `movies.csv` is in the project directory

**Issue: Port 5000 already in use**
- Change the port in `app.py` to something like 5001, 5002, etc.

**Issue: CSV encoding errors**
- Ensure `movies.csv` is UTF-8 encoded

## Browser Support

Works best with modern browsers:
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance Notes

- Database queries are optimized with indexes
- Charts use Chart.js for efficient rendering
- Responsive design works on mobile, tablet, and desktop
- Search results cached in browser for smooth UX

## License

This project is open source and free to use.

## Contact & Support

For issues or questions, check your setup steps and ensure all dependencies are installed correctly.

Enjoy exploring your movie data! 🎬🍿
