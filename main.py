from data_loader import DataLoader
from vector_db_client import VectorDBClient
from llm_client import LLMClient


def main():
    # load data
    data_loader = DataLoader("top_rated_wines.csv", ["variety"])
    data = data_loader.get_data()

    # get vector db client
    vector_db_client = VectorDBClient("wines")
    vector_db_client.upload_data(data, "notes")

    # search for wines in vector db
    user_prompt = "Suggest me one best Malbec wine from Argentina"
    hits = vector_db_client.search(user_prompt)

    # invoke llm client
    llm_client = LLMClient()
    message = llm_client.chat(
        "You are chatbot, a wine specialist. Your top priority is to help guide users into selecting amazing wine and guide them with their requests.",
        user_prompt,
        [hit.payload for hit in hits],
    )
    print("Result from vector db search: ", [hit.payload["name"] for hit in hits])
    print("Response from llm chat: ", message.content)


main()

# References:
# https://github.com/Mozilla-Ocho/llamafile
# https://github.com/alfredodeza/learn-retrieval-augmented-generation
# https://github.com/anupamgit/create_rag_with_llm
