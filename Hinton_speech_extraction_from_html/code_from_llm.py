from bs4 import BeautifulSoup

def extract_transcript(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all segments
    segments = soup.find_all(class_='segment-text')

    # Extract text from each segment
    transcript_text = ' '.join(segment.get_text().strip() for segment in segments)

    return transcript_text

# Specify the path to your HTML file
# html_file_path = 'path_to_your_html_file.html' # changing this line to my path
html_file_path = 'hinton_scary_ai_talk_html.txt'
transcript = extract_transcript(html_file_path)
print(transcript)
