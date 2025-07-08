JavaDocs Web Scraper

This is a Python project that scrapes method details from Oracle’s Java 8 API documentation pages such as StringBuffer, ArrayList etc. It extracts the method signatures, modifiers, return types, and descriptions, and stores them in a CSV file.

----------------------------------------------------------
What does this project do?

- Visits any Java class documentation page.
- Extracts the Method Summary as:
  - Modifier and return type (e.g., public StringBuffer)
  - Method signature (e.g., append(String str))
  - Description of the method
- Saves all the extracted data into a file located in the dataset folder.

----------------------------------------------------------
How to clone the project

To get the project onto your computer, you must first clone it using Git. Open a terminal or command prompt and type the following command:

git clone https://github.com/Nathansuares/WebScraper-.git

----------------------------------------------------------
How to create a virtual environment:

Creating a virtual environment ensures that dependencies do not interfere with system Python.
To create a virtual environment, type this:

python -m venv .venv

----------------------------------------------------------
How to activate the virtual environment:
Depending on your operating system, use one of the following commands:

If you are on Windows:
.venv\Scripts\activate

If you are on macOS or Linux:
source .venv/bin/activate

You should now see (.venv) at the beginning of your terminal line, meaning the environment is active.

----------------------------------------------------------
How to install the required libraries:

This project needs two libraries: beautifulsoup4 and crawl4ai. 
These are listed in a file called requirements.txt.

To install all required libraries, use:
pip install -r requirements.txt

----------------------------------------------------------
How to run the project:

To run the scraper and extract method data from the default Java class (StringBuffer), run:
python crawl_java_docs.py

If you want to scrape a different Java class like ArrayList, you can pass the full URL into the command line as:
python crawl_java_docs.py https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html

----------------------------------------------------------
How to change the default URL:

If you prefer not to pass the URL every time, you can change the default URL directly in the file named config.py.
Open config.py and replace the link with your desired JavaDocs class URL:

JAVADOC_URL = "https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html"

----------------------------------------------------------
Where the output goes

After running the scraper, the output CSV will be saved in the dataset folder.

Example output path:
dataset/StringBuffer_methods.csv

Each row of the CSV will contain the following columns:

- modifier_and_type
- method
- description

----------------------------------------------------------
Files to ignore in Git

Before pushing your code to GitHub, make sure you exclude unnecessary files using a .gitignore file.

Add the following lines to .gitignore:

__pycache__/
*.pyc
.venv/

This ensures that compiled files and virtual environments are not tracked by Git.

----------------------------------------------------------
----------------------------------------------------------

