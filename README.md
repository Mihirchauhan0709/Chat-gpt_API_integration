# Chat-gpt_API_integration

# AI Advice Generator README

## Introduction
This repository contains a Python script that leverages the OpenAI API to generate AI-driven advice based on user-provided information and questions. This README will guide you through the setup and usage of this script.

## Prerequisites
Before you can use this code, you need to obtain an API key from OpenAI. You can sign up for an API key on the [OpenAI website](https://beta.openai.com/signup/). Once you have your API key, replace `'YOUR_API_KEY'` in the code with your actual API key.

## Installation
1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/Mihirchauhan0709/Chat-gpt_API_integration.git
   ```
2. Navigate to the project directory:
   ```
   cd Chat-gpt_API_integration
   ```

3. Install the required Python packages using pip:
   ```
   pip install openai
   ```

## Usage
To use the AI advice generator, follow these steps:

1. Open a terminal and navigate to the project directory where the script is located.

2. Run the script using Python:
   ```
   python api.py
   ```

3. You will be prompted to provide the following information:
   - User Profile: Enter your profile information (e.g., Name: John, Age: 30, Gender: Male, Profession: Engineer).
   - Area of Interest: Specify your area of interest (e.g., Subject: Math).
   - Question: Enter the question for which you need advice.

4. After providing the required input, the script will send a request to the OpenAI API and retrieve AI-generated advice based on your input.

5. The AI-generated advice will be displayed on the terminal.

## Configuration Options
You can adjust the behavior of the AI advice generator by modifying the following parameters in the `generate_advice` function within the `api.py` script:

- `max_tokens`: Control the length of the AI-generated response by adjusting the `max_tokens` parameter. Increase it for longer responses or decrease it for shorter responses.
- `temperature`: Adjust the `temperature` parameter to control the randomness of the AI's responses. Higher values (e.g., 0.7) make responses more random, while lower values (e.g., 0.2) make responses more deterministic.

## Example
Here's an example of how to use the AI advice generator:

```
Enter your profile information (e.g., Name: John, Age: 30, Gender: Male, Profession: Engineer): John, 30, Male, Engineer
Enter your area of interest (e.g., Subject: Math): Math
Enter your question: How can I improve my math skills?

AI-Generated Advice:
[AI-generated advice will be displayed here]
```
![Example Output](https://github.com/Mihirchauhan0709/Chat-gpt_API_integration/blob/main/Screenshot%202023-10-02%20175746.png)


## Notes
- Make sure to keep your API key secure and do not share it publicly.
- The OpenAI API usage may incur costs based on the number of requests you make. Please refer to OpenAI's pricing information for details.


## Author
Mihir Chauhan

If you have any questions or encounter any issues while using the AI advice generator, feel free to contact mihirchauhan951@gmail.com.
