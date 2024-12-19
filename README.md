# Horror Movie and Political Climate Analysis

This project analyzes popular horror movies across various decades to explore how their themes reflect and respond to political environments. Follow the steps below to clone and set up the project.

---

## Steps to Clone and Open

### Clone the Repository
1. Open your terminal or command prompt, navigate to the directory where you want to save the project, and run the following command:  
   ```bash
   git clone https://github.com/monishar123/horror-movie-political-analysis.git

2. To set up and run the project, navigate into the project folder by running `cd horror-movie-political-analysis`. 

3. Set up a virtual environment by creating it with `python -m venv .venv` and activating it using `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Mac/Linux. 

4. Install the required Python packages by running `pip install -r requirements.txt`. 

5. In the project directory, create a `.env` file and add your TMDB API key in the format `TMDB_API_KEY=your_api_key_here`, replacing `your_api_key_here` with your actual API key. 

6. Execute the main analysis script by running `python analyze_data.py`, and after the script completes, outputs such as graphs and insights will appear in your terminal or in the specified output folder. 

7. Optionally, you can test the project by running `pytest tests/` to verify the functionality. When finished, deactivate the virtual environment by running `deactivate`.
