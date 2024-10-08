import streamlit as st 
import pandas as pd 


st.write("hello world")

st.header("My new Dashboard")

uploaded_file = st.file_uploader("Choose a CSV File",type="csv")

if uploaded_file is not None:
    st.write(":white_check_mark: File Uloaded!")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by",columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis Column", columns)
    y_column = st.selectbox("Select y-axis Column", columns)

    if st.button("Generate Plot"):
        st.write("All the values for "+selected_value)
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on File upload")


