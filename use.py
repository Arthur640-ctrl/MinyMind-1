from loguru import logger
from pxl_gpt.tokenizer import BPETokenizer

test_sentences = [
    # Français courant
    "Bonjour, comment ça va aujourd’hui ?",
    "Je vais à la bibliothèque pour emprunter un livre.",
    "C’est incroyable ! Tu as vraiment réussi ton projet.",

    # Mots avec accents et caractères spéciaux
    "François aime le café au lait et les croissants.",
    "La naïveté est parfois une force, pas une faiblesse.",
    "L’élève étudie l’histoire de l’Île-de-France.",

    # Mots inconnus ou composés
    "Anticonstitutionnellement, c’est le mot le plus long.",
    "Supercalifragilisticexpialidocious est un mot inventé.",
    "PyTorch et Transformers sont des bibliothèques Python utiles.",

    # Chiffres, ponctuation et symboles
    "Mon numéro est le 06-12-34-56-78 !",
    "Prix : 12,99 € – réduction de 20 %.",
    "Email : exemple@test.com, site web : https://www.example.org",

    # Emojis et symboles Unicode
    "J’adore 😄, mais parfois 😢.",
    "Les maths : ∑, ∫, √, π sont fascinants.",
    "Le code peut être 💻 ou 🤖 selon le projet."
]


def main():
    tokenizer = BPETokenizer()
    tokenizer.load("data/tokenizer.json")

    logger.info("Testing tokenizer...")
    for sentence in test_sentences:
        print("=====")
        print(f"Test pour la phrase : '{sentence}'")
        encoded_text = tokenizer.encode(sentence)
        logger.info(f"Encoded : {encoded_text}")

        decoded_text = tokenizer.decode(encoded_text)
        logger.info(f"Decoded text: {decoded_text}")




if __name__ == "__main__":
    main()
