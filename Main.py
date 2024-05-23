import streamlit as st

def generate_prompts(table_of_contents, research_paper_topic, sample_prompt):
    prompts = []
    for heading, word_count in table_of_contents.items():
        filled_prompt = sample_prompt.replace("[word count]", str(word_count))
        filled_prompt = filled_prompt.replace("[topic name]", research_paper_topic)
        filled_prompt = filled_prompt.replace("[heading name]", heading.lower())
        prompts.append(filled_prompt)
    return prompts

def main():
    st.title("Research Paper Prompt Generator")

    # User inputs
    st.sidebar.header("Input Parameters")
    
    research_paper_topic = st.sidebar.text_input("Enter the research paper topic", "")
    
    sample_prompt = st.sidebar.text_input(
        "Enter the sample prompt with blank fields (e.g., '[Word Count] [Heading name] [Research Paper Title]')",
        ""
    ).lower()

    st.sidebar.subheader("Table of Contents")
    toc_count = st.sidebar.number_input("Number of sections in Table of Contents", min_value=1, max_value=20, step=1)

    table_of_contents = {}
    for i in range(toc_count):
        heading = st.sidebar.text_input(f"Heading {i+1}", "")
        word_count = st.sidebar.number_input(f"Word Count for {heading}", min_value=1, step=1)
        if heading:
            table_of_contents[heading] = word_count

    if st.sidebar.button("Generate Prompts"):
        if research_paper_topic and sample_prompt and table_of_contents:
            prompts = generate_prompts(table_of_contents, research_paper_topic, sample_prompt)
            st.subheader("Generated Prompts")
            for i, prompt in enumerate(prompts, start=1):
                st.write(f"{i}. {prompt}")
        else:
            st.error("Please fill in all the fields to generate prompts")

if __name__ == "__main__":
    main()
