import spacy
import streamlit as st
from spacy import displacy
from io import BytesIO
import base64
import base64
import tempfile
from io import BytesIO
from PIL import Image
import webbrowser


nlp_ner = spacy.load("D:/Revival/MLI/NER2/model-best")

# def ner(text):

#     doc = nlp_ner(text)
#     # for ent in doc.ents:
#     #     print(ent.text, ent.label_)

#     # colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"#FFFFFF"}
#     # options = {"colors": colors} 

#     # spacy.displacy.render(doc, style="ent", options= options, jupyter=True)
#     # Generate the displaCy visualization
#     html = displacy.render(doc, style='ent')

#     # Convert HTML to image
#     image = BytesIO()
#     image.write(html.encode())
#     image.seek(0)

#     # Display the image in Streamlit
#     st.image(image, format='png')


# def main():


#     # giving a title
#     st.title('Medical NER')


#     # getting the input data from the user


#     # Get text input from the user
#     text_input = st.text_input('Enter your text')

#     # Display the input text
#     st.write('You entered:', text_input)

    


#     # code for Prediction
#     logo = ''

#     # creating a button for Prediction

#     if st.button('NER'):
#         # Process the text and generate the displaCy visualization
#         image = ner(text_input)

#         # Display the image in Streamlit
#         st.image(image, format='png')
        
        
#     st.success(logo)

# Define a function to process the text and generate the displaCy visualization
# def ner(text):
#     doc = nlp_ner(text)
#     html = displacy.render(doc, style='ent')
#     image = BytesIO()
#     image.write(html.encode())
#     image.seek(0)
#     return image

# def main():
#     # Get text input from the user
#     text_input = st.text_input('Enter your text')

#     # Display the input textif 
#     if st.button('NER'):
#         # Process the text and generate the displaCy visualization
#         image = ner(text_input)
        
#         # Save the image to a temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
#             temp_file.write(image.read())
#             temp_file.seek(0)

#             # Display the image in Streamlit
#             st.image(temp_file.name)

# Define a function to process the text and generate the displaCy visualization
# def ner(text):
#     doc = nlp_ner(text)
#     html = displacy.render(doc, style='ent')
#     image = Image.open(BytesIO(html.encode()))
#     return image

# def main():
#     # Get text input from the user
#     text_input = st.text_input('Enter your text')

#     # Process the text and generate the displaCy visualization
#     image = ner(text_input)

#     # Display the image in Streamlit
#     st.image(image, caption='Named Entity Recognition', use_column_width=True)

# Define a function to process the text and generate the displaCy visualization
# def ner(text):
#     doc = nlp_ner(text)

#     colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"#FFFFFF"}
#     options = {"colors": colors} 

#     # spacy.displacy.render(doc, style="ent", options= options, jupyter=True)
#     html = displacy.render(doc, style="ent", options= options)

#     # Save the HTML to a temporary file
#     with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_file:
#         temp_file.write(html)
#         temp_file_path = temp_file.name

#     # Open the HTML file in a web browser to display the visualization
#     webbrowser.open_new_tab(temp_file_path)

# def main():
#     # Get text input from the user
#     text_input = st.text_input('Enter your text')

#     if st.button('Visualize'):
#         # Process the text and generate the displaCy visualization
#         ner(text_input)

def ner(text):
    doc = nlp_ner(text)
    # html = displacy.render(doc, style='ent', jupyter=False)

    colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION":"purple"}
    options = {'bg':'#FFFFFF',"colors": colors} 

    # spacy.displacy.render(doc, style="ent", options= options, jupyter=True)
    html = displacy.render(doc, style="ent", options= options)

    # Display the HTML content using Streamlit's html component
    st.components.v1.html(html, width=800, height=500, scrolling=True)

def main():
    st.title('Medical NER')
    # Get text input from the user
    text_input = st.text_input('Enter your text')

    if st.button('Visualize'):
        # Process the text and generate the displaCy visualization
        ner(text_input)


if __name__ == '__main__':
    main()
