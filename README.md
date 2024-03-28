# AI Ideas Enhancer

## Description

AI Ideas Enhancer is a command-line interface (CLI) Python project that allows you to quickly add your project ideas to a Notion database. It leverages AI to generate a title and icon for your project, making it easier to organize and visualize your ideas. Additionally, it provides the functionality to import ideas from a file.

## Installation

To install AI Ideas Enhancer, follow these steps:

1. Clone the repository:
    ```shell
    git clone https://github.com/your-username/project-name.git
    ```

2. Install the project dependencies using Poetry:
    ```shell
    poetry install
    ```

3. Install the project globally using pipx:
    ```shell
    pipx install .
    ```

## Configuration
You need to add the following env variables for the script to be able to authenticate to Gemini and Notion:

Env Variable Name | Description
===
GEMINI_API_KEY | Your Gemini API key
NOTION_API_KEY | Your Notion API key
NOTION_DATABASE_ID | The ID of the Notion database where you want to store your project ideas

## Usage

To use AI Ideas Enhancer, run the following command:

```shell
$ idea "Your project idea"
```

To import from a CSV file for example use:
```shell
$ idea -p path-to-file
```

> Note
>
> If while importing the script failed to process one idea (since generative AIs are unpredictable), it will spit out the index of the failed idea and stop. You can then use `idea -p path-to-file -i beginning-index` to continue from that index, you might keep trying a lot until Gemini starts generating correct titles and icons, so if that's a problem maybe just skip that idea and add it manually

