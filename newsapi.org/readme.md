# News Application

A simple desktop application that displays the latest headlines using a graphical user interface built with Python's Tkinter library.

## Features

- Fetches real-time news articles from NewsAPI - https://newsapi.org/
- Clean, user-friendly GUI interface
- Displays top 10 news articles in a numbered list format
- Automatic news loading on startup

## Screenshots

The application displays news headlines in a 900x350 window with a reload button and scrollable news content.

## Prerequisites

Before running this application, make sure you have:

- Python 3.6 or higher installed
- Internet connection for fetching news data
- A NewsAPI key (see Setup section)

## Installation

1. **Clone or download the project files**
   ```bash
   git clone <your-repository-url>
   cd news-application
   ```

2. **Install required dependencies**
   ```bash
   pip install requests
   ```
   
   Note: `tkinter` comes pre-installed with most Python installations.

## Setup

### Getting a NewsAPI Key

1. Visit [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Generate your API key from the dashboard
4. Copy your API key for use in the application

### Configuration

**Important:** For security reasons, you should store your API key as an environment variable rather than hardcoding it in the source code.

1. **Option 1: Environment Variable (Recommended)**
   - Set an environment variable named `NEWS_API_KEY`
   - Update the code to use: `api_key = os.getenv('NEWS_API_KEY')`

2. **Option 2: Direct Replacement**
   - Replace the existing API key in the code with your own key
   - **Warning:** Never commit API keys to version control

## Usage

1. **Run the application**
   ```bash
   python news_app.py
   ```

2. **Using the application**
   - The app will automatically load the latest news on startup
   - Click the "Reload" button to fetch fresh headlines
   - News articles are displayed as a numbered list
   - Close the window to exit the application

## How It Works

1. **API Integration**: Makes HTTP requests to NewsAPI's top-headlines endpoint
2. **Data Processing**: Parses JSON response and extracts article titles
3. **GUI Display**: Uses Tkinter to create a window with news content
4. **User Interaction**: Reload button allows refreshing content on demand

## API Details

- **Endpoint**: `https://newsapi.org/v2/top-headlines`
- **Parameters**: 
  - `country=us` (United States news)
  - `category=business` (Business news only)
  - `apiKey` (Your personal API key)

## Customization

You can easily modify the application to:

- **Change news category**: Replace `business` with `technology`, `sports`, `health`, etc.
- **Change country**: Replace `us` with other country codes (`gb`, `ca`, `au`, etc.)
- **Display more articles**: Increase the range in the loop (currently set to 10)
- **Modify appearance**: Adjust window size, fonts, colors, and layout

## File Structure

```
news-application/
│
├── news_app.py          # Main application file
├── README.md            # This file
└── requirements.txt     # Python dependencies (optional)
```

## Dependencies

- **requests**: For making HTTP API calls
- **tkinter**: For creating the GUI (built into Python)

## Error Handling

The current version has basic functionality. Consider adding error handling for:

- Network connectivity issues
- Invalid API responses
- API rate limit exceeded
- Missing or invalid API key

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:

- Enhanced error handling
- Better UI design
- Additional news categories
- Search functionality
- Article content preview

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues:

1. Check your internet connection
2. Verify your NewsAPI key is valid and not rate-limited
3. Ensure all dependencies are installed correctly
4. Check the NewsAPI documentation for any service updates

## Version History

- **v1.0**: Initial release with basic news fetching and display functionality

---

**Note**: This application is for educational and personal use. Please respect NewsAPI's terms of service and rate limits.