from langchain_core.prompts import PromptTemplate

blog_prompt = PromptTemplate(
    input_variables=["topic","tone","length","audience"],
    template="""
you are an expert content writer.

Write a {length} blog post.

Topic: {topic}
Tone: {tone}
Audience: {audience}

Include:
- Catchy Title
- Introduction
- 4-5 headings
- Practical examples
- Conclusion
- Key takeways

Return the response in Markdown.
"""
)
