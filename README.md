# AI Code Assistant - Calculator Example

This repository demonstrates an AI code assistant capable of understanding and manipulating code within a defined working directory. It provides a calculator application as an example, showcasing the assistant's ability to:

- List files and directories
- Read file contents
- Execute Python files
- Write or overwrite files

## Overview

The core of the assistant lies in its ability to interact with the file system through a set of predefined functions. These functions are exposed to the AI model, allowing it to perform tasks such as exploring the codebase, running scripts, and modifying files.

The calculator application serves as a practical demonstration of these capabilities. The AI can be instructed to perform tasks such as:

- Fixing bugs in the calculator logic
- Adding new features (e.g., trigonometric functions)
- Improving the user interface

## Code Structure

The repository is organized as follows:

-   `.`: The root directory contains the main application logic and configuration.
    -   `main.py`: Entry point for the AI code assistant. It takes a prompt from the command line and uses the Gemini API to generate a response.
    -   `call_function.py`: This file handles calling the different functions the AI model can use.
    -   `prompts.py`: Contains the system prompt that guides the AI's behavior.
    -   `config.py`: Configuration file containing constants such as the maximum number of characters to read from a file (`MAX_CHARS`), the working directory (`WORKING_DIR`), and the maximum number of iterations (`MAX_ITERS`).
    -   `tests.py`: Tests for the main application logic.
    -   `README.md`: This file.
    -   `functions`: directory containing the definitions for each available function.
        -   `get_files_info.py`: Lists files and directories within the working directory.
        -   `get_file_content.py`: Reads the content of a file.
        -   `run_python.py`: Executes a Python file.
        -   `write_file.py`: Writes or overwrites a file.
    -   `calculator`: directory containing the calculator application.
        -   `main.py`: The entry point for the calculator application.
        -   `tests.py`: Unit tests for the calculator.
        -   `pkg`: A package containing the calculator logic.
            -   `calculator.py`: Implements the `Calculator` class, which evaluates mathematical expressions.
            -   `render.py`: Renders the expression and result in a formatted box.

## Configuration

The `config.py` file contains important configuration settings:

-   `MAX_CHARS`: Limits the number of characters read from a file to prevent excessive memory usage.
-   `WORKING_DIR`: Specifies the working directory for the AI assistant. **For demonstration purposes, this is set to `'./calculator'`**, meaning the AI can only access and modify files within the `calculator` directory. This restriction is in place to prevent unintended modifications to the entire file system.
-   `MAX_ITERS`: Limits the number of iterations the AI can perform to prevent infinite loops.

## Running the Assistant

1.  **Set up your environment:**
    -   Install the required dependencies (e.g., using `pip install -r requirements.txt`).
    -   Set the `GEMINI_API_KEY` environment variable with your Gemini API key.

2.  **Run the `main.py` script:**

    ```bash
    python main.py "your prompt here" [--verbose]
    ```

    Replace `"your prompt here"` with the instructions for the AI assistant. The `--verbose` flag enables detailed logging of the AI's actions.

    Example:

    ```bash
    python main.py "Fix the bug in the calculator that causes it to crash when dividing by zero" --verbose
    ```

## Example Scenario: Bug Fixing

Let's say the calculator has a bug where it crashes when dividing by zero. The AI assistant can be instructed to fix this bug by:

1.  Listing the files in the `calculator` directory to identify the relevant files.
2.  Reading the content of `calculator/pkg/calculator.py` to understand the calculator's logic.
3.  Modifying `calculator/pkg/calculator.py` to handle division by zero gracefully (e.g., by raising an exception or returning an error message).
4.  Running the unit tests in `calculator/tests.py` to verify that the bug is fixed and no new issues have been introduced.

## Security Considerations

The AI assistant has the ability to modify files within the designated working directory. It is crucial to carefully configure the `WORKING_DIR` setting to limit the scope of the AI's access and prevent unintended consequences. Always review the AI's proposed changes before applying them to the codebase.

## Disclaimer

This project is provided as a demonstration of AI code assistance capabilities. It is not intended for production use and should be used with caution.

THIS AI AGENT code wrote the entire readme.