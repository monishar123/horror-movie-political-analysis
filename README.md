# Horror Movies and Political Climate Analysis

## Project Overview
This project analyzes popular horror movies across various decades to explore how their themes, narratives, and societal anxieties reflect and respond to the political environments of their times. By identifying key films, examining political contexts, and creating visualizations, this project demonstrates the role of the horror genre as a form of cultural commentary.

---

## Goals

### Primary Goal
- **Analyze popular horror movies from various decades** to understand how their themes, narratives, and societal anxieties reflect and respond to the political environment of their respective times.

### Additional Goals
1. **Identify Patterns**: Examine recurring themes and motifs within horror films across different decades, linking them to significant political events and societal changes.
2. **Cultural Analysis**: Investigate how horror films portray marginalized groups and address social justice issues, highlighting the genre's evolution in response to shifting societal attitudes.
3. **Create a Visual Representation**: Develop a timeline or visual aid that maps the release of notable horror films against major political events.
4. **Engage with Audiences**: Present findings through a well-structured report or presentation that invites discussion about the implications of horror films in reflecting societal fears and the political landscape.

---

## Features
- **Data Collection**: Includes horror movies by decade (titles, release years, box office performance).
- **Political Context**: Analysis of political events or movements coinciding with each film’s release decade.
- **Visualization**: Illustrates correlations between horror film themes and political climates.

---

## Tools and Technologies
- **Programming Languages**: Python (for data analysis and visualization)
- **Libraries**:
  - Pandas (data manipulation and analysis)
  - NumPy (numerical computations)
- **APIs**:
  - IMDb API (for movie data: genre, ratings)
  - Political event databases (e.g., US government archives, Wikipedia)
- **Web Development**: HTML/CSS/JavaScript for a user-friendly interface
- **Data Sources**:
  - IMDb and Rotten Tomatoes (movie data)
  - News APIs (political context and articles)

## How to Run the Project

# How to Run the Project

To run the project, follow these steps: 

1. **Clone the Repository**: Open your terminal or command prompt, navigate to the directory where you want to save the project, and run:  
   ```bash
git clone https://github.com/monishar123/horror-movie-political-analysis.git 

2. set up a virtual environment by running `python -m venv .venv` and activating it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Mac/Linux. 

3. install the required dependencies by running `pip install -r requirements.txt`. Step 

4. create a `.env` file in the project directory and add your TMDB API key in the format `TMDB_API_KEY=your_api_key_here`, replacing `your_api_key_here` with your actual API key. 

5. execute the main analysis script with `python analyze_data.py`, and view the outputs, such as generated graphs and insights, which will appear in the output directory or terminal. Optionally, in 

6. test the project by running `pytest tests/` to ensure the script processes data correctly and passes all tests. 

7. when finished, deactivate the virtual environment by running `deactivate`. Make sure Python 3.8 or higher is installed on your system before starting. If you encounter any issues, refer to the GitHub repository’s README or open an issue for support.

# Challenges and Improvements
1. **Legend Complexity**: Simplify by grouping similar crisis types into broader categories for clarity.  
2. **Readability**: Improve x-axis label presentation by rotating or filtering by decades.  
3. **Focused Analysis**: Deepen insights by filtering data by specific decades or crisis types.

# Conclusion
This project demonstrates the intersection of horror films and political climates, showcasing the horror genre as a lens for examining societal fears and political anxieties. By analyzing films across decades, this work emphasizes the genre's cultural significance and evolution in response to societal changes.
