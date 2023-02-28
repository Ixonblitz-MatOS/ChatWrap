"""
ChatWrap is a module to simplify the use of openai lib
"""
import openai
from typing import Literal as literal

class Filter:
    """
    Class for simplified openai filtering using the content filter ai
    """
    content_filter_engine="content-filter-alpha"

class Code:
    """
    Class for simplified openai code completion and help using code completion ai
    """
    davinci_code_engine="code-davinci-002"
    cushman_code_engine="code-cushman-001"
    
class Chat:
    """
    Class for simplified openai chatting using text response ai
    """
    davinci_engine="davinci"
    davinciv3_engine="text-davinci-003"
    curie_engine="curie"
    babbage_engine="babbage"
    ada_engine="ada"
    def __init__(self,api_key:str="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",model_engine:str|literal['davinci']|literal["text-davinci-003"]|literal["curie"]|literal["babbage"]|literal["ada"]='davinci')->None:
        """
        Initial configuration for ai communication

        :param str api_key:
        :param str model_engine:
        :raises TypeError: if not isinstance(api_key,str)|is not a literal of one of the supported engines found
        :raises openai.error.AuthenticationError: if no api_key is given
        :raises openai.error.InvalidRequestError: if model does not exist.
        """
        openai.api_key=api_key
        self.model=model_engine
    def ask(self,prompt:str)->str:
        """
        Send a message to be evaluated by openai using one of the text responding ai

        :param str prompt: The prompt to be sent to the AI for completion
        :raises TypeError: if the prompt not isinstance(prompt,str)
        """
        return openai.Completion.create(engine=self.model, prompt=prompt, max_tokens=4000).choices[0].text
a=openai.Completion.create(api_key="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",engine="thisis",prompt="What is 11+12",max_tokens=4000)