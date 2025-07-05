# 📖 HTML to Audiobook Converter

Convert HTML content into a spoken audiobook — through simple steps involving HTML -> Text -> PDF -> Audio. This is ideal for turning long articles, blog posts, or documentation into hands-free audio experiences.

---

## 🛠 Project Structure

```bash
├── html_to_txt.py         # Converts HTML content into plain text
├── txt_to_pdf.py          # Converts text into a PDF document
├── pdf_to_audiobook.py    # Reads the PDF aloud as an audiobook
├── Links.txt              # (Optional) Store multiple HTML links

 Step 1: Provide HTML Links
If you have multiple links
Save all the links (one per line) into a file named Links.txt.

If you have just one link
You can paste it directly inside the html_to_txt.py script.

Step 2: Convert HTML to Text
Run the following script to fetch and clean the HTML content
python html_to_txt.py(bash)
This script will:
Read the link(s)
Extract readable content
Save it to a .txt file

Step 3: Convert Text to PDF
Turn your text file into a clean, readable PDF by running:
python txt_to_pdf.py(bash)
This generates a PDF file from your previously extracted text.

 Step 4: Listen to the Audiobook
Finally, use the audiobook generator:

python pdf_to_audiobook.py(bash)
A file dialog will ask you to select the PDF.

The content will be read aloud using a neutral TTS voice (not gender-specific).
