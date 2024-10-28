In Streamlit, you can bold and increase the size of text using Markdown and HTML tags. Here’s how to do both:

### 1. **Bold Text**
To bold text, you can use Markdown syntax:
```python
st.markdown("**This is bold text**")
```

### 2. **Increase Font Size**
To increase the font size, you can use HTML tags with Streamlit's `st.markdown` and enable `unsafe_allow_html=True`. 

For example:
```python
st.markdown("<h1 style='font-size:24px;'>This is larger text</h1>", unsafe_allow_html=True)
```

### 3. **Combine Bold and Larger Font Size**
To make text both bold and larger:
```python
st.markdown("<h1 style='font-size:24px; font-weight:bold;'>This is bold and larger text</h1>", unsafe_allow_html=True)
```

### Example in Context
If you want to use these in your app to emphasize the title for "Emotion Analysis Result," you can do this:

```python
st.markdown("<h1 style='font-size:24px; font-weight:bold;'>Emotion Analysis Result</h1>", unsafe_allow_html=True)
```

This will display a bold, larger title on the Streamlit page. Adjust the font size by changing the `font-size` value to suit your needs.
