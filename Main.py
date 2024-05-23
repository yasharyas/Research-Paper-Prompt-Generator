def generate_prompts(table_of_contents, research_paper_topic, sample_prompt):
    prompts = []
    for heading, word_count in table_of_contents.items():
        filled_prompt = sample_prompt.replace("[Word count]", str(word_count))
        filled_prompt = filled_prompt.replace("[Topic name]", research_paper_topic)
        filled_prompt = filled_prompt.replace("[heading name]", heading.lower())
        prompts.append(filled_prompt)
    return prompts

if __name__ == "__main__":
    # User inputs
    table_of_contents = {

        # Write your index in similar manner
        # "Introduction": 750,
        # "Background": 100,
        # "Federated Learning in Healthcare": 200,
        # "Importance of Diagnosing Urinary Bladder Inflammation": 250,
        # "Objectives of the Study": 200,
        # "Literature Review": 1000,
        # "Federated Learning in Healthcare": 250,
        # "Artificial Neural Networks (ANN) in Medical Diagnostics": 250,
        # "Support Vector Machines (SVM) in Medical Diagnostics": 250,
        # "Comparative Studies on ANN and SVM": 250,
        # "References": 500
        
    }
    research_paper_topic = input("Enter the research paper topic: ")
    sample_prompt = input("Enter the sample prompt with blank fields (e.g., '[Word Count] [Heading name] [Research Paper Title]'): ").lower()

    # Generate prompts
    prompts = generate_prompts(table_of_contents, research_paper_topic, sample_prompt)

    # Display prompts
    print("\nGenerated Prompts:")
    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt}")
