"""
ChatWrap is a module to simplify the use of openai lib
"""
__all__=["setKey","Filter","Code","Chat","Image"]
__version__="0.0.1"
import openai
from io import TextIOWrapper
from typing import Literal as literal
def setKey(key:str)->None:
    """
    Set the key for openai use
    :param str key: key to be set for openai
    """
class base:
    def __init__(self) -> None:pass
    def setKey(self,key:str)->None:
        """
        Set the key for openai use
        :param str key: key to be set for openai
        """
class Filter(base):
    """
    Class for simplified openai filtering using the content filter ai
    """
    content_filter_engine="content-filter-alpha"
    def __init__(self,api_key:str,model_engine:str|literal["content-filter-alpha"])->None:
        """
        Initiates class for content filtering with openai
        :param str api_key: api key for openai
        :param str model_engine: engine type to use
        :raises TypeError: if not isinstance(api_key,str)|isinstance(model_engine,str|literal)
        """
    def checkSafety(self,prompt:str)->tuple[int,literal["safe"]|literal["unsafe"]|literal["possibly unsafe"]]:
        """
        Checks the safety of a prompt with openai
        :param str prompt: prompt to send for checking
        """
class Code(base):
    """
    Class for simplified openai code completion and help using code completion ai
    """
    davinci_code_engine="code-davinci-002"
    cushman_code_engine="code-cushman-001"
    def __init__(self,api_key:str,model_engine:str|literal["code-davinci-002"]|literal["code-cushman-001"]="code-davinci-002") -> None:
        """
        Initial configuration for code completion openai
        :param str api_key: api key for openai
        :param str|literal["code-davinci-002"]|literal["code-cushman-001"] model_engine: engine type for code completion
        :raises TypeError: if not isinstance(api_key,str)|isinstance(model_engine,str)|isinstance(model_engine,literal)

        """
    def getCode(self,prompt:str)->str:
        """
        Send a message to be evaluated by openai using one of the code completion ai

        :param str prompt: The prompt to be sent to the AI for completion
        :raises TypeError: if the prompt not isinstance(prompt,str)
        :raises openai.error.InvalidRequestError: if model does not exist.
        :raises openai.error.AuthenticationError: if no api_key is given
        :raises openai.error.RateLimitError: if you used the quota too much, check your account plan
        """
class Chat(base):
    """
    Class for simplified openai chatting using text response ai
    """
    davinci_engine="davinci"
    davinciv3_engine="text-davinci-003"
    curie_engine="curie"
    babbage_engine="babbage"
    ada_engine="ada"
    def __init__(self,api_key:str,model_engine:str|literal['davinci']|literal["text-davinci-003"]|literal["curie"]|literal["babbage"]|literal["ada"]='davinci')->None:
        """
        Initial configuration for ai communication

        :param str api_key:
        :param str model_engine:
        :raises TypeError: if not isinstance(api_key,str)|is not a literal of one of the supported engines found
        """
    def ask(self,prompt:str)->str:
        """
        Send a message to be evaluated by openai using one of the text responding ai

        :param str prompt: The prompt to be sent to the AI for completion
        :raises TypeError: if the prompt not isinstance(prompt,str)
        :raises openai.error.InvalidRequestError: if model does not exist.
        :raises openai.error.AuthenticationError: if no api_key is given
        :raises openai.error.RateLimitError: if you used the quota too much, check your account plan
        """
class Image(base):
    def __init__(self,api_key:str) -> None:
        """
        Uses openai to create a prompt based image
        """
    def requestImage(self,prompt:str,size:str="1024x1024")->str:
        """
        :param str prompt: prompt for image 
        :returns str: url to image
        :raises openai.error.OpenAIError:
        """
        return openai.Image.create(prompt=prompt,n=1,size=size)['data'][0]['url']
        """
        Creates images based on prompts when given the mask and image and returns the url for them
        :param TextIOWrapper image: original image using rb mode
        :param TextIOWrapper mask: mask for the image using rb mode
        :param str prompt: prompt to change the image 
        :param str size: size of the image. 
        :raises openai.error.OpenAIError:
        """
    def createVariationImage(self,image:TextIOWrapper,size:str="1024x1024")->str:
        """
        Creates variations of an image given
        :param TextIOWrapper image: original image using rb mode
        :param str size: size of the image
        :raises openai.error.OpenAIError:
        """
    def createVariationFromMemory(self,image:bytes,size:str="1024x1024")->str:
        """
        Creates a variation image from memory usually found in io.BytesIO but must be converted to bytes with BytesIO.getvalue()
        :param bytes image: image data
        :param str size: size of the image
        :raises openai.error.OpenAIError:
        """
def getEmbedding(prompt:str,engine:str="text-embedding-ada-002")->dict:
    """
    Gets embeddding using openai
    :param str prompt: The prompt to be embedded
    :param str engine: while ada-002 is suggested this can be changed
    :raises openai.error.OpenAIError:
    """
