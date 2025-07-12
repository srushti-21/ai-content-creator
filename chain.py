from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_groq import ChatGroq
from langchain.chains import LLMChain


# ----PROMPT TEMPLATE----

# The user input will go in {topic} variable

def create_blog_chain(api_key):
    
    """Creates and returns an LLMChain for generating blog posts."""

    # PROMPT TEMPLATE
    prompt_template_str = """
    You are an expert content creator AI.Your task is to write a compelling and informative blog post on a given topic.

    INSTRUCTIONS:
    -The blog post should be atleast 100 words long.
    -It must have clear structure: an engaging introduction,several main body paragraphs with
    subheddings, and a concluding summary.
    -Use a friendly and accessible tone, as if you are explaining the topic to a curious friend.
    -Format the output in Markdown.Use '#' for the main title and '##' for subheadings.

    TOPIC: "{topic}"

    YOUR BLOG POST:
    """

    # Create PromptTemplate object
    prompt_template = PromptTemplate(
        input_variable=['topic'],
        template = prompt_template_str
    )

    # Test the Prompt Template (optional)
    # formatted_prompt = prompt_template.format(topic="the benefits of learning new language")
    # print(formatted_prompt)

    # ----LLM----

    #  Initialize LLM we want to use
    llm = ChatGroq(
        model_name = "llama3-8b-8192",
        api_key = api_key
    )

    # ----LLMChain----

    # Create a chain by combining prompt template and the LLM
    blog_chain = LLMChain(
        llm = llm,
        prompt = prompt_template,
        verbose = True # Set to True to see the inner workings of chain
    )
    
    return blog_chain

   
# YOUTUBE TITLES
def create_youtube_title_chain(api_key):
    """Creates and returns an LLMChain for generating YouTube titles."""
    
    # Create output parser instance
    output_parser = CommaSeparatedListOutputParser()
    
    # Get format instructions from parser
    # This string tells LLM how to format its output
    format_instructions = output_parser.get_format_instructions()
    
    # Create Prompt Template , now including the format instructions
    prompt_template_str = """
    You are an expert in YouTube SEO and content strategy.
    Your task is to generate 5 catchy and click-worthy video titles for a given topic.
    
    TOPIC: {topic}
    
    {format_instructions}
    
    """
    
    prompt_template = PromptTemplate(
        template = prompt_template_str,
        input_variables = ['topic'],
        # This tells template that 'format_instructions' is a special variable that will be filled in by output_parser, not by user
        partial_variables = {'format_instructions' : format_instructions}
    )
    
    # LLM
    llm = ChatGroq(
        model_name = "llama3-8b-8192",
        api_key = api_key
    )
    
    # Create chain including output parser
    youtube_title_chain = LLMChain(
        llm=llm,
        prompt = prompt_template,
        output_parser = output_parser,
        verbose = True
    )
    
    return youtube_title_chain
    