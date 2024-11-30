import pandas as pd
import streamlit as st
import altair as alt


st.image('dna-logo.jpg', use_container_width = True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the ***nelceotide composition*** of query **DNA**!
""")

st.header("Enter DNA sequence")

sequence_input = "DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height= 125).upper()
sequence = sequence.splitlines()
sequence = "".join(sequence[1:])

st.write("***")

st.header("INPUT (DNA Query)")
sequence

st.header("OUTPUT (DNA Nucleotide Count)")

x = {
    'A': sequence.count("A"),
    'T': sequence.count("T"),
    'G': sequence.count("G"),
    'C': sequence.count("C")
}

st.subheader('1. Print dictionary')
x

st.subheader("2. Print text")

protine_prts = ['adenine (A)', 'thymine (T)', 'guanine (G)', 'cytosine (C)']
for i in x:
    st.write("There are", str(x[i]), protine_prts.pop(0))


st.subheader("3. Display DataFrame")

df = pd.DataFrame.from_dict(x, orient='index')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'necleotide', 0: 'count'})

st.write(df)


st.subheader("4. Display the bar chart")
p =  alt.Chart(df).mark_bar().encode(
    x = "necleotide",
    y = "count"
)
p = p.properties( width = alt.Step(80) )
st.write(p)