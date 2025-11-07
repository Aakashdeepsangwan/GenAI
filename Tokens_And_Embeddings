# GenAI

Step 1 : Downloading and Running an LLM
>> Using Transformers Library Load a LLM and tokenizer
>> from transformers import AutoModelForCasualLM, AutoTokenizer


Before the prompt is presented to the language  model, it has go through a tockenizer that breaks it into pieces 
    1. Each token has it's token ID

    prompt = "Welcome to Computer Science, it will break you or make you"

    input_id = tokenizer(prompt, return_tensors = "pt"). input_ids.to("cuda")



  --- How Does the Tokenizer Break Down Text ?
    1) Model Design Time
    2) Tokenizer Design choice like vocabulary size
    3) Tokenizer Training - on a specific Dataset

    * Model Design Time : Creator of model use tokenization method, popular methods include 
                          Byte Pair Encoding (BPE) -- Used by GPT
                          WordPiece (Used by Bert)

    * Tokenizer Training : Tokenizer needs to be Trained on a specific dataset to establish best vocabulary, it can use to represent that Dataset

  --- Word Vs SubWord Vs Character Vs Byte Tokens

  Word Token : Challenge with word token is that the tokenizer may be unable to deal with new words that enter the dataset after the tokenizer is trained.
               Example : Apology, apologize, apologetic, apologist
               > As this can solved using Subword Tokenization 

               
  SubWord Token : Contains full and partial words
                  Advantage - Ability to represent new words by breaking down the new token into smaller characters, which tends to be a part of the vocabulary
                  Example : Apolo + gy , Apolo + gize


  Character Token : Another method that can easily deal with new words because it has the raw letters to fall back on
                    Disadvantage : It make the representation easier to tokenize, but makes the modeling more difficult
                                  - "play" one token, a model using character level token need "p-l-a-y" in addition to modelling rest of the sequence
                    Subword Token present an advantage over Character tokens in the ability to fit more text within the limited context length of a Transformer model.
                    -- Model with a context length 1024, we may be able to fit 3X subword tokenization than using character tokens

  Byte Token : Represent Unicode Characters 

*** Some Subword tokenizers also include byte as token in their vocabulary as the final building block to fall back to when they encounter characters they can't represent.




  

    
