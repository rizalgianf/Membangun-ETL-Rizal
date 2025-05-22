# ETL Project

## Overview
This ETL (Extract, Transform, Load) project is designed to facilitate the process of extracting data from various sources, transforming it into a usable format, and loading it into a specified destination. The project is structured to promote modularity and ease of testing.

## Project Structure
```
ETL/
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
├── utils/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── main.py
├── requirements.txt
├── README.md
```

## Components
- **tests/**: Contains unit tests for the ETL process.
  - `test_extract.py`: Tests for extraction functions.
  - `test_transform.py`: Tests for transformation functions.
  - `test_load.py`: Tests for loading functions.

- **utils/**: Contains the core functionality for the ETL process.
  - `extract.py`: Functions for extracting data from various sources.
  - `transform.py`: Functions for transforming the extracted data.
  - `load.py`: Functions for loading the transformed data into a destination.

- **main.py**: The entry point of the ETL process that orchestrates the workflow.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the ETL process, execute the following command:
```
python main.py
```

## Testing
To run the unit tests, use:
```
pytest tests/
```

## License
This project is licensed under the MIT License.