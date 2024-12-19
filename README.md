# Horror Movie and Political Climate Analysis

This project analyzes popular horror movies across various decades to explore how their themes reflect and respond to political environments. Follow the steps below to clone and set up the project.

---

## Steps to Clone and Open

1. **Clone the Repository**:  
   Open your terminal or command prompt, navigate to the directory where you want to save the project, and run the following command:  
   ```bash
   git clone https://github.com/monishar123/horror-movie-political-analysis.git


2. Navigate to the Project Folder:
To set up and run the project, navigate into the project folder by running:

bash
Copy code
cd horror-movie-political-analysis

3. Set Up a Virtual Environment:
Create a virtual environment with:

bash
Copy code
python -m venv .venv

Activate the virtual environment:

On Windows:
bash
Copy code
.venv\Scripts\activate

On Mac/Linux:
bash
Copy code
source .venv/bin/activate

4. Install Dependencies:
Install the required Python packages by running:

bash
Copy code
pip install -r requirements.txt

5. Add Your API Key:
In the project directory, create a .env file and add the following line:

plaintext
Copy code
TMDB_API_KEY=47370f021e29ef5dfbd2cbf6b8e15516

6. Run the Analysis:
Execute the main analysis script:

bash
Copy code
python analyze_data.py

After the script completes, outputs such as graphs and insights will appear in your terminal or in the specified output folder.

7. Test the Project (Optional):
You can test the project by running:

bash
Copy code
pytest tests/

8. Deactivate the Virtual Environment:
When finished, deactivate the virtual environment by running:

bash
Copy code
deactivate

Conclusion
This project explores the intersection of horror movies and political climates, showcasing how the genre reflects societal fears and anxieties across different decades. By following the steps above, you can analyze key insights, generate visualizations, and understand the impact of political environments on horror movie themes. 